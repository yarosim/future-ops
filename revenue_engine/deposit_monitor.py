"""Deposit Monitor — pull successful Stripe payments, append to ledger, compute totals.

Stripe key is loaded from env ONLY (STRIPE_API_KEY or the keptenv loader).
If the key is missing/rotated -> report BLOCKED. Never falls back to stale keys.
Dependency-light: requests (same as existing scripts), no `stripe` SDK.
"""
import json
import os
import sys
from datetime import datetime, timezone, timedelta

import requests

import ledger

# Try the existing env_loader seam if present (non-fatal).
def _load_env_key():
    secrets = os.environ.get("OPENCLAW_SECRETS_DIR",
                             r"C:\Users\YAROS\openclaw\secrets")
    if os.path.exists(os.path.join(secrets, "env_loader.py")) and secrets not in sys.path:
        sys.path.append(secrets)
    try:
        from env_loader import get_key  # type: ignore
        key = get_key("STRIPE_API_KEY")
        if key:
            return key.strip()
    except Exception:
        pass
    # Direct env fallback (avoid printing/leaking the value).
    return (os.environ.get("STRIPE_API_KEY") or "").strip()


STRIPE_API_KEY = _load_env_key()
if not STRIPE_API_KEY:
    # Not fatal so the orchestrator can report BLOCKED gracefully.
    print(json.dumps({"status": "BLOCKED",
                      "reason": "STRIPE_API_KEY missing/not rotated. Supply a rotated key via env."}))


def fetch_payments(since_ts):
    """Return successful PaymentIntents with amount>0 created after since_ts."""
    if not STRIPE_API_KEY:
        return []
    session = requests.Session()
    session.auth = (STRIPE_API_KEY, "")
    session.headers.update({"Stripe-Version": "2023-10-16"})
    out = []
    # page through recent 100
    resp = session.get("https://api.stripe.com/v1/payment_intents",
                       params={"limit": 100}, timeout=30)
    resp.raise_for_status()
    for pi in resp.json().get("data", []):
        if pi.get("status") != "succeeded":
            continue
        created = pi.get("created", 0)
        if created < since_ts:
            continue
        charge = (pi.get("charges") or {}).get("data") or [{}]
        charge = charge[0] or {}
        email = (charge.get("billing_details") or {}).get("email") or charge.get("receipt_email") or pi.get("receipt_email")
        out.append({
            "id": pi.get("id"),
            "created": created,
            "amount": pi.get("amount_received") or pi.get("amount") or 0,
            "currency": pi.get("currency") or "usd",
            "email": email,
            "customer": pi.get("customer"),
            "description": pi.get("description"),
        })
    return out


def run(since_hours=24):
    if not STRIPE_API_KEY:
        return {"status": "BLOCKED", "reason": "STRIPE_API_KEY missing/rotated"}
    cutoff_ts = int((datetime.now(timezone.utc) - timedelta(hours=since_hours)).timestamp())
    try:
        payments = fetch_payments(cutoff_ts)
    except Exception as e:
        return {"status": "ERROR", "reason": str(e)}

    # Dedup against ledger so we don't double-log on manual re-runs.
    seen = {r["detail"] for r in ledger.read() if r["kind"] == "deposit"}
    new = 0
    for p in payments:
        if p["id"] in seen:
            continue
        ledger.log("deposit", "stripe", detail=p["id"],
                   amount_cents=p["amount"], currency=p["currency"],
                   lead_ref=p.get("email") or p.get("customer") or "")
        new += 1

    week_total_cents, week_count = ledger.totals_since(7)
    summary = {
        "status": "OK",
        "new_deposits_this_run": new,
        "week_total_cents": week_total_cents,
        "week_total_usd": round(week_total_cents / 100.0, 2),
        "week_payment_count": week_count,
        "run_utc": datetime.now(timezone.utc).isoformat(),
    }
    return summary


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))