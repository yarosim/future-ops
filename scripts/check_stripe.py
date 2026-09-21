import json
import os
import sys
from datetime import datetime, timezone, timedelta

import requests

SECRETS_DIR = r"C:\Users\YAROS\openclaw\secrets"
os.environ.setdefault("OPENCLAW_SECRETS_DIR", SECRETS_DIR)
os.environ.setdefault("OPENCLAW_ENV_PATH", os.path.join(SECRETS_DIR, ".env"))
os.environ.setdefault("OPENCLAW_FALLBACKS_PATH", os.path.join(SECRETS_DIR, "fallbacks.yaml"))

sys.path.append(SECRETS_DIR)
from env_loader import get_key  # type: ignore

API_KEY = get_key("STRIPE_API_KEY")
if not API_KEY:
    raise SystemExit("Missing STRIPE_API_KEY")

CUT_OFF_HOURS = 24
cutoff = datetime.now(timezone.utc) - timedelta(hours=CUT_OFF_HOURS)
cutoff_ts = cutoff.timestamp()

session = requests.Session()
session.auth = (API_KEY, "")
session.headers.update({"Stripe-Version": "2023-10-16"})

resp = session.get("https://api.stripe.com/v1/payment_intents", params={"limit": 100}, timeout=30)
resp.raise_for_status()
payment_intents = resp.json().get("data", [])

book_sales = []
for pi in payment_intents:
    created = pi.get("created", 0)
    if created < cutoff_ts:
        continue
    status = pi.get("status")
    description = (pi.get("description") or "").lower()
    metadata = pi.get("metadata") or {}
    metadata_text = " ".join(str(v) for v in metadata.values()).lower()
    has_flag = (
        "book mega bundle" in description
        or "book mega bundle" in metadata_text
        or metadata.get("product") == "book_mega_bundle"
        or metadata.get("sku") == "book_mega_bundle"
    )
    if not has_flag:
        continue
    if status != "succeeded":
        continue
    charges = pi.get("charges", {}).get("data") or []
    charge = charges[0] if charges else None
    amount_received = pi.get("amount_received") or (charge or {}).get("amount") or pi.get("amount")
    currency = pi.get("currency") or (charge or {}).get("currency")
    email = None
    if charge:
        email = charge.get("billing_details", {}).get("email")
        if not email:
            email = charge.get("receipt_email")
    if not email:
        email = pi.get("receipt_email")
    customer = pi.get("customer")
    book_sales.append(
        {
            "id": pi.get("id"),
            "created": created,
            "amount": amount_received,
            "currency": currency,
            "email": email,
            "customer": customer,
            "description": pi.get("description"),
        }
    )

resp_payouts = session.get("https://api.stripe.com/v1/payouts", params={"limit": 10}, timeout=30)
resp_payouts.raise_for_status()
payouts = resp_payouts.json().get("data", [])
recent_payouts = [p for p in payouts if p.get("created", 0) >= cutoff_ts]

print(
    json.dumps(
        {
            "cutoff_utc": cutoff.isoformat(),
            "book_sales": book_sales,
            "recent_payouts": recent_payouts,
        },
        indent=2,
    )
)
