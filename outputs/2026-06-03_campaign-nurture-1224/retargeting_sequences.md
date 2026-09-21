# Campaign Nurture — Retargeting Sequences
Run time: 2026-06-03 12:24 ET  
Campaign: Agent Governance / Verifiable Agent Logs  
Mode: staged / not launched

## Launch guardrails
Do not launch retargeting until tracking, consent, CTA links, and suppression rules are confirmed.

Minimum live requirements:
- confirmed booking/checkout URL for Agent Governance Audit
- working lead magnet pages/downloads
- verified opt-in/consent policy for email/SMS/custom audiences
- LinkedIn/X/Meta pixel or equivalent tracking path
- suppression list connected: booked, active sales, unsubscribed, disqualified

---

## Audiences
1. **Governance content visitors, no opt-in**
   - Rule: visited agent governance/black-box/logging content, did not submit form within 24h.
   - Offer: Agent Access Audit Checklist.
2. **Checklist claimed, no audit click**
   - Rule: submitted Agent Access Audit Checklist, no audit CTA click within 72h.
   - Offer: Blast Radius Calculator.
3. **Audit page visitors, no booking**
   - Rule: visited audit booking/checkout page, no booking within 48h.
   - Offer: Sample Agent Audit Log Template + workflow sanity-check reply prompt.
4. **ROI content engaged, no audit click**
   - Rule: clicked/read ROI dashboard content, no governance audit click within 72h.
   - Offer: AI Agent ROI Dashboard Spec.
5. **Support/CX content engaged**
   - Rule: clicked support agent / compliance / PII / escalation content.
   - Offer: Compliance-Ready Support Agent Rollout.
6. **Idle nurture contacts**
   - Rule: no open/click/reply after 5 days.
   - Offer: low-pressure “sanity-check one workflow” email.
7. **Partner-fit contacts**
   - Rule: MSP, AI consultant, cybersecurity consultant, agency, implementation partner.
   - Offer: partner one-pager / referral angle.

---

## LinkedIn retargeting ad set
**Budget posture:** tiny validation budget only; pause if no working CTA or conversion tracking.  
**Frequency cap:** 2 impressions/day/person.  
**Objective:** lead generation or website conversion depending on tracking readiness.

### Ad 1 — Receipts
**Format:** static or document ad

**Primary text:**
Your AI agent is not a chatbot.

It is an employee with API keys.

If it can touch repos, CRMs, files, support queues, APIs, or customer data, it needs receipts:

- what it accessed
- what it changed
- what required approval
- what outcome came from it
- what should trigger rollback

Use the Agent Access Audit Checklist before giving it more access.

**Headline:** Chat history is not an audit trail
**CTA:** Download
**Destination:** {{agent_access_audit_checklist_link}}

### Ad 2 — Blast Radius
**Format:** single image / carousel

**Primary text:**
Stop asking whether the AI agent is “safe.”

Ask for the blast radius.

Access × Autonomy × Reversibility tells you which workflow needs governance first.

Score one workflow before the agent gets more access.

**Headline:** Score your agent workflow
**CTA:** Download
**Destination:** {{blast_radius_calculator_link}}

### Ad 3 — Audit Offer
**Format:** static

**Primary text:**
If your agents are touching real workflows, you need more than prompts and summaries.

The Agent Governance Audit maps:
- agent workflows
- tool/data access
- approval gaps
- audit-log gaps
- blast radius
- ROI measurement
- 30-day control-plane roadmap

**Headline:** No logs, no trust
**CTA:** Book Now
**Destination:** {{book_agent_governance_audit_link}}

### Ad 4 — ROI Dashboard
**Format:** document ad

**Primary text:**
“We use AI agents” is not ROI.

Track successful outcome cost, cleanup time, rejection rate, revenue influenced, and kill criteria.

Get the AI Agent ROI Dashboard spec.

