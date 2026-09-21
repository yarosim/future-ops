# Data Backup & Contingency Plan — [PRACTICE NAME]

**Document Control**

| Field | Value |
|---|---|
| Policy ID | HPP-016 |
| Effective Date | [EFFECTIVE DATE] |
| Last Reviewed | [DATE] |
| Owner | [SECURITY OFFICER NAME], Security Officer |
| CFR Reference | 45 CFR §164.308(a)(7), §164.312(a)(2)(ii), §164.310(d)(4) |

## 1. Purpose

To establish a contingency plan ensuring the availability of ePHI and critical operations during emergencies (system outage, ransomware, fire, flood, power failure, vendor outage), per 45 CFR §164.308(a)(7).

## 2. Data Backup Plan (§164.308(a)(7)(ii)(A))

| Data | System | Backup Method | Frequency | Retention |
|---|---|---|---|---|
| EHR data | [SYSTEM] | [VENDOR-MANAGED CLOUD BACKUP] | [DAILY] | [30/90 DAYS] |
| Billing/financial | [SYSTEM] | [METHOD] | [DAILY] | [PERIOD] |
| Shared files | [SYSTEM] | [METHOD] | [DAILY] | [PERIOD] |

- Backups are **encrypted** (AES-256) whether in transit or at rest.
- At least one backup copy is kept **off-site or in a separate cloud region**.
- At least one copy is **immutable or offline** (ransomware protection).
- Backup restoration is **tested [QUARTERLY]**; results logged in [BACKUP TEST LOG] (a backup you haven't restored from is not a backup).

## 3. Disaster Recovery Plan (§164.308(a)(7)(ii)(B))

### 3.1 Recovery Objectives
- Recovery Time Objective (RTO): [HOURS] — how fast systems must be restored.
- Recovery Point Objective (RPO): [HOURS] — maximum tolerable data loss.

### 3.2 Recovery Steps (summary)
1. Declare disaster: [SECURITY OFFICER/OWNER] assesses and declares.
2. Notify: [IT VENDOR CONTACT, PHONE] — engage vendor support.
3. Restore: restore from last verified backup per vendor runbook.
4. Verify: confirm data integrity with [VALIDATION METHOD].
5. Resume: return to normal operations; document timeline.

### 3.3 If EHR Is Down (Downtime Procedures)
- Switch to paper intake and charting using [DOWNTIME FORMS LOCATION].
- Capture: patient name, DOB, reason for visit, vitals, assessment, orders.
- After restoration, back-enter all downtime records into the EHR within [24–48 HOURS]; document back-entry completion.

## 4. Emergency Mode Operation Plan (§164.308(a)(7)(ii)(E))

During emergencies, the Practice continues operations with modified procedures: [DESCRIBE, e.g., manual scheduling, paper sign-in, altered access controls reviewed post-event]. Changes to access during emergency mode are logged and reviewed within [3] business days of resolution.

## 5. Testing & Maintenance

- Tabletop exercise of this plan performed [ANNUALLY] with staff; lessons documented.
- Contact list (IT vendor, backup vendor, utilities) reviewed [SEMI-ANNUALLY].

## 6. Key Contacts

| Contact | Name | Phone |
|---|---|---|
| IT/Managed Services | [NAME] | [PHONE] |
| Backup vendor | [NAME] | [PHONE] |
| EHR support | [VENDOR] | [PHONE] |
| Practice Owner | [NAME] | [PHONE] |

## Sign-Off

| Role | Name | Signature | Date |
|---|---|---|---|
| Security Officer | [NAME] | | |
| Practice Owner | [NAME] | | |

---
*Not legal advice — counsel review required.*
