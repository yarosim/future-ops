# Holding Pattern Output — CMMC Cohort (2026-04-27)

## Deliverables
- 3-email nurture drip (immediate, +2d, +5d) with subject lines, preview text, body copy, CTAs, and automation tags.
- Lead magnet draft: "Prime Readiness Checklist" (Google Doc-ready outline + talking points).
- Retargeting sequence matrix for newsletter subscribers (email, SMS, paid) with triggers + copy blocks.

## Implementation Notes
- Load all emails into marketing automation as campaign `hp_cmmc_apr27` with steps spaced exactly 0d/2d/5d from opt-in.
- Apply UTM `utm_source=campaign_engine&utm_medium=holding_pattern&utm_campaign=cmmc_apr27` to all clickable links.
- Checklist should be exported to Google Docs before publishing; placeholders for doc link and Calendly URL are flagged with `{{ }}` tokens.
- Retargeting audiences mapped to CRM tags: `cohort:cmmc_subs_warm`, `stage:hp_engaged`, `stage:hp_idle`.

## Files
- `email_sequence.md`
- `prime_readiness_checklist.md`
- `retargeting_sequences.md`
