# 3-Part Nurture Sequence — CMMC Holding Pattern
Campaign ID: `hp_cmmc_apr27`
Primary CTA URL: `https://yaro-security.com/ai-audit?utm_source=campaign_engine&utm_medium=holding_pattern&utm_campaign=cmmc_apr27`

---

## Email 1 — "How primes secretly grade subcontractors"
- **Send Timing:** Immediately after opt-in (Step 0)
- **From Name:** YaRo Security Intelligence Desk
- **Subject Options:**
  1. "The DFARS scorecard your prime won't show you"
  2. "Before your next option year, read this SPRS note"
- **Preview Text:** "Prime Readiness Checklist + how to read Supplier Performance Risk Reports in 3 minutes."
- **Body Copy:**
  ```
  Hi {{first_name}},
  
  Every prime we talk to runs two silent checks before they even reply to a subcontractor:
  1. **SPRS score recency** — if it's older than 12 months or blank, you fall to the bottom of the list.
  2. **Supplier Performance Risk Report (SPRR)** trends — even one unresolved finding can trigger an automatic pause.
  
  We pulled the exact DFARS 252.204-7020 language they're using and turned it into a quick Prime Readiness Checklist.
  
  👉 **Download it here:** {{prime_readiness_doc_link}}
  
  Use the checklist like a pilot's pre-flight:
  - Confirm you can state your system security plan (SSP) date within 10 seconds.
  - Know your current SPRS score and the 3 controls pulling it down.
  - Document how you monitor subcontractor flow-down risk.
  
  **Want a sanity check?** Reply "score" and paste your current control summary. We'll point out the top drift area within 24h — no pitch, just a second set of eyes.
  
  Holding the line with you,
  Simon + the YaRo Security team
  ```
- **CTA:** Text link "Download the Prime Readiness Checklist" pointing to `{{prime_readiness_doc_link}}` (Google Doc once published).
- **Automation Tags:** add `stage:hp_engaged`; if reply detected with "score", branch to SDR queue `hp_score_review`.

---

## Email 2 — "The 48-hour Control Compression Method"
- **Send Timing:** +2 days after Email 1
- **From Name:** Simon @ YaRo Security
- **Subject Options:**
  1. "How we compress 320 CMMC objectives into 5 workstreams"
  2. "Control Compression: inside the 48-hour audit"
- **Preview Text:** "Screenshots + walkthrough of the dashboard subs use to stay ahead of their primes."
- **Body Copy:**
  ```
  Hey {{first_name}},
  
  Most CMMC playbooks read like 300-page novels. Our Control Compression Method keeps it to **5 workstreams** so founders can move:
  1. Access Control
  2. Logging & Monitoring
  3. Incident Response
  4. Supplier Governance
  5. Workforce Training
  
  Inside the 48-hour audit, the AI engine scores each workstream, flags objective drift, and stages remediation cards. Here's a blurred snapshot so you can see the cadence we run:
  [image placeholder — YaRo dashboard]
  
  **Why it works:**
  - We auto-ingest your SSP, POA&M, and policy set, so you aren't rewriting anything.
  - The system maps every objective to an owner + due date (even if that's just you and one IT lead).
  - You leave the 48-hour sprint with an SPRS-ready packet plus the exact evidence your prime will ask for.
  
  If you want to see how your controls stack up, grab a 15-minute Control Compression consult slot here: {{calendly_link}}. We'll run your current workstreams through the dashboard live and hand you a prioritized fix list.
  
  Talk soon,
  Simon
  ```
- **CTA:** Button "Book a 15-min Control Compression consult" linking to `{{calendly_link}}` (Calendly placeholder).
- **Automation Tags:** add `intent:consult_interest`; if Calendly booking occurs, suppress Email 3 and move contact to `selling_event_invite` segment.

---

## Email 3 — "What happens if you wait for your prime to ask"
- **Send Timing:** +5 days after Email 1 (3 days after Email 2)
- **From Name:** YaRo Security Field Notes
- **Subject Options:**
  1. "The machining shop that almost lost its Navy contract"
  2. "Waiting for the prime's email cost them 42 days"
- **Preview Text:** "A 40-person shop nearly missed its option year — here’s how the 48-hour audit pulled them back."
- **Body Copy:**
  ```
  {{first_name}},
  
  One of our recent clients — a 40-person machining shop outside Norfolk — assumed they'd get plenty of warning before Level 2 enforcement. Here's how it actually unfolded:
  
  - **Day 0:** Prime asked for SPRS score + SSP addendum within 10 business days.
  - **Day 6:** They were still chasing internal evidence, so the prime escalated to compliance.
  - **Day 9:** Option-year renewal went "on hold" pending verification.
  
  They called us on Day 10. We ran the 48-hour audit, delivered a documented SPRS score of 92, and sent the exact gap remediation plan the prime was asking for. Contract saved, scramble avoided.
  
  We're walking through that scenario — and two others — during the **CMMC Reality Check** session next week. We'll grade live SPRS submissions, show what primes flag, and release 25 audit slots on the call.
  
  👉 **Save your seat:** {{selling_event_link}}
  
  Can't make it live? Reply "replay" and we'll send the highlight reel.
  
  Secure the option year before someone else does,
  YaRo Security Field Team
  ```
- **CTA:** Button "Reserve my CMMC Reality Check seat" linking to `{{selling_event_link}}` (Zoom registration).
- **Automation Tags:** add `stage:selling_event_invited`; if reply contains "replay", place contact into `selling_event_replay` automation.