**Headline:** Which agents should you kill?
**CTA:** Download
**Destination:** {{ai_roi_dashboard_link}}

---

## X / Twitter retargeting copy
Use only when audience/tracking/compliance path is confirmed.

### X Ad 1
Your AI agent is not a chatbot.

It is an employee with API keys.

Before it gets more access, map what it can touch, change, approve, expose, and undo.

Get the Agent Access Audit Checklist: {{agent_access_audit_checklist_link}}

### X Ad 2
An AI agent without logs is just a black box with permissions.

Tool calls. File diffs. Approvals. Policy violations. Outcomes.

No logs, no trust.

Book an Agent Governance Audit: {{book_agent_governance_audit_link}}

### X Ad 3
The wrong AI ROI question:
“What does the tool cost?”

The right one:
“What does each successful business outcome cost?”

Get the AI Agent ROI Dashboard spec: {{ai_roi_dashboard_link}}

---

## Meta retargeting ad set
Use only for compliant custom audiences. Avoid cold consumer targeting unless offer/page is approved for that channel.

### Ad 1 — Checklist reminder
**Primary text:**
If an agent can access customer data, repos, CRMs, files, or APIs, it needs more than a chat summary.

Use the Agent Access Audit Checklist to find the first governance gap.

**Headline:** Your agents need receipts
**CTA:** Download

### Ad 2 — Sample audit log
**Primary text:**
Not sure what an AI agent audit trail should capture?

Get the sample log template: tool calls, data touched, approval events, file changes, policy violations, rollback points, and outcomes.

**Headline:** Chat history is not an audit trail
**CTA:** Learn More

---

## Email/SMS retargeting rules

### Email nudge — Audit page visitor, no booking
**Trigger:** visited audit page, no booking after 48h.

**Subject:** Want the audit-log template first?

**Body:**
Hi {{first_name}},

Saw you were looking at the Agent Governance Audit.

If you want to see what “agent receipts” actually means before booking, start with the audit-log template:

{{sample_agent_audit_log_template_link}}

The audit answers one practical question:

Can you prove what your agent did, what it touched, what changed, what required approval, and what business outcome came from it?

If yes, you can scale with more confidence.

If no, the next step is a control-plane review.

Book here when ready: {{book_agent_governance_audit_link}}

— Simon

### SMS nudge — Engaged no booking
**Trigger:** clicked audit CTA, no booking after 48h, SMS consent present.

**Copy:**
Simon / Agent Governance: want me to sanity-check one AI workflow before you book? Reply with the workflow or grab a slot here: {{book_agent_governance_audit_link}}

### Email nudge — ROI interest
**Trigger:** clicked ROI content/spec, no audit CTA click after 72h.

**Subject:** Usage is not ROI

**Body:**
{{first_name}},

If your team is already testing agents, the useful dashboard is not “who used AI this week.”

It is:

- tasks attempted
- tasks completed
- human cleanup time
- successful outcome cost
- revenue influenced
- errors reduced
- workflows to scale
- workflows to kill

Here is the dashboard spec again: {{ai_roi_dashboard_link}}

If you want this mapped against your actual workflows, book the audit here: {{book_agent_governance_audit_link}}

— Simon

---

## Suppression rules
Suppress all nurture and retargeting when:
- contact books audit/consult
- contact purchases audit
- contact unsubscribes or opts out
- email bounces
- contact is in active sales conversation
- company is disqualified
- contact is not opted in for the selected channel
- partner contact should receive partner branch instead of buyer nurture

---

## Measurement
Track weekly:
- governance content visits → checklist opt-ins
- checklist opt-ins → blast-radius calculator clicks
- lead magnet claim → Email 1 open/click/reply
- audit page visits → bookings
- audit CTA clicks → booked call rate
- ROI spec downloads → audit/ROI dashboard conversations
- support branch clicks → pilot conversations
- partner replies → referral conversations
- idle contacts recovered by workflow sanity-check bump
