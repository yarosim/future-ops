# Campaign Nurture — Newsletter Drip Refresh
Run time: 2026-06-03 14:21 ET  
Mode: staged / send-ready after CTA + consent verification  
Campaign: Agent Governance / Verifiable Agent Logs  
Primary offer: Agent Governance Audit / Agent Black Box Sprint  
Fallback CTA until live links exist: **Reply `audit` and I’ll send the checklist.**

## Launch guardrail
No external emails, DMs, SMS, ads, or posts were sent. This is a holding-pattern refresh for warm/opted-in contacts only. Do not send until Simon confirms: booking/checkout URL, lead magnet download URLs, sender list opt-in status, unsubscribe handling, CRM/ESP tags, and suppression rules.

## Segment map
- `new_agent_interest`: engaged with agent governance, black-box, logging, least-agency, or “employee with API keys” content.
- `audit_intent`: clicked/replied around logs, receipts, governance controls, approvals, blast radius.
- `roi_intent`: clicked/read ROI dashboard, cost per successful outcome, cleanup time, kill criteria.
- `support_intent`: clicked/read support-agent, CX automation, PII, escalation, compliance rollout.
- `engaged_no_booking`: clicked audit CTA or replied with interest but no booking after 48h.
- `idle_warm`: opened/clicked once but no reply/click for 5 days.
- `partner_fit`: MSPs, AI consultants, cybersecurity consultants, agencies, implementation partners.

---

## Email 1 — The receipts problem
**Timing:** Immediately after opt-in, comment keyword, or manual qualification  
**Audience:** `new_agent_interest`  
**Subject options:**
1. Your agents need receipts
2. Chat history is not an audit trail
3. The agent black box problem

**Preview:** If an agent can touch real tools, it needs a trail.

**Body:**
Hi {{first_name}},

The problem with AI agents is not that they are useless.

It is that they are becoming useful before teams can answer basic operating questions:

- What did the agent touch?
- What did it change?
- What required approval?
- What did it cost?
- What outcome came from it?
- What would make us shut it down?

That is the receipts problem.

A chatbot can be fuzzy. An agent with access to repos, CRMs, files, APIs, support tickets, or customer data cannot.

Start with one workflow and map:

- systems touched
- read/write access
- autonomy level
- approval gates
- audit-log coverage
- rollback / kill-switch path
- ROI measurement status

If you want the checklist, reply `audit` and I’ll send it.

— Simon

**CTA:** Reply `audit` / Download Agent Access Audit Checklist: {{agent_access_audit_checklist_link}}  
**Tags:** add `stage:nurture_started`; reply/click → `intent:agent_access_audit`.

---

## Email 2 — Least agency
**Timing:** +2 days after Email 1  
**Audience:** `new_agent_interest`, excluding booked/active sales  
**Subject options:**
1. Least privilege is not enough
2. Agents need least agency
3. Don’t give the agent your whole login

**Preview:** Permissions are only half the control problem.

**Body:**
Hey {{first_name}},

Least privilege is a good start.

But agents need something stricter:

**least agency.**

Not just “what can this agent access?”

Also:

- what can it decide alone?
- what can it change?
- what must a human approve?
- what is reversible?
- what gets logged?
- when does the workflow stop?

An agent should not inherit a human’s broad permissions just because it acts for that human.

The Agent Governance Audit maps one workflow end-to-end: identity, access, autonomy, approvals, logs, rollback, and ROI.

If you want to sanity-check one workflow first, reply with what the agent can touch.

— Simon

**CTA:** Book Agent Governance Audit: {{book_agent_governance_audit_link}} / reply with workflow  
**Tags:** click → `intent:governance_audit`; reply → `intent:workflow_sanity_check`.

---

## Email 3 — Blast radius
**Timing:** +4 days after Email 1  
**Audience:** non-booked contacts; prioritize `audit_intent`  
**Subject options:**
1. The blast-radius test
2. Access × autonomy × reversibility
3. Which workflow can do the most damage?

**Preview:** Pick the first workflow to govern by blast radius, not vibes.

**Body:**
{{first_name}},

A useful way to rank agent risk:

**Blast Radius = Access × Autonomy × Reversibility**

Access: what can it reach?  
Autonomy: can it act without review?  
Reversibility: how hard is it to undo?

A draft-only agent using public docs is low-risk.

An agent that edits CRM records, opens PRs, sends customer replies, calls APIs, or accesses private files is different.

Do not govern everything at once. Start with the workflow with the highest blast radius.

