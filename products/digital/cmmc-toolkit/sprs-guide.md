# SPRS Scoring Guide (Plain English)

The Supplier Performance Risk System (SPRS) is how the DoD scores a contractor's NIST 800-171 security posture **before** CMMC Level 2 assessment.

## The 110-point system
- Starts at 110. You LOSE points for each requirement NOT met.
- Missing control = -1 to -5 points depending on how important the control is.
- **Mandatory deducts (NIST 800-171 DoD Assessment Methodology):** a flat -1 point penalty (on top of any other loss) is taken for conditions including:
  - CUI physically/logically accessed without authorization (data loss give-back)
  - Not documenting a finding in the POAM by the end of the one-time assessment
  - Not implementing required basic safeguards
- Result reported out of 110.

## Worked example
- Fully meet 95 controls, partially meet 10, miss 5 entirely.
- The 5 missed are 3-point Access Control controls: -15.
- One triggers a mandatory data-loss give-back: -1.
- A missing POAM entry: -1.
- Raw = 110 - 15 - 1 - 1 = 93.

## How to improve
1. Fix the big-ticket families first: Access Control (3.1) and System & Comms Protection (3.13) carry the most points.
2. Nail point-of-entry items: firewall, VPN, MFA, encryption at rest/in transit.
3. Keep the POAM current — the -1 mandatory deducts are the cheapest to lose and easiest to recover.
4. Re-assess quarterly with this toolkit and track movement.

> Note: SPRS raw score differs from CMMC certification scoring; treat this as the DoD SPRS view commonly asked for before prime RFPs.
