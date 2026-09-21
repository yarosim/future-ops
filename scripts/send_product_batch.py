# send_product_batch.py — cold email batch #2: pitch digital products to segment-matched leads
import csv, os, time, smtplib, ssl
from email.message import EmailMessage

LEAD = r"C:\Users\YAROS\.openclaw\workspace\revenue_engine\leads.csv"
SMTP_USER = "pnsgloballlc@gmail.com"
SMTP_PASS = None
for line in open(r"C:\Users\YAROS\.openclaw\credentials\email-smtp.env", encoding="utf-8"):
    if line.startswith("SMTP_PASS="):
        SMTP_PASS = line.split("=", 1)[1].strip()
assert SMTP_PASS

def pitch(seg):
    if seg == "hipaa":
        return ("HIPAA Compliance Policy Pack", 79,
            "we just put out a HIPAA policy pack for small practices - 18 ready-to-customize templates, "
            "a 7-step risk-assessment worksheet, and an annual audit checklist. Way cheaper than hiring it out "
            "and it covers the #1 OCR finding (no documented risk analysis). $79, instant download.")
    if seg == "saas":
        return ("AI Agent Governance Starter Kit", 99,
            "if you're running AI agents or automations, this kit is timely: permission-matrix templates, a "
            "50-point agent audit checklist, an incident runbook, and monitoring scorecards. Most teams running "
            "agents have zero governance - this fixes that in an afternoon. $99, instant download.")
    return ("CMMC 2.0 Readiness Toolkit", 49,
        "we just put out a CMMC readiness toolkit: all 110 NIST 800-171 controls in plain English, a gap-tracker, "
        "and an SPRS scoring guide. Know exactly where you stand before a prime asks. $49, instant download.")

SIG = ("Yaro Security LLC - Durham, NC 27712 - pnsgloballlc@gmail.com\n"
       "https://yarosim.github.io/yarosecurity/downloads/\n"
       "If you'd rather not hear from us, reply \"unsubscribe\" and we'll stop.\n")

rows = list(csv.DictReader(open(LEAD, encoding="utf-8")))
cands = [r for r in rows if r.get("stage") == "identified" and r.get("consent") == "no"]
def seg(r):
    n=(r.get("notes","") or "").lower()
    return "hipaa" if any(k in n for k in ("hipaa","clinic","practice","health","aba","pediatric","therapy")) else ("saas" if "saas" in n else "cmmc")
# up to 6 per segment = 18
picked=[]
for s in ("cmmc","hipaa","saas"):
    picked += [r for r in cands if seg(r)==s][:6]
print("sending",len(picked))
ctx=ssl.create_default_context()
for r in picked:
    name, price, body = pitch(seg(r))
    first = (r.get("name") or "there").split()[0]
    msg = EmailMessage()
    msg["From"] = f"YaRo Security <{SMTP_USER}>"
    msg["To"] = r["email"].strip()
    msg["Subject"] = f"{r['company']} - {name} (${price}, instant download)"
    msg.set_content(f"Hi {first},\n\n{body}\n\nDownload page: https://yarosim.github.io/yarosecurity/downloads/\n\n{SIG}")
    try:
        with smtplib.SMTP("smtp.gmail.com",587,timeout=60) as s:
            s.starttls(context=ctx); s.login(SMTP_USER,SMTP_PASS); s.send_message(msg)
        print("sent",r["email"]); r["stage"]="contacted"; r["consent"]="cold_outreach_2026-09-21_product"; r["last_action"]="product_email_v1"
    except Exception as e:
        print("FAIL",r["email"],str(e)[:80])
    time.sleep(3)
with open(LEAD,"w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader()
    for rr in rows:
        for rr2 in picked:
            if rr.get("email")==rr2.get("email"):
                rr["stage"]=rr2["stage"]; rr["consent"]=rr2["consent"]; rr["last_action"]=rr2["last_action"]
        w.writerow(rr)