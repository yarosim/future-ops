# Device & Media Control Policy — [PRACTICE NAME]

**Document Control**

| Field | Value |
|---|---|
| Policy ID | HPP-012 |
| Effective Date | [EFFECTIVE DATE] |
| Last Reviewed | [DATE] |
| Owner | [SECURITY OFFICER NAME], Security Officer |
| CFR Reference | 45 CFR §164.310(d)(1) |

## 1. Purpose

To control the receipt, movement, use, and disposal of hardware and electronic media containing ePHI at [PRACTICE NAME], per 45 CFR §164.310(d)(1).

## 2. Inventory & Accountability

- The Security Officer maintains an asset inventory of all devices and media that store or access ePHI (make, model, serial number, assigned user, encryption status, location).
- The inventory is reconciled [SEMI-ANNUALLY].
- Movement of devices/media off-site requires checkout in [LOG LOCATION] (§164.310(d)(2)(i) — accountability).

## 3. Mobile Devices

- Laptops, tablets, and phones that access ePHI must have full-disk encryption enabled ([AES-256]) and device passcodes.
- Remote wipe capability ([MDM SOLUTION]) is configured where possible.
- ePHI may not be stored on personal devices unless enrolled in the Practice's [MDM/BYOD PROGRAM].
- Devices must never be left unattended in vehicles or public spaces.

## 4. Removable Media

- USB drives used for ePHI must be [PRACTICE-ISSUED AND ENCRYPTED].
- Personal USB drives are prohibited on practice computers.
- USB ports on workstations may be [RESTRICTED VIA POLICY/GPO] where feasible.

## 5. Disposal & Reuse (§164.310(d)(2)(ii)–(iii))

Before any device or media is discarded, reused, returned, or donated:

- **Destruction**: shredding, degaussing, or secure wiping (NIST SP 800-88 media sanitization) such that PHI is unreadable and unreconstructable.
- **Reuse**: sanitized per NIST 800-88; encryption keys wiped.
- Paper records: cross-cut shredding or secure destruction vendor with certificate of destruction.
- Disposal is documented in the Media Disposal Log: date, item, serial number, method, performed by, witness.

## 6. Lost or Stolen Devices

Report immediately to the Security Officer ([PHONE]). Follow the Incident Response Policy (HPP-009). Note: encrypted devices lost with keys uncompromised generally avoid breach-notification status — which is why encryption is mandatory.

## Sign-Off

| Role | Name | Signature | Date |
|---|---|---|---|
| Security Officer | [NAME] | | |
| Practice Owner | [NAME] | | |

---
*Not legal advice — counsel review required.*
