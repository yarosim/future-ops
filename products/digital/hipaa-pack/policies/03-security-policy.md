# Security Policy — [PRACTICE NAME]

**Document Control**

| Field | Value |
|---|---|
| Policy ID | HPP-003 |
| Effective Date | [EFFECTIVE DATE] |
| Last Reviewed | [DATE] |
| Owner | [SECURITY OFFICER NAME], Security Officer |
| CFR Reference | 45 CFR §164.306 (Security Rule, general requirements) |

## 1. Purpose

This policy establishes the administrative, physical, and technical safeguards [PRACTICE NAME] uses to protect the confidentiality, integrity, and availability of electronic protected health information (ePHI), as required by the HIPAA Security Rule (45 CFR §164.302–§164.318).

## 2. Scope

Applies to all ePHI created, received, maintained, or transmitted by the Practice, in any system or device — including servers, workstations, laptops, tablets, phones, USB drives, cloud services, and email.

## 3. Security Officer

The Security Officer for the Practice is [SECURITY OFFICER NAME]. The Security Officer is responsible for developing and implementing security policies, conducting risk analyses, overseeing workforce training, and managing security incidents.

## 4. Administrative Safeguards (§164.308)

| Safeguard | Implementation |
|---|---|
| Security management process | Risk analysis (HPP-011) performed [ANNUALLY] and after major system changes |
| Workforce security | Role-based access; clearance and termination procedures (HPP-005) |
| Information access management | Minimum necessary access; unique user IDs |
| Security awareness & training | At hire and [ANNUALLY] (HPP-006) |
| Security incident procedures | Incident Response Policy (HPP-009) |
| Contingency plan | Data Backup & Contingency Plan (HPP-016) |
| Evaluation | Periodic technical and nontechnical evaluation of security practices |
| Business associate contracts | BAA required before any ePHI is shared (HPP-008) |

## 5. Physical Safeguards (§164.310)

- Facility access controls (HPP-013)
- Workstation use and security (HPP-014)
- Device and media controls (HPP-012)

## 6. Technical Safeguards (§164.312)

| Safeguard | Implementation at [PRACTICE NAME] |
|---|---|
| Access control | Unique user IDs, [automatic logoff after X minutes], encryption |
| Audit controls | Audit logging on EHR and network systems (HPP-015) |
| Integrity | [MECHANISM, e.g., checksums/audit trails] to guard against improper alteration |
| Person or entity authentication | Strong passwords + [MFA REQUIRED? YES/NO] |
| Transmission security | Encryption of ePHI in transit (TLS 1.2+); encrypted email (HPP-017) |

## 7. Encryption Standards

- At rest: ePHI is encrypted with AES-256 or equivalent on all [DEVICES/SYSTEMS].
- In transit: TLS 1.2 or higher for all connections carrying ePHI.
- Full-disk encryption is enabled on all laptops and mobile devices that store or access ePHI.

## 8. Password & Authentication Standards

- Minimum [12] characters, no reuse of last [5] passwords.
- No shared accounts. All users have unique credentials.
- [MFA is required on: EHR, email, remote access, cloud services.]

## 9. Remote Work & Mobile Devices

Access to ePHI from outside the Practice requires:

- VPN or approved secure connection
- Practice-owned or [BYOD-enrolled] devices meeting encryption standards
- Prohibition on storing ePHI on personal cloud storage (personal Dropbox/Google Drive accounts)

## 10. Vendor and Cloud Services

No ePHI may be stored or transmitted through any software or vendor without a signed Business Associate Agreement and Security Officer approval. Approved vendors are listed in [VENDOR LIST LOCATION].

## 11. Review & Updates

This policy is reviewed [ANNUALLY] and after any material change to systems, workforce, or regulation.

## Sign-Off

| Role | Name | Signature | Date |
|---|---|---|---|
| Security Officer | [NAME] | | |
| Practice Owner | [NAME] | | |

---
*Not legal advice — counsel review required.*
