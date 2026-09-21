import os
import stripe

api_key = os.environ.get('STRIPE_SECRET_KEY')
if not api_key:
    # check .env
    if os.path.exists('.env'):
        with open('.env', 'r') as f:
            for line in f:
                if line.startswith('STRIPE_SECRET_KEY='):
                    api_key = line.split('=', 1)[1].strip().strip('"\'')

if api_key:
    stripe.api_key = api_key
    try:
        sessions = stripe.checkout.Session.list(limit=10)
        print(f"Checkout sessions: {len(sessions.data)}")
        for s in sessions.data:
            print(f"- ID: {s.id} | Status: {s.status} | Payment: {s.payment_status} | Amount: {s.amount_total}")
        
        balance = stripe.Balance.retrieve()
        print("Balance:", balance)
    except Exception as e:
        print("Error:", e)
else:
    print("No STRIPE_SECRET_KEY found")
