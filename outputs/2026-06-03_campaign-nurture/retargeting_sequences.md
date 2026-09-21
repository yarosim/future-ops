# Campaign Nurture — Retargeting Sequences
Run time: 2026-06-03 10:28 ET
Campaign: YaroSecurity CMMC / 48-hour AI compliance gap analysis

## Pixel / audience rules
Do not launch paid spend until tracking and consent are confirmed.

### Audiences
1. **Checklist visitors, no opt-in**
   - Rule: visited checklist landing page, did not submit form within 24h.
   - Offer: Prime Readiness Checklist.
2. **Checklist claimed, no audit click**
   - Rule: submitted lead magnet, no audit CTA click within 72h.
   - Offer: 5-workstream CMMC map.
3. **Audit page visitors, no purchase/booking**
   - Rule: visited audit checkout/booking page, no completion within 48h.
   - Offer: sample 48-hour audit output + objection handling.
4. **Idle nurture contacts**
   - Rule: in email sequence with no opens/clicks after 5 days.
   - Offer: problem-framed reminder, lower-pressure checklist CTA.
5. **Partner-fit contacts**
   - Rule: titles/firms suggesting MSP, cybersecurity consultancy, AI security founder, BD/referral partner.
   - Offer: partner one-pager.

---

## LinkedIn retargeting ad set
**Budget posture:** start tiny/test only; pause if no tracking or no checkout link.
**Frequency cap:** 2 impressions/day/person.
**Objective:** lead generation or website conversion, depending on tracking readiness.

### Ad 1 — Blank score
**Format:** static
**Primary text:**
If your current CMMC answer is “we think we are okay,” you may have a blank-score problem.

The Prime Readiness Checklist helps GovCon subcontractors find the first evidence gaps a prime is likely to notice.

**Headline:** Know what breaks first before your prime asks
**CTA:** Download
**Destination:** {{prime_readiness_checklist_link}}

### Ad 2 — Cost anchor
**Format:** single image or short video
**Primary text:**
Traditional assessments can run $5K–$15K.

A 48-hour AI compliance gap analysis gives you the first decision for $299:
- risk score
- gap map
- prioritized remediation plan
- plain-English walkthrough

**Headline:** $299 clarity before a $15K assessment
**CTA:** Get audit
**Destination:** {{audit_checkout_or_booking_link}}

### Ad 3 — Compression
**Format:** carousel
**Slides:**
1. CMMC feels impossible when it is uncompressed.
2. Stop holding 320 objectives in your head.
3. Start with access control.
4. Then logging + monitoring.
5. Then incident response.
6. Then supplier governance.
7. Then workforce training.
8. Want the map? Download it.

**Headline:** The 5-workstream CMMC map
**CTA:** Download
**Destination:** {{workstream_map_link}}

---

## Meta retargeting ad set
**Use only for opted-in / compliant custom audiences.**

### Ad 1 — Checklist reminder
**Primary text:**
Before a prime asks for proof, know what slows you down first.

Get the 5-minute Prime Readiness Checklist for CMMC/SPRS prep.

**Headline:** CMMC readiness check
**CTA:** Download

### Ad 2 — Sample output
**Primary text:**
Not sure what a 48-hour AI compliance gap analysis actually gives you?

See a sample output: risk score, gap map, remediation plan, and walkthrough notes.

**Headline:** See the audit sample
**CTA:** Learn More

---

## Email/SMS retargeting rules

### SMS nudge — engaged no booking
**Trigger:** clicked audit CTA, no booking/purchase after 48h, SMS consent present.

**Copy:**
YaroSecurity: Want me to hold a 48-hour CMMC gap analysis slot for you this week? Reply with a day/time window or use this link: {{audit_checkout_or_booking_link}}

### Email nudge — audit page visitor
**Subject:** Want the sample output first?

**Body:**
Hi {{first_name}},

Saw you were looking at the 48-hour gap analysis.

If you want to see what the deliverable looks like before deciding, use this sample output first:

{{sample_audit_output_link}}

The audit is designed to answer one question: what breaks first, and what should you fix first?

— Simon

---

## Suppression rules
Suppress all nurture/retargeting when:
- contact books audit or consult
- contact purchases audit
- contact unsubscribes
- contact is active in sales conversation
- email bounced
- company is disqualified / not a GovCon or partner fit

## Measurement
Track weekly:
- lead magnet visits → opt-ins
- opt-ins → Email 1 open/click
- Email 2 audit CTA clicks
- audit page visits → purchase/booking
- idle contacts recovered by bump
- partner replies
