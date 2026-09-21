"""Lead Engine — autonomous drip state machine.

Each lead lives in leads.csv with a current stage and next_action_date.
Each run fires leads whose next_action_date has arrived, sends the due email
via SMTP (existing sender pattern), advances state, and logs to the ledger.

Only consented/warm leads are ever contacted (guardrail). Sending is a no-op
unless EMAIL_SENDING_ENABLED=1 AND the lead has consent=yes.
"""
import csv
import json
import os
import smtplib
from datetime import datetime, timezone, timedelta
from email.message import EmailMessage

import ledger

BASE = os.path.dirname(os.path.abspath(__file__))
LEADS_CSV = os.path.join(BASE, "leads.csv")
COLUMNS = ["email", "name", "company", "stage", "consent",
           "last_action", "next_action_date", "source", "notes"]

STAGES = ["identified", "contacted", "engaged", "converted", "won"]
BUMPS = {  # stage -> days to next action
    "identified": 0,     # send initial right away
    "contacted": 2,      # 48h follow-up
    "engaged": 3,        # qualification bump
    "converted": 0,
    "won": 0,
}


def _ensure_leads():
    os.makedirs(BASE, exist_ok=True)
    if not os.path.exists(LEADS_CSV):
        with open(LEADS_CSV, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(COLUMNS)


def _load_leads():
    _ensure_leads()
    rows = []
    with open(LEADS_CSV, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows


def _save_leads(rows):
    with open(LEADS_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)


def _smpt_config():
    path = os.environ.get("SMTP_ENV_PATH",
                          r"C:\Users\YAROS\.openclaw\credentials\email-smtp.env")
    cfg = {}
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            cfg[k.strip()] = v.strip().strip('"').strip("'")
    return cfg


def _send_email(to_email, subject, body, cfg):
    if not cfg.get("SMTP_HOST"):
        return False
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = cfg.get("SMTP_FROM", "YaRo Security")
    msg["To"] = to_email
    msg.set_content(body)
    with smtplib.SMTP(cfg["SMTP_HOST"], int(cfg.get("SMTP_PORT", 587)), timeout=30) as s:
        s.starttls()
        s.login(cfg.get("SMTP_USER", ""), cfg.get("SMTP_PASS", ""))
        s.send_message(msg)
    return True


def add_lead(email, name, company, source, consent="no", notes=""):
    """Add a lead (default consent=no until confirmed)."""
    rows = _load_leads()
    if any(r["email"] == email for r in rows):
        return False, "exists"
    rows.append({
        "email": email, "name": name, "company": company, "stage": "identified",
        "consent": consent, "last_action": "", "next_action_date": datetime.now(timezone.utc).isoformat(),
        "source": source, "notes": notes,
    })
    _save_leads(rows)
    return True, "added"


def run(email_enabled=False):
    """Fire all due leads once."""
    _ensure_leads()
    if not email_enabled:
        return {"status": "PAUSED", "reason": "EMAIL_SENDING_ENABLED not set. No emails sent."}
    cfg = _smpt_config()
    if not cfg.get("SMTP_HOST"):
        return {"status": "BLOCKED", "reason": "SMTP config missing at SMTP_ENV_PATH"}
    now = datetime.now(timezone.utc)
    rows = _load_leads()
    fired = []
    for r in rows:
        if r.get("consent") != "yes":
            continue
        try:
            due = datetime.fromisoformat(r["next_action_date"])
        except Exception:
            due = now
        if due > now:
            continue
        stage = r["stage"]
        if stage not in STAGES:
            continue
        body = (f"Hi {r['name'] or 'there'},\n\n"
                f"Following up on the AI compliance gap analysis for {r['company'] or 'your team'}.\n"
                "Quick question — is compliance/AI governance on your roadmap right now?\n\n"
                "If it helps, I can send the one-page scope. No pressure.\n\n— YaRo Security")
        try:
            _send_email(r["email"], f"Compliance gap analysis for {r['company'] or 'your team'}", body, cfg)
            r["last_action"] = now.isoformat()
            nxt = STAGES[min(STAGES.index(stage) + 1, len(STAGES) - 1)]
            r["stage"] = nxt
            r["next_action_date"] = (now + timedelta(days=BUMPS.get(stage, 2))).isoformat()
            fired.append(r["email"])
            ledger.log("lead_contacted", "lead_engine", detail=r["email"], lead_ref=r["email"])
        except Exception as e:
            r["notes"] = (r.get("notes") or "") + f" send_error={e}"
    _save_leads(rows)
    return {"status": "OK", "emails_sent": fired, "count": len(fired)}


if __name__ == "__main__":
    print(json.dumps(run(email_enabled=os.environ.get("EMAIL_SENDING_ENABLED") == "1"), indent=2))