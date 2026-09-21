# Campaign Nurture — Newsletter Drip
Run time: 2026-06-03 10:28 ET
Campaign: YaroSecurity 48-hour AI compliance gap analysis / CMMC readiness
Primary CTA placeholder: `https://yaro-security.com/ai-audit?utm_source=newsletter&utm_medium=nurture&utm_campaign=cmmc_jun03`

## Operating note
No external emails were sent. This run staged send-ready copy and automation rules because no email service / opt-in audience export is configured in the workspace.

## Segment assumptions
- `new_lead`: leads from tracker with status `New - Contacted`, `New - Research`, or `Partnership Prospect`.
- `opened_or_clicked`: contacts who open/click Email 1.
- `engaged_no_booking`: clicked but no consult/audit purchase within 48 hours.
- `idle`: no open/click after 5 days.
- `partner_fit`: AI/security founders, BDs, MSPs, referral partners.

---

## Email 1 — The quiet risk in a blank compliance profile
**Timing:** Immediately after opt-in or manual lead qualification  
**Audience:** `new_lead`  
**Subject options:**
1. Your prime will not explain this scorecard
2. The quiet risk in a blank compliance profile
3. Before CMMC becomes urgent, check this

**Preview:** A 5-minute way to see whether your readiness story holds up.

**Body:**
Hi {{first_name}},

Most subcontractors do not lose momentum because every control is broken.

They lose momentum because they cannot answer the first questions fast enough:

- What is your current SPRS score?
- When was it last updated?
- Which 3 controls would break first if a prime asked this week?

That is the blank-score problem. It looks harmless until an RFP, option-year review, or prime request turns it into a scramble.

We made a short Prime Readiness Checklist that compresses the first pass into plain English.

**Download it here:** {{prime_readiness_checklist_link}}

Use it to pressure-test your current story before someone else does.

If you want a second set of eyes, reply **score** with what you know about your current status. I’ll point you to the likely drift area.

— Simon @ YaroSecurity

**CTA:** Download the Prime Readiness Checklist  
**Tags:** add `stage:nurture_started`; if click, add `stage:lead_magnet_claimed`; if reply contains `score`, add `intent:score_review`.

---

## Email 2 — $299 is cheap. Guessing is expensive.
**Timing:** +2 days after Email 1  
**Audience:** all except `intent:score_review` and booked contacts  
**Subject options:**
1. $299 is cheap. Guessing is expensive.
2. The real cost of waiting on CMMC
3. A faster way to decide what to fix first

**Preview:** The entry audit is meant to answer one question: what breaks first?

**Body:**
Hey {{first_name}},

Traditional compliance work often starts at $5K–$15K.

That can make teams delay the first step, even when they know CMMC readiness is going to matter.

The problem is that waiting does not reduce risk. It just keeps the risk invisible.

Our 48-hour AI compliance gap analysis is built as the entry point before the giant consulting spend.

You get:

- a clear risk score
- every major gap mapped in plain English
- a prioritized remediation plan
- a walkthrough so the output is usable, not shelfware

The goal is not to scare you into a huge project.

The goal is to tell you what to fix first.

**Book the 48-hour audit:** {{audit_checkout_or_booking_link}}

— Simon

**CTA:** Book the 48-hour audit  
**Tags:** if click, add `intent:audit_interest`; start 48h booking timer.

---

## Email 3 — Stop holding 320 objectives in your head
**Timing:** +5 days after Email 1  
**Audience:** non-buyers and non-booked contacts  
**Subject options:**
1. Stop holding 320 objectives in your head
2. The 5-workstream CMMC map
3. CMMC feels impossible when it is uncompressed

**Preview:** Access, logging, incident response, suppliers, training. That is the first map.

**Body:**
{{first_name}},

CMMC feels impossible when you try to hold 320 objectives in your head at once.

We do not start there.

We compress the first pass into 5 workstreams:

1. Access control
2. Logging + monitoring
3. Incident response
4. Supplier governance
5. Workforce training

That gives you sequence:

- what evidence exists now
- what is missing
- who owns it
- what can be fixed in the next 14 days
- what actually needs deeper support

That is the point of the 48-hour audit: clarity before complexity.

If you want the 5-workstream breakdown, grab it here:

**Get the workstream map:** {{workstream_map_link}}

And if you want us to score your current position, the audit is here:

**Start the 48-hour gap analysis:** {{audit_checkout_or_booking_link}}

— YaroSecurity Field Notes

**CTA:** Get the workstream map / Start the audit  
**Tags:** add `stage:workstream_educated`; if click audit, add `intent:audit_interest`.

---

## Email 4 — Idle bump: still want the checklist?
**Timing:** Day 7 if no open/click  
**Audience:** `idle`  
**Subject:** Still need that SPRS sanity check?

**Preview:** Resending the checklist so it is not buried.

**Body:**
Hi {{first_name}},

Resending this in case it got buried.

If your current CMMC answer is “we think we are fine,” the checklist is a quick way to find the weak spots before a prime asks.

**Checklist:** {{prime_readiness_checklist_link}}

The useful question is simple:

> If someone asked for your SPRS score and evidence packet this week, what would slow you down first?

Reply **score** if you want a quick sanity check.

— Simon

**CTA:** Open the checklist  
**Tags:** keep in `stage:idle`; add to retargeting audience after send.

---

## Email 5 — Partner-fit variation
**Timing:** Manual or automated branch for `partner_fit` contacts  
**Audience:** referral partners, MSPs, AI/security founders, business development leads  
**Subject options:**
1. Quick partner angle for CMMC leads
2. Referral fit: 48-hour CMMC gap analysis
3. A low-friction audit offer for your GovCon clients

**Preview:** A $299 entry audit can surface larger remediation work without forcing the big sell first.

**Body:**
Hi {{first_name}},

Quick partner angle.

We are packaging a 48-hour AI compliance gap analysis for GovCon subcontractors who know CMMC matters but are not ready to buy a full consulting engagement.

It is intentionally low-friction:

- $299 entry audit
- risk score + gap map
- prioritized remediation plan
- plain-English walkthrough

For partners, it creates a clean first step:

1. Your client gets clarity.
2. We identify what breaks first.
3. If deeper remediation is needed, there is a natural handoff or co-delivery conversation.

If you have GovCon/MSP clients stuck in the “we should deal with CMMC soon” stage, this is a useful door-opener.

Want me to send the one-page partner brief?

— Simon @ YaroSecurity

**CTA:** Reply `partner`  
**Tags:** add `segment:partner_fit`; if reply contains `partner`, create partner follow-up task.
