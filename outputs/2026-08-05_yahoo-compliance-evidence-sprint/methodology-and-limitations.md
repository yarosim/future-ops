# Methodology and Limitations

## Objective

Assess the availability and quality of **public evidence**, not Yahoo’s compliance or internal control effectiveness. The practical mapping uses NIST CSF 2.0, privacy/transparency themes, vulnerability/incident disclosure, NIST AI RMF concepts and narrowly observable web hygiene.

## Procedure

Performed 2026-08-05 between 20:11 and 20:13 UTC:

1. Searched the public web for official Yahoo privacy, security, disclosure, transparency, governance and AI materials.
2. Retrieved official pages using ordinary HTTPS GET requests.
3. Retrieved `https://www.yahoo.com/robots.txt` and `https://www.yahoo.com/.well-known/security.txt`.
4. Sent one ordinary HEAD request to `https://www.yahoo.com/` to observe the returned status and headers.
5. Consulted official NIST CSF 2.0 and AI RMF pages as authoritative framework references.
6. Classified each result as Evidence Found, Not Publicly Verifiable, Potential Gap, or Recommendation, with confidence.

## Scoring method

The 0–100 score estimates public-evidence coverage across nine domains: CSF Govern, Identify, Protect, Detect, Respond, Recover, privacy/transparency, AI governance, and observable web hygiene. Considerations were artifact existence, specificity, currency, official provenance, linkage and coverage. The rounded overall score is **61/100**.

The score does **not** measure compliance, maturity, security effectiveness, legal sufficiency, or residual risk. Lack of public evidence is not evidence of absence.

## Hard boundaries observed

- No ports or services scanned.
- No crawling beyond a small number of ordinary public GET/HEAD requests.
- No vulnerability probes, payloads, fuzzing or bypass attempts.
- No accounts created, authenticated, enumerated or tested.
- No credentials, cookies or nonpublic data used.
- No security reports submitted and no contact made with Yahoo.
- No claims about internal systems were inferred from marketing/legal statements.

## Limitations

- Point-in-time evidence can change after the cutoff.
- Search indexing and geo/localization may hide or alter pages.
- Some Yahoo pages are dynamic; readable extraction may omit navigation or interactive controls.
- A HEAD request to the root returned `429 Too Many Requests`, so it is not representative evidence of standard application responses. Header observations apply only to that response.
- No certificate-chain, protocol/cipher, DNSSEC, CAA, CT-log or email-authentication audit was performed; doing so safely was optional but not necessary for this sprint.
- `robots.txt` is a crawler preference mechanism, not an access-control or AI-governance control. Its explicit restrictions on named AI crawlers are evidence of stated crawling preferences only.
- Public privacy/security statements are management assertions. No SOC report, ISO certificate, audit report, regulator determination or technical validation was reviewed.
- Yahoo Japan/LY Corporation materials were excluded from conclusions about Yahoo Inc. unless clearly applicable.
- The sprint does not offer legal advice or determine obligations in any jurisdiction.

## Confidence scale

- **High:** direct, current, official source or directly observed endpoint.
- **Medium:** official source but high-level, dated, incomplete, or requiring interpretation.
- **Low:** search-only indication, ambiguous scope, or inability to reproduce directly.
