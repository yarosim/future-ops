# Incident Response Policy — [PRACTICE NAME]

**Document Control**

| Field | Value |
|---|---|
| Policy ID | HPP-009 |
| Effective Date | [EFFECTIVE DATE] |
| Last Reviewed | [DATE] |
| Owner | [SECURITY OFFICER NAME], Security Officer |
| CFR Reference | 45 CFR §164.308(a)(6), §164.410 |

## 1. Purpose

To define how [PRACTICE NAME] identifies, responds to, contains, and learns from security incidents involving PHI or ePHI, as required by 45 CFR §164.308(a)(6).

## 2. Definition of Security Incident

Any attempted or successful unauthorized access, use, disclosure, modification, interference with, or destruction of information in an information system — e.g., lost laptop, misdirected email, ransomware, unauthorized record snooping, phishing compromise (§164.304).

A **breach** is an impermissible use or disclosure of unsecured PHI that compromises its security or privacy, unless a risk-assessment exception applies (§164.402).

## 3. Incident Response Team

| Role | Person | Responsibility |
|---|---|---|
| Incident Commander | [SECURITY OFFICER] | Coordinates response, decisions |
| Privacy Officer | [NAME] | Breach determination, notifications |
| IT Lead | [NAME/IT VENDOR CONTACT] | Containment, forensics, restoration |
| Practice Owner | [NAME] | Business decisions, legal counsel engagement |

## 4. Response Phases

### 4.1 Detection & Reporting
Any workforce member who suspects an incident must report it **immediately** (same day) to the Privacy Officer or Security Officer via [PHONE/EMAIL/IN-PERSON]. No one is penalized for good-faith reporting.

### 4.2 Containment (target: within [24 HOURS])
- Isolate affected systems; disable compromised accounts.
- Change credentials; block malicious senders/IPs.
- Preserve evidence — do not wipe or "clean" affected devices before IT review.

### 4.3 Assessment
- Determine what PHI was involved, whose, and what was done with it.
- Apply the four-factor breach risk assessment (§164.402(2)): (1) nature and extent of PHI; (2) unauthorized person who used/received it; (3) whether PHI was actually acquired or viewed; (4) extent of mitigation.
- If encrypted per §164.402 guidance and the key was not compromised, the event is generally **not** a reportable breach — document this determination.
- Document the assessment in the Incident Log regardless of outcome.

### 4.4 Eradication & Recovery
- Remove the cause (malware, vulnerable account, process gap).
- Restore from backup per the Contingency Plan (HPP-016).
- Verify integrity before returning systems to service.

### 4.5 Notification (if breach confirmed)
- **Individuals**: without unreasonable delay, no later than 60 days from discovery (§164.404) — content per §164.404(c).
- **HHS**: immediately if 500+ individuals affected; otherwise within 60 days of year-end via the HHS breach portal (§164.408).
- **Media**: notice to prominent media outlets if 500+ residents of a state/jurisdiction affected (§164.406).
- **Business associates must notify the Practice within [60] days** of discovery (§164.410).

### 4.6 Post-Incident Review
Within [2 WEEKS] of resolution, the team completes a root-cause review and documents corrective actions (training, technical control, policy change). Lessons learned are folded into the next risk analysis.

## 5. Incident Log

All incidents are recorded in [INCIDENT LOG LOCATION] with: date discovered, date reported, description, PHI involved, assessment outcome, actions taken, and closing date. Retain [6] years.

## 6. Contact

- Security Officer: [NAME], [PHONE], [EMAIL]
- IT vendor: [VENDOR], [PHONE]
- Legal counsel: [COUNSEL], [PHONE]

## Sign-Off

| Role | Name | Signature | Date |
|---|---|---|---|
| Security Officer | [NAME] | | |
| Privacy Officer | [NAME] | | |

---
*Not legal advice — counsel review required.*
