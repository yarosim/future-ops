# send_cold_batch.py — first CAN-SPAM compliant cold email batch (10 CMMC leads)
# Sender: pnsgloballlc@gmail.com (YaRo Security). Opt-out: reply "unsubscribe".
import csv, smtplib, ssl, os, sys, time
from email.message import EmailMessage

CSV = r"C:\Users\YAROS\.openclaw\workspace\revenue_engine\leads.csv"
SENT_LOG = r"C:\Users\YAROS\.openclaw\workspace\revenue_engine\sent_log.csv"
SMTP_USER = "pnsgloballlc@gmail.com"
SMTP_PASS = os.environ.get("SMTP_PASS")
if not SMTP_PASS:
    for line in open(r"C:\Users\YAROS\.openclaw\credentials\email-smtp.env", encoding="utf-8"):
        if line.startswith("SMTP_PASS="):
            SMTP_PASS = line.split("=", 1)[1].strip()
assert SMTP_PASS, "no SMTP_PASS"

SIGNATURE = (
    "Yaro Security LLC\n"
    "Durham, NC 27712\n"
    "pnsgloballlc@gmail.com\n"
    "https://yarosim.github.io/yarosecurity/\n"
)
FOOTER = "\nIf you'd rather not hear from us, just reply \"unsubscribe\" and we won't email again.\n"

def body(company, contact_first):
    first = (contact_first or "there").split()[0]
    return (
        f"Hi {first},\n\n"
        f"Quick flag on {company}'s CMMC exposure: starting now, more DoW contracts require "
        f"CMMC Level 2 (NIST 800-171) proof, and primes are quietly cutting suppliers who can't show it.\n\n"
        f"Most firms don't know where they stand. A traditional gap assessment runs $5,000-$15,000 "
        f"and takes weeks. We run the same scope with AI in 48 hours for a flat $299: risk score, every "
        f"gap mapped to NIST 800-171, and a prioritized fix list.\n\n"
        f"Worth knowing where {company} stands before your next prime asks?\n\n"
        f"- Future (autonomous ops), YaRo Security\n{SIGNATURE}{FOOTER}"
    )

rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
cands = [r for r in rows if r.get("stage") == "identified" and r.get("consent") == "no"]
# prioritize defense/CMMC segment via notes keywords
cands.sort(key=lambda r: 0 if any(k in (r.get("notes","").lower()) for k in ("cmmc","defense","dib","rpo")) else 1)
batch = cands[:10]
print(f"sending {len(batch)} emails")

ctx = ssl.create_default_context()
results = []
for r in batch:
    msg = EmailMessage()
    msg["From"] = f"YaRo Security <{SMTP_USER}>"
    msg["To"] = r["email"].strip()
    msg["Subject"] = f"{r['company']} - do you know your CMMC/NIST 800-171 gaps?"
    msg.set_content(body(r["company"], r.get("name","")))
    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=60) as s:
            s.starttls(context=ctx)
            s.login(SMTP_USER, SMTP_PASS)
            s.send_message(msg)
        results.append((r["email"], "sent"))
        r["stage"] = "contacted"
        r["consent"] = "cold_outreach_2026-09-21"
        r["last_action"] = "cold_email_v1"
    except Exception as e:
        results.append((r["email"], f"FAIL {e}"))
    time.sleep(3)

# update CSV stage for sent rows
for r in rows:
    for email, status in results:
        if r.get("email") == email and status == "sent":
            r["stage"] = "contacted"
with open(CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader(); w.writerows(rows)

with open(SENT_LOG, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    if f.tell() == 0:
        w.writerow(["date", "email", "status", "template"])
    for email, status in results:
        w.writerow(["2026-09-21", email, status, "cmmc_v1"])
for email, status in results:
    print(email, "->", status)
