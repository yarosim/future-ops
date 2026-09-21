# Executive Summary

**Target:** yahoo.com  
**Evidence cutoff:** 2026-08-05 20:13 UTC

## Overall conclusion

Yahoo presents substantial public evidence for privacy transparency, user controls, security ownership, and coordinated vulnerability disclosure. Particularly strong artifacts include a current privacy policy (updated March 2026), an RFC-style `security.txt` with reporting contacts and an expiry date, an official vulnerability-disclosure policy with researcher rules and safe-harbor language, a named security organization (the Paranoids), and a public commitment to biannual government-request transparency reporting.

Public evidence is materially thinner for formal enterprise cyber-risk governance, measurable incident-response/recovery performance, assurance reports/certifications, supply-chain oversight outcomes, and AI governance. These are **not publicly verifiable**, not demonstrated control failures.

## Public-evidence coverage score: **61/100**

This score measures public-evidence discoverability and coverage only. It is not a compliance score.

| Domain | Coverage | Summary |
|---|---:|---|
| NIST CSF Govern | 45% | Security ownership and policies visible; risk appetite, board oversight, metrics and assurance not publicly evidenced. |
| Identify | 40% | High-level assets/data uses described; inventories, dependency mapping and formal risk assessments not public. |
| Protect | 78% | TLS claims, account verification options, safeguards, training, privacy controls and vendor confidentiality statements. |
| Detect | 40% | Security team and testing/vulnerability research described; monitoring outcomes and detection metrics not public. |
| Respond | 72% | Mature external disclosure channels and policy; internal IR lifecycle, exercises and notification metrics not public. |
| Recover | 25% | Privacy policy references disaster-recovery backups; recovery plans, objectives and exercise evidence not public. |
| Privacy/transparency | 85% | Detailed policy, purposes, sharing, retention, rights/controls, transfers and contact mechanisms. |
| AI governance | 15% | General research/innovation and content analysis disclosed; no consolidated responsible-AI framework found. |
| Observable web hygiene | 75% | HTTPS reachable, `security.txt` and robots policy present; full header/TLS posture could not be established due to rate limiting. |

## Highest-confidence evidence found

1. `/.well-known/security.txt` returned HTTP 200 and named email/Intigriti contacts, acknowledgments, policy, hiring page, and expiry `2026-12-31`.
2. Yahoo’s vulnerability policy documents reporting routes, scoped researcher conduct, confidentiality, safe harbor conditioned on policy compliance, and a 90-day coordinated-disclosure approach for third parties.
3. Yahoo’s March 2026 privacy policy describes collection, use, sharing, data retention, safeguards, rights/controls, international transfer mechanisms and material-change notice.
4. Yahoo identifies the Paranoids as its information-security team and describes infrastructure security, vulnerability research, open source and bug bounty work.
5. The privacy security page publicly states TLS use for certain information, second sign-in verification, security education/training and continuing enhancement.

## Priority potential gaps in public evidence

- **AI governance:** no public consolidated policy covering AI accountability, inventory, impact assessment, model/data governance, testing, monitoring, incident handling, user notice, or appeals was found.
- **Cyber governance:** no publicly discoverable CSF profile, control objectives, executive/board oversight model, risk appetite, security KPIs or independent assurance statement was established.
- **Incident and recovery evidence:** external reporting is strong, but lifecycle procedures, exercise cadence, post-incident learning, recovery objectives and resilience testing are not publicly verifiable.
- **Web-security observability:** a direct HEAD request received HTTP 429, preventing a representative assessment of headers. The response did include `X-Content-Type-Options: nosniff` and `Referrer-Policy: no-referrer-when-downgrade`; absence of other headers on that rate-limit response must not be generalized.

## Recommended next actions

1. Publish a concise trust-center index connecting security, privacy, vulnerability disclosure, transparency, resilience and AI-governance artifacts.
2. Publish a responsible-AI statement aligned to NIST AI RMF (Govern, Map, Measure, Manage), including accountable ownership and lifecycle controls.
3. Add a public CSF 2.0-aligned control narrative and evidence-update cadence, without disclosing sensitive implementation detail.
4. Publish bounded incident-response/resilience evidence: governance, exercise cadence, notification principles, recovery validation and aggregate metrics.
5. Maintain automated checks for `security.txt` expiry, redirects, policy-link integrity and representative security headers.
