import os, stripe, json
from datetime import datetime, timezone, timedelta

key = (os.environ.get("STRIPE_API_KEY") or "").strip()  # was hardcoded live key (compromised, scrubbed)
if not key:
    raise SystemExit("Missing STRIPE_API_KEY — set a rotated key in env, not in code.")
stripe.api_key = key

PRICES = {
    "AI Compliance Gap Analysis": "price_1TQG5eEJtdifHfsdKpZBUHps",
    "Managed Compliance": "price_1TQG5gEJtdifHfsd7OAiA42l",
}
"""Read-only revenue check — does not create/modify Stripe objects."""

now = datetime.now(timezone.utc)
# Report successful payments (paid), paid checkout sessions, new customers, payout/deposit changes.

def fmt(ts):
    try:
        return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    except Exception:
        return str(ts)

print("=== CHECKOUT SESSIONS ===")
paid_sessions = []
try:
    sessions = stripe.checkout.Session.list(limit=100, status="complete")
    for s in sessions.data:
        line = f"{s.id} | {s.payment_status} | total={s.amount_total} {s.currency} | {fmt(s.created)} | cust={s.customer}"
        print(line)
        if s.payment_status == "paid" and s.amount_total:
            paid_sessions.append((s.id, s.amount_total, s.currency, s.customer))
except Exception as e:
    print("ERR sessions:", e)

print("\n=== PAYMENT INTENTS (recent 100) ===")
pi_rows = []
try:
    pis = stripe.PaymentIntent.list(limit=100)
    for p in pis.data:
        amt = p.amount or 0
        mark = ""
        if amt == 29900: mark = " <-- Gap Analysis($299)"
        elif amt in (99700, 997*100): mark = " <-- Managed Compliance($997)"
        line = f"{p.id} | {p.status} | amt={amt} {p.currency} | {fmt(p.created)} | cust={p.customer}{mark}"
        print(line)
        if p.status == "succeeded":
            pi_rows.append((p.id, amt, p.currency, p.customer))
except Exception as e:
    print("ERR paymentintents:", e)

print("\n=== CUSTOMERS (recent 20) ===")
try:
    cs = stripe.Customer.list(limit=20)
    for c in cs.data:
        print(f"{c.id} | {c.name or ''} | {c.email or ''} | {fmt(c.created)}")
except Exception as e:
    print("ERR customers:", e)

print("\n=== BALANCE / AVAILABLE / PENDING ===")
try:
    bal = stripe.Balance.retrieve()
    for a in bal.available:
        print(f"available: {a.amount} {a.currency}")
    for a in bal.pending:
        print(f"pending: {a.amount} {a.currency}")
except Exception as e:
    print("ERR balance:", e)

print("\n=== PAYOUTS (recent 10) ===")
try:
    po = stripe.Payout.list(limit=10)
    for p in po.data:
        print(f"{p.id} | {p.status} | amt={p.amount} {p.currency} | {fmt(p.created)}")
except Exception as e:
    print("ERR payouts:", e)