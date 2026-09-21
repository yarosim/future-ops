# Audit Controls Policy — [PRACTICE NAME]

**Document Control**

| Field | Value |
|---|---|
| Policy ID | HPP-015 |
| Effective Date | [EFFECTIVE DATE] |
| Last Reviewed | [DATE] |
| Owner | [SECURITY OFFICER NAME], Security Officer |
| CFR Reference | 45 CFR §164.312(b), §164.308(a)(1)(ii)(D) |

## 1. Purpose

To implement hardware, software, and/or procedural mechanisms that record and examine activity in systems containing ePHI, per 45 CFR §164.312(b).

## 2. Systems with Audit Logging

| System | Log Type | Retention |
|---|---|---|
| [EHR SYSTEM] | Access, view, edit, print, export | [6 YEARS] |
| [Practice management/billing] | Login, record access | [6 YEARS] |
| [Email platform] | Login, forwarding rules | [1 YEAR] |
| [Firewall/network] | Connection attempts, blocks | [1 YEAR] |
| [Workstations] | Login events, USB activity | [6 MONTHS] |

## 3. What Is Logged (Minimum)

- Date, time, and user identity for each access to systems containing ePHI.
- Records accessed or modified.
- Failed login attempts.
- Administrative actions (account creation, permission changes).
- Data exports and printing of records where technically available.

## 4. Log Review Procedure

- The Security Officer (or IT vendor) reviews audit logs on a [MONTHLY] schedule using [REVIEW METHOD: EHR audit report / SIEM tool].
- Review targets:
  - Access by terminated or inactive users
  - After-hours or unusual-volume access
  - Records of coworkers, VIPs, or family members (snooping)
  - Repeated failed logins
  - Excessive exports or printing
- Findings are documented in the [AUDIT REVIEW LOG] with date, reviewer, anomalies, and disposition.

## 5. Follow-Up

Anomalies trigger investigation per the Incident Response Policy (HPP-009). Confirmed violations are handled under the Sanctions Policy (HPP-007).

## 6. Integrity of Logs (§164.312(c)(1))

Logs are retained per the table above and protected from modification by users; only [SECURITY OFFICER/IT] has log administration rights.

## Sign-Off

| Role | Name | Signature | Date |
|---|---|---|---|
| Security Officer | [NAME] | | |
| Practice Owner | [NAME] | | |

---
*Not legal advice — counsel review required.*
