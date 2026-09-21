"""Append-only dated ledger. Every funnel/deposit event recorded with date + source."""
import csv
import os
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
LEDGER_DIR = os.path.join(BASE, "ledger")
EVENTS_CSV = os.path.join(LEDGER_DIR, "events.csv")
COLUMNS = ["ts_utc", "kind", "source", "detail", "amount_cents", "currency", "lead_ref"]

_fields = None  # cache


def _ensure():
    global _fields
    os.makedirs(LEDGER_DIR, exist_ok=True)
    if not os.path.exists(EVENTS_CSV):
        with open(EVENTS_CSV, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(COLUMNS)
    with open(EVENTS_CSV, newline="", encoding="utf-8") as f:
        _fields = f.readline().strip().split(",")


def log(kind, source, detail="", amount_cents=None, currency="usd", lead_ref=""):
    _ensure()
    row = {
        "ts_utc": datetime.now(timezone.utc).isoformat(),
        "kind": kind,           # deposit | lead_contacted | lead_engaged | lead_converted | blocker | report
        "source": source,       # stripe | lead_engine | orchestrator | manual
        "detail": detail,
        "amount_cents": amount_cents if amount_cents is not None else "",
        "currency": currency,
        "lead_ref": lead_ref,
    }
    with open(EVENTS_CSV, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=COLUMNS).writerow(row)
    return row


def read():
    _ensure()
    rows = []
    with open(EVENTS_CSV, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows


def totals_since(days=7):
    """Return succeeded deposit totals over the trailing N days from the ledger."""
    from datetime import timedelta
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    total = 0
    count = 0
    for r in read():
        if r.get("kind") != "deposit":
            continue
        try:
            ts = datetime.fromisoformat(r["ts_utc"])
        except Exception:
            continue
        if ts >= cutoff and r.get("amount_cents"):
            try:
                amount = int(r["amount_cents"])
                if amount is None or amount <= 0:
                    continue
                # skip zero/refund
                total += amount
                count += 1
            except ValueError:
                continue
    return total, count