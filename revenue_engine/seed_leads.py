"""Seed revenue_engine/leads.csv from the named leads in YaroSecurity_Lead_Tracker.xlsx.

Consent defaults to 'no' (safe). Only leads with a verified email are drip-eligible.
Email-less leads are seeded so their missing-email blocker is visible, but they won't
be contacted until consent=yes AND an email exists.
"""
import lead_engine

LEADS = [
    # (name, company, email, source, notes)
    ("Scott McKittrick", "GEI Consultants, Inc.", "s.mckittrick@geiconsultants.com",
     "LinkedIn Tracker", "IT & Cybersecurity Leader; score 8; AI Security Posture Sprint; 2nd conn LinkedIn; CISSP/ITIL4"),
    ("Andrew Bagrin", "Cytracom/OmniNet", "",
     "LinkedIn Tracker", "CEO/Security Exec; score 9; NEEDS EMAIL; Charlotte NC; 2nd conn"),
    ("Justin Hill", "Strix IT", "",
     "LinkedIn Tracker", "BD Mgr Cybersecurity/AI; score 7; NEEDS EMAIL; potential referral partner; Birmingham AL"),
    ("Edward L.", "AIDEFEND", "",
     "LinkedIn Tracker", "AI Security Founder; score 6; NEEDS EMAIL; partnership/referral; RSA speaker"),
]

for name, company, email, source, notes in LEADS:
    ok, msg = lead_engine.add_lead(email=email or f"pending:{name.lower().replace(' ', '.')}@find",
                                   name=name, company=company,
                                   source=source, consent="no", notes=notes)
    print(f"{ok} | {name} | {company} | email={'YES' if email else 'MISSING'} | {msg}")