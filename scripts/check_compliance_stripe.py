import os, sys, json, time, base64, urllib.parse, urllib.request
from datetime import datetime, timezone

ENV_PATH = r"C:\Users\YAROS\.openclaw\credentials\stripe.env"
PRICE_IDS = {
    "AI Compliance Gap Analysis ($299)": "price_1TQG5eEJtdifHfsdKpZBUHps",
    "Managed Compliance ($997/mo)": "price_1TQG5gEJtdifHfsd7OAiA42l",
}
LINKS = {
    "AI Compliance Gap Analysis ($299)": "https://buy.stripe.com/eVqeVdd6A40Y2Nk0UY2Ji16",
    "Managed Compliance ($997/mo)": "https://buy.stripe.com/28E5kDgiM40YfA61Z2",
}


def load_env(path):
    if not os.path.exists(path):
        raise SystemExit(f"missing env file: {path}")
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            k,v=line.split('=',1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

load_env(ENV_PATH)
KEY = os.environ.get('STRIPE_API_KEY')
if not KEY:
    raise SystemExit('STRIPE_API_KEY not set')

BASE='https://api.stripe.com/v1'

def request(path, params=None):
    url = BASE + path
    if params:
        # params supports list values
        qs = urllib.parse.urlencode(params, doseq=True)
        url += '?' + qs
    token = base64.b64encode((KEY + ':').encode()).decode()
    req = urllib.request.Request(url, headers={'Authorization': 'Basic '+token, 'Stripe-Version':'2025-02-24.acacia'})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def list_all(path, params):
    out=[]
    params=dict(params)
    params.setdefault('limit', 100)
    while True:
        data=request(path, params)
        out.extend(data.get('data',[]))
        if not data.get('has_more') or not data.get('data'):
            break
        params['starting_after']=data['data'][-1]['id']
    return out


def get_line_items(session_id):
    return list_all(f'/checkout/sessions/{session_id}/line_items', {'limit':100})


def price_ids_from_line_items(items):
    ids=[]
    for item in items:
        price=(item.get('price') or {})
        if price.get('id'):
            ids.append(price['id'])
    return ids


def http_status(url):
    try:
        req=urllib.request.Request(url, method='HEAD', headers={'User-Agent':'OpenClaw revenue tracker'})
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status
    except Exception:
        try:
            req=urllib.request.Request(url, headers={'User-Agent':'OpenClaw revenue tracker'})
            with urllib.request.urlopen(req, timeout=20) as resp:
                return resp.status
        except Exception as e:
            return f"ERR:{type(e).__name__}"

now=int(time.time())
window_24h=now-24*3600
# prior cron entry was ~04:06 ET / 08:06Z in daily memory
since_prior=int(datetime(2026,6,4,8,6,9,tzinfo=timezone.utc).timestamp())

sessions=list_all('/checkout/sessions', {
    'created[gte]': window_24h,
    'expand[]': ['data.payment_intent','data.customer','data.subscription'],
})
paid_sessions=[]
matched_sessions=[]
matched_by_offer={name: [] for name in PRICE_IDS}
customer_ids=set()
payment_intent_ids=set()

for s in sessions:
    if s.get('payment_status') == 'paid' or s.get('status') == 'complete':
        paid_sessions.append(s)
    items=get_line_items(s['id'])
    prices=price_ids_from_line_items(items)
    hit_names=[name for name,pid in PRICE_IDS.items() if pid in prices]
    if hit_names and (s.get('payment_status') == 'paid' or s.get('status') == 'complete'):
        matched_sessions.append(s)
        for name in hit_names:
            matched_by_offer[name].append(s)
        cust=s.get('customer')
        if isinstance(cust, dict): cust=cust.get('id')
        if cust: customer_ids.add(cust)
        pi=s.get('payment_intent')
        if isinstance(pi, dict): pi=pi.get('id')
        if pi: payment_intent_ids.add(pi)

# Successful PIs account-wide and those tied to matched sessions. Also inspect invoices for recurring subscription renewals.
pis=list_all('/payment_intents', {'created[gte]': window_24h})
succeeded_pis=[p for p in pis if p.get('status')=='succeeded']
matched_pi_ids=set(payment_intent_ids)
matched_invoice_pis=[]
for p in succeeded_pis:
    inv=p.get('invoice')
    if inv:
        try:
            invoice=request(f'/invoices/{inv}', {'expand[]':['lines.data.price','customer']})
            line_prices=[]
            for line in (invoice.get('lines') or {}).get('data',[]):
                price=(line.get('price') or {})
                if price.get('id'): line_prices.append(price['id'])
            if any(pid in line_prices for pid in PRICE_IDS.values()):
                matched_pi_ids.add(p['id'])
                matched_invoice_pis.append(p)
                cust=invoice.get('customer')
                if isinstance(cust, dict): cust=cust.get('id')
                if cust: customer_ids.add(cust)
        except Exception:
            pass

charges=list_all('/charges', {'created[gte]': window_24h})
paid_charges=[c for c in charges if c.get('paid') and not c.get('refunded')]
matched_charges=[c for c in paid_charges if c.get('payment_intent') in matched_pi_ids]

customers=list_all('/customers', {'created[gte]': window_24h})
new_customers=len(customers)
new_offer_customers=[c for c in customers if c.get('id') in customer_ids]

payouts=list_all('/payouts', {'created[gte]': window_24h})
# Balance transactions can show source payout/stripe_fx_fee etc; payout list is the deposit/change surface requested.

fmt=lambda ts: datetime.fromtimestamp(ts, tz=timezone.utc).isoformat().replace('+00:00','Z')

def dollars(cents, currency='usd'):
    if cents is None: cents=0
    return f"{(cents/100):.2f} {currency.upper()}"

offer_rows=[]
for name, arr in matched_by_offer.items():
    gross=sum((s.get('amount_total') or 0) for s in arr)
    currency=(arr[0].get('currency') if arr else 'usd') or 'usd'
    offer_rows.append({'offer': name, 'paid_checkout_sessions': len(arr), 'gross': dollars(gross, currency), 'since_prior': sum(1 for s in arr if s.get('created',0)>=since_prior)})

result={
    'window_24h': {'from': fmt(window_24h), 'to': fmt(now)},
    'incremental_since_prior': fmt(since_prior),
    'offers': offer_rows,
    'paid_checkout_sessions_account': len(paid_sessions),
    'paid_checkout_sessions_offer': len(matched_sessions),
    'successful_payment_intents_account': len(succeeded_pis),
    'successful_payment_intents_offer': len(matched_pi_ids),
    'paid_non_refunded_charges_account': len(paid_charges),
    'paid_non_refunded_charges_offer': len(matched_charges),
    'new_customers_account': new_customers,
    'new_customers_offer': len(new_offer_customers),
    'payouts_count': len(payouts),
    'payouts_total': dollars(sum(p.get('amount') or 0 for p in payouts), (payouts[0].get('currency') if payouts else 'usd')),
    'payout_ids': [p.get('id') for p in payouts],
    'link_status': {name: http_status(url) for name,url in LINKS.items()},
    'matched_session_ids': [s.get('id') for s in matched_sessions],
    'matched_payment_intent_ids': sorted(matched_pi_ids),
}
print(json.dumps(result, indent=2))
