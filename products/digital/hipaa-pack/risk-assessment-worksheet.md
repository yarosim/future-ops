# Simplified 7-Step HIPAA Security Risk Assessment Worksheet

**For small practices** — [PRACTICE NAME] | Completed by: [NAME] | Date: [DATE]

> 45 CFR §164.308(a)(1)(ii)(A) requires an "accurate and thorough" risk analysis. This worksheet walks you through it. Complete it annually and after any major system change. Keep the completed copy for at least 6 years.

---

## Step 1 — Inventory Your ePHI

List every place electronic patient information lives. Don't forget the "invisible" ones.

| # | System / Device / Location | Type (server, cloud, laptop, phone, USB, email, fax) | ePHI Stored? (Y/N) | Owner/Vendor | Encrypted (at rest / in transit / unknown) |
|---|---|---|---|---|---|
| 1 | [EHR system] | Cloud | | | |
| 2 | [Practice management/billing] | | | | |
| 3 | [Workstations] | | | | |
| 4 | [Laptops] | | | | |
| 5 | [Smartphones/tablets] | | | | |
| 6 | [Email] | | | | |
| 7 | [Fax] | | | | |
| 8 | [Backup service] | | | | |
| 9 | [Telehealth platform] | | | | |
| 10 | [USB drives/external media] | | | | |
| 11 | [Others] | | | | |

## Step 2 — Identify Threats

For each item above, note realistic threats: theft/loss, hacking/ransomware, unauthorized employee access, misdirected email/fax, power failure, fire/flood, vendor outage, improper disposal.

## Step 3 — Identify Vulnerabilities

For each item, note weaknesses: no encryption, weak/shared passwords, no MFA, outdated software, untrained staff, no backup testing, open Wi-Fi, unlocked screens, no disposal process.

## Step 4 — Rate Likelihood and Impact

For each threat/vulnerability pair, rate:

| Rating | Likelihood (will it happen?) | Impact (how bad if it does?) |
|---|---|---|
| High | Expected; happens regularly in practices like yours | Breach notification, patient harm, practice closure |
| Medium | Plausible | Regulatory scrutiny, remediation cost, reputation hit |
| Low | Unlikely given controls | Minor, contained incident |

## Step 5 — Calculate Risk

Risk = Likelihood × Impact. Use: High+High = Critical, High+Medium or Medium+High = High, Medium+Medium = Moderate, anything with Low = Low/Moderate.

| # | System | Threat / Vulnerability | Likelihood | Impact | Risk Level |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |

## Step 6 — Document Current Safeguards and Gaps

| Safeguard Category | What You Have | What's Missing |
|---|---|---|
| Encryption (at rest) | | |
| Encryption (in transit) | | |
| Unique user IDs + MFA | | |
| Automatic screen lock | | |
| Audit logging + review | | |
| Antivirus/patching | | |
| Backups (tested, offsite, immutable) | | |
| Signed BAAs for all vendors | | |
| Staff training (annual) | | |
| Device disposal process | | |
| Physical security (locks, privacy screens) | | |
| Incident response plan | | |

## Step 7 — Build the Remediation Plan

For every Moderate-or-higher risk, list a fix, owner, and deadline.

| # | Risk Being Addressed | Action | Owner | Due Date | Status |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Common quick wins for small practices:** enable full-disk encryption on every laptop; turn on MFA for EHR, email, and remote access; verify signed BAAs exist for every vendor touching PHI (including IT support and shredding companies); test a backup restore; enable EHR audit logs and review monthly.

## Sign-Off

| Role | Name | Signature | Date |
|---|---|---|---|
| Completed by | | | |
| Reviewed by (Security Officer) | | | |

*This worksheet is a self-assessment tool, not legal advice and not a substitute for a professional risk analysis where your risk profile warrants one.*
