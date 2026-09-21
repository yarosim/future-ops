# Campaign Nurture — Newsletter Drip
Run time: 2026-06-03 12:24 ET  
Mode: staged / send-ready after CTA + opt-in verification  
Campaign: Agent Governance / Verifiable Agent Logs  
Primary offer: Agent Governance Audit / Agent Black Box Sprint  
Primary CTA placeholder: `{{book_agent_governance_audit_link}}`

## Operating note
No external emails, DMs, SMS, ads, or posts were sent. This run stages the Holding Pattern for opted-in or manually qualified leads only. Live launch remains blocked until Simon confirms CTA links, sender list/consent status, CRM/ESP tags, and booking/payment path.

## Segment map
- `new_agent_interest`: engaged with agent governance, black-box, audit-log, or “employee with API keys” content.
- `audit_intent`: clicked/replied around logs, receipts, governance, approvals, blast radius.
- `roi_intent`: clicked/replied around ROI dashboard, cost per outcome, CFO proof, kill criteria.
- `support_intent`: clicked/replied around support agent, CX automation, PII, compliance, escalation.
- `engaged_no_booking`: clicked audit CTA but no booking within 48 hours.
- `cold_or_idle`: no open/click/reply after 5 days.
- `partner_fit`: AI/security consultants, MSPs, agencies, implementation partners.

---

## Email 1 — Receipts
**Timing:** Immediately after opt-in, comment keyword, or manual qualification  
**Audience:** `new_agent_interest`  
**Subject options:**
1. Your agents need receipts
2. Chat history is not an audit trail
3. No logs, no trust

**Preview:** If an agent can touch tools, files, CRMs, repos, or customer data, it needs a trail.

**Body:**
Hi {{first_name}},

The issue with AI agents is not that they are useless.

It is that they are becoming useful before most teams can answer basic operating questions:

- What did the agent do?
- What did it touch?
- What did it change?
- What required approval?
- What business result came from it?
- What should make us shut it down?

That is the receipts problem.

A chatbot can be fuzzy.

An agent with tool access cannot.

If it touches repos, CRMs, files, support tickets, customer data, or APIs, it needs a trail.

Start with one workflow and map:

- systems touched
- permission scope
- approval gaps
- audit-log gaps
- rollback / kill-switch status
- ROI measurement status

**Download the Agent Access Audit checklist:** {{agent_access_audit_checklist_link}}

If you want a quick read, reply with the workflow your agent can touch and I’ll tell you where I’d look first.

— Simon

**CTA:** Download the Agent Access Audit checklist  
**Tags:** add `stage:nurture_started`; click → `intent:agent_access_audit`; reply → `intent:manual_review`.

---

## Email 2 — Blast Radius
**Timing:** +2 days after Email 1  
**Audience:** `new_agent_interest`, excluding booked contacts and active sales conversations  
**Subject options:**
1. The blast-radius test
2. Before the agent gets more access
3. Access × autonomy × reversibility

**Preview:** A simple way to identify which agent workflow needs governance first.

**Body:**
Hey {{first_name}},

A useful shortcut for agent risk:

**Blast Radius = Access × Autonomy × Reversibility**

Access: what can it reach?  
Autonomy: can it act without review?  
Reversibility: how easy is the action to undo?

A draft-only agent with public info is one thing.

An agent that updates CRM records, edits code, sends customer replies, calls APIs, or accesses private files is another.

The Agent Governance Audit maps that first:

- which agents/workflows exist
- who owns them
- what tools and data they can reach
- what requires approval
- what is logged
- what is missing
- which workflow has the highest blast radius

**Book the Agent Governance Audit:** {{book_agent_governance_audit_link}}

— Simon

**CTA:** Book the Agent Governance Audit  
**Tags:** click → `intent:governance_audit`; no booking after 48h → `engaged_no_booking`.

---

## Email 3 — ROI Layer
**Timing:** +5 days after Email 1  
**Audience:** non-booked contacts; prioritize `roi_intent` where present  
**Subject options:**
1. Which agents should you kill?
2. Stop measuring AI by subscription cost
3. The ROI layer under agentic work

**Preview:** Usage is not ROI. Successful outcome cost is closer to the truth.

**Body:**
{{first_name}},

Most teams can tell you what their AI tools cost.

Fewer can tell you what the agents return.

The useful layer is:

- tasks attempted
- tasks completed
- rejection rate
- human cleanup time
- token/tool/API spend
- successful outcome cost
- revenue influenced
- error reduction
- quality score
- kill criteria

The goal is not to prove every agent is magical.

The goal is to see which workflows compound and which workflows create expensive noise.

If ROI is your priority, we can orient the audit around the dashboard spec first.

**Get the AI Agent ROI Dashboard spec:** {{ai_roi_dashboard_link}}

— Simon

**CTA:** Get the dashboard spec / Book governance audit  
**Tags:** add `stage:roi_educated`; click → `intent:roi_dashboard`.

---

## Email 4 — Engaged No Booking
**Timing:** +48 hours after audit CTA click with no booking  
**Audience:** `engaged_no_booking`  
**Subject:** Want me to sanity-check one workflow?

**Preview:** You do not need to map the whole company to find the first risk.

**Body:**
Hi {{first_name}},

You do not need to map the whole company to get value from this.

Start with one workflow where an agent can actually take action:

- edit files
- update CRM records
- draft or send customer messages
- open PRs
- call APIs
- move tickets
- access customer data

Pick the one with the highest Access × Autonomy × Reversibility.

Reply with that workflow and I’ll tell you what I’d audit first.

Or book the audit here: {{book_agent_governance_audit_link}}

— Simon

**CTA:** Reply with workflow / Book audit  
**Tags:** add `stage:booking_bump`; reply → `intent:workflow_sanity_check`.

---

## Email 5 — Support Branch
**Timing:** Triggered for support/CX/compliance fit  
**Audience:** `support_intent`  
**Subject options:**
1. The safe way to roll out a support agent
2. Start with one safe support category
3. Before the bot talks to customers

**Preview:** Support automation should start with one controlled category, not a blank permission slip.

**Body:**
Hi {{first_name}},

If the use case is customer support, the safest path is not “replace support.”

It is one contained category first:

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
- what requires human approval
- what hallucination tests it must pass
- what handoff should include
- what triggers rollback

That turns a chatbot risk into a controlled pilot.

**Request the Compliance-Ready Support Agent Rollout:** {{support_agent_pilot_link}}

— Simon

**CTA:** Request support rollout  
**Tags:** add `branch:support_agent`; click → `intent:support_pilot`.

---

## Email 6 — Partner-Fit Branch
**Timing:** Manual or automated after partner qualification  
**Audience:** `partner_fit`  
**Subject options:**
1. Partner angle: agent governance audits
2. A low-friction control-plane offer for AI clients
3. Referral fit: Agent Black Box Sprint

**Preview:** A governance audit can surface implementation work without forcing a huge strategy sale.

**Body:**
Hi {{first_name}},

Quick partner angle.

A lot of teams are deploying agents faster than they can govern them.

That creates a clean entry offer:

- map the agent workflows
- identify access and approval gaps
- score the blast radius
- define an audit-log schema
- build a 30-day governance roadmap

It is low-friction enough to open the conversation, but concrete enough to create real follow-on implementation work.

If you work with founders, CTOs, ops teams, MSP clients, or AI builders, this may be a useful referral wedge.

Want the partner one-pager? Reply **partner** and I’ll send it over.

— Simon

**CTA:** Reply partner / Book intro  
**Tags:** add `branch:partner_fit`; reply contains `partner` → `intent:partner_referral`.
