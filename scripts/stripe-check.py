import subprocess, json, sys
from datetime import datetime

KEY = os.environ.get("STRIPE_API_KEY") or __import__("sys").exit("Missing STRIPE_API_KEY env")

def stripe_get(endpoint, params=None):
    cmd = ["curl.exe", "-s", "-u", f"{KEY}:", f"https://api.stripe.com/v1/{endpoint}"]
    if params:
        for k, v in params.items():
            cmd += ["-d", f"{k}={v}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

def ts_to_date(ts):
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M UTC')

# PAYMENTS
payments = stripe_get("payment_intents/search", {"limit": "50", "query": "status:'succeeded'"})
print("=== SUCCESSFUL PAYMENTS (last 50) ===")
total = 0
count = 0
for p in payments.get("data", []):
    amt = p["amount"] / 100
    print(f"  {p['id']} | ${amt:,.2f} | {ts_to_date(p['created'])} | {p.get('description','N/A')}")
    total += amt
    count += 1
print(f"  TOTAL: {count} payments, ${total:,.2f}")

# CHECKOUT SESSIONS
sessions = stripe_get("checkout/sessions", {"limit": "50"})
print("\n=== CHECKOUT SESSIONS (last 50) ===")
paid_sessions = []
for s in sessions.get("data", []):
    status = s.get("payment_status", "N/A")
    if status == "paid":
        paid_sessions.append(s)
    print(f"  {s['id']} | Status: {s.get('status','?')} | Payment: {status} | {ts_to_date(s['created'])} | Mode: {s.get('mode','?')}")
print(f"  PAID: {len(paid_sessions)}")

# PAYOUTS
payouts = stripe_get("payouts", {"limit": "10"})
print("\n=== RECENT PAYOUTS (last 10) ===")
for p in payouts.get("data", []):
    print(f"  {p['id']} | ${p['amount']/100:,.2f} | Status: {p['status']} | Arrival: {p['arrival_date']} | {ts_to_date(p['created'])}")

# CUSTOMERS
customers = stripe_get("customers", {"limit": "20"})
print("\n=== RECENT CUSTOMERS (last 20) ===")
for c in customers.get("data", []):
    print(f"  {c['id']} | {c.get('email','N/A')} | {ts_to_date(c['created'])}")