Get the calculator here: {{blast_radius_calculator_link}}

— Simon

**CTA:** Download Blast Radius Calculator  
**Tags:** click → `intent:blast_radius`; no booking after 48h → `engaged_no_booking`.

---

## Email 4 — ROI layer
**Timing:** +6 days after Email 1 or triggered by ROI content click  
**Audience:** `roi_intent` + unbooked nurture contacts  
**Subject options:**
1. Which agents should you kill?
2. Usage is not ROI
3. Stop measuring AI by tool cost

**Preview:** Successful outcome cost beats activity metrics.

**Body:**
Hi {{first_name}},

Most teams can tell you what their AI subscriptions cost.

Fewer can tell you what each agent returns.

The better dashboard tracks:

- tasks attempted
- tasks completed
- rejection rate
- human cleanup time
- token/tool/API spend
- successful outcome cost
- revenue influenced
- error reduction
- escalations created
- kill criteria

The point is not to prove every agent is valuable.

The point is to scale the ones that compound and kill the ones creating expensive noise.

Here is the AI Agent ROI Dashboard spec: {{ai_roi_dashboard_link}}

— Simon

**CTA:** Get ROI dashboard spec / book audit  
**Tags:** click → `intent:roi_dashboard`; add `stage:roi_educated`.

---

## Email 5 — Engaged, no booking
**Timing:** 48h after audit CTA click/reply with no booking  
**Audience:** `engaged_no_booking`  
**Subject:** Want me to sanity-check one workflow?

**Preview:** You do not need a company-wide map to find the first control gap.

**Body:**
Hi {{first_name}},

You do not need to map the whole company to get value from this.

Pick one workflow where an agent can actually act:

- edit files
- update CRM records
- draft/send customer messages
- open PRs
- call APIs
- move tickets
- access customer data

Reply with that workflow and I’ll tell you what I’d audit first.

Or book the audit here: {{book_agent_governance_audit_link}}

— Simon

**CTA:** Reply with workflow / book audit  
**Tags:** add `stage:booking_bump`; reply → `intent:manual_review`.

---

## Email 6 — Support/CX branch
**Timing:** Triggered by support, CX, PII, compliance, or escalation engagement  
**Audience:** `support_intent`  
**Subject options:**
1. Before the bot talks to customers
2. The safe support-agent pilot
3. Start with one controlled category

**Preview:** Support automation should start with a contained workflow, not a blank permission slip.

**Body:**
Hi {{first_name}},

For customer support, the safest path is not “replace support.”

It is one controlled category first:

- order status
- appointment rescheduling
- FAQ routing
- internal draft replies
- policy lookup
- low-risk account updates

Then define:

- what the agent may answer
- what it must escalate
- what PII is masked
- what requires approval
- what hallucination tests it must pass
- what handoff includes
- what triggers rollback

That turns chatbot risk into a governed pilot.

Request the support-agent rollout map here: {{support_agent_pilot_link}}

— Simon

**CTA:** Request support rollout  
**Tags:** add `branch:support_agent`; click → `intent:support_pilot`.

---

## Email 7 — Partner branch
**Timing:** Manual or automated after partner qualification  
**Audience:** `partner_fit`  
**Subject options:**
1. Partner angle: agent governance audits
2. A low-friction AI control-plane offer
3. Referral fit: Agent Black Box Sprint

**Preview:** A concrete entry offer for clients already experimenting with agents.

**Body:**
Hi {{first_name}},

A lot of companies are starting agent pilots before they have the controls around them.

That creates a clean partner wedge:

**Agent Governance Audit / Agent Black Box Sprint**

It maps one agent workflow across:

- tool/data access
- autonomy level
- approval gaps
- audit-log gaps
- rollback / kill-switch path
- ROI dashboard gaps
- 30-day control roadmap

Good fit for clients using agents in support, ops, sales, internal tools, coding, or compliance-heavy workflows.

If this fits your client base, reply `partner` and I’ll send the referral/partner brief.

— Simon

**CTA:** Reply `partner` / book partner call: {{partner_call_link}}  
**Tags:** add `branch:partner_fit`; reply → `intent:partner_conversation`.

---

## Send sequence rules
- Stop all buyer nurture on booking, active sales conversation, unsubscribe, bounce, or disqualification.
- Do not send SMS unless explicit SMS consent exists.
- Use fallback reply CTA until live landing/booking URLs are confirmed.
- If contact replies, suppress automation for 7 days and move to manual triage.
- Partner-fit contacts should receive partner branch, not generic buyer nurture.