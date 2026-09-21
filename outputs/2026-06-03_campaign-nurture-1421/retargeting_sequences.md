# Campaign Nurture — Retargeting Refresh
Run time: 2026-06-03 14:21 ET  
Campaign: Agent Governance / Verifiable Agent Logs  
Mode: staged / not launched

## Live launch requirements
Do not launch paid retargeting, email retargeting, SMS, or custom audiences until these are confirmed:
- booking/checkout URL for Agent Governance Audit
- working lead magnet pages/downloads
- verified email/SMS consent policy
- unsubscribe and suppression handling
- LinkedIn/X/Meta pixel or equivalent audience path
- CRM/ESP tags connected
- suppression lists: booked, active sales, unsubscribed, bounced, disqualified, partner-only

---

## Audience ladder
1. **Governance content visitors, no opt-in**
   - Rule: viewed agent governance/logging/least-agency content, no form submit within 24h.
   - Offer: Agent Access Audit Checklist.
2. **Checklist claimed, no audit click**
   - Rule: submitted checklist, no audit CTA click within 72h.
   - Offer: Blast Radius Calculator.
3. **Audit page visitors, no booking**
   - Rule: visited audit page, no booking after 48h.
   - Offer: Sample Agent Audit Log Template + workflow sanity-check reply prompt.
4. **ROI content engaged**
   - Rule: clicked/read ROI dashboard content, no audit click within 72h.
   - Offer: AI Agent ROI Dashboard Spec.
5. **Support/CX engaged**
   - Rule: clicked support, CX, escalation, PII, compliance content.
   - Offer: Compliance-Ready Support Agent Rollout / controlled pilot.
6. **Idle warm contacts**
   - Rule: opened/clicked once but no click/reply for 5 days.
   - Offer: “sanity-check one workflow” reply CTA.
7. **Partner-fit contacts**
   - Rule: MSP, AI/security consultant, agency, implementation partner.
   - Offer: Partner one-pager / referral angle.

---

## LinkedIn retargeting ad set
**Budget posture:** tiny validation budget only. Pause if no conversion tracking.  
**Frequency cap:** 2 impressions/day/person.  
**Objective:** lead gen form first if landing pages are not live; website conversion only after pages/pixel are validated.

### LinkedIn Ad 1 — Receipts
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

### LinkedIn Ad 2 — Least agency
**Primary text:**
Least privilege is not enough for agents.

They need least agency:

- task-scoped authority
- approval gates
- revocable access
- audit logs
- rollback paths
- kill criteria

Before your agent inherits a human login or broad API key, map the workflow.

**Headline:** Your agent needs boundaries  
**CTA:** Download  
**Destination:** {{agent_access_audit_checklist_link}}

### LinkedIn Ad 3 — Blast radius
**Primary text:**
Stop asking whether the AI agent is “safe.”

Ask for the blast radius:

Access × Autonomy × Reversibility

Score one workflow before the agent gets more access.

**Headline:** Score your agent workflow  
**CTA:** Download  
**Destination:** {{blast_radius_calculator_link}}

### LinkedIn Ad 4 — Audit offer
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

---

## X / Twitter retargeting copy
Use only when tracking/compliance path is confirmed.

### X Ad 1 — access audit
Your AI agent is not a chatbot.

It is an employee with API keys.

Before it gets more access, map what it can touch, change, approve, expose, and undo.

Get the Agent Access Audit Checklist: {{agent_access_audit_checklist_link}}

### X Ad 2 — logs
An AI agent without logs is just a black box with permissions.

Tool calls. File diffs. Approvals. Policy violations. Outcomes.

No logs, no trust.

Book an Agent Governance Audit: {{book_agent_governance_audit_link}}

### X Ad 3 — ROI
The wrong AI ROI question:
“What does the tool cost?”

The right one:
“What does each successful business outcome cost?”

Get the AI Agent ROI Dashboard spec: {{ai_roi_dashboard_link}}

### X Ad 4 — least agency
Least privilege says what the agent can access.

Least agency says what it can decide, change, approve, expose, spend, and undo.

Agents need both.

Download the checklist: {{agent_access_audit_checklist_link}}

---

## Meta retargeting ad set
Use only for compliant custom audiences. Avoid broad cold consumer targeting unless the page/offer is approved for that channel.

### Meta Ad 1 — checklist reminder
**Primary text:**
If an agent can access customer data, repos, CRMs, files, or APIs, it needs more than a chat summary.

Use the Agent Access Audit Checklist to find the first governance gap.

**Headline:** Your agents need receipts  
**CTA:** Download

### Meta Ad 2 — audit-log template
**Primary text:**
Not sure what an AI agent audit trail should capture?

Get the sample log template: tool calls, data touched, approval events, file changes, policy violations, rollback points, and outcomes.

**Headline:** Chat history is not an audit trail  
**CTA:** Learn More

---

## Email retargeting

### Email nudge 1 — Audit page visitor, no booking
**Trigger:** visited audit page, no booking after 48h.  
**Subject:** Want the audit-log template first?

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

### Email nudge 2 — ROI interest
**Trigger:** clicked ROI content/spec, no audit CTA click after 72h.  
**Subject:** Usage is not ROI

{{first_name}},

If your team is testing agents, the useful dashboard is not “who used AI this week.”

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

### Email nudge 3 — Idle warm contact
**Trigger:** no open/click/reply after 5 days.  
**Subject:** Sanity-check one workflow?

Hi {{first_name}},

If a full audit is not the right next step, start smaller.

Reply with one workflow where an agent can touch real systems — CRM, support tickets, repos, files, APIs, customer messages — and I’ll tell you what I’d check first.

No deck needed. Just the workflow.

— Simon

---

## SMS retargeting
Only if explicit SMS consent exists.

### SMS — Engaged no booking
Simon / Agent Governance: want me to sanity-check one AI workflow before you book? Reply with the workflow or grab a slot here: {{book_agent_governance_audit_link}}

### SMS — Checklist claimed, no click
Simon / Agent Governance: if your agent has tool/API access, score its blast radius before expanding permissions: {{blast_radius_calculator_link}}

---

## Manual DM retargeting prompts
Use for LinkedIn replies/comments only; do not automate unsolicited bulk DMs.

### Comment keyword response
Appreciate the interest. The quick version: start by mapping one agent workflow across access, autonomy, approvals, logs, rollback, and ROI. Want the checklist?

### Warm DM after public engagement
Saw you engaging with the agent-governance post. The cleanest first step is usually one workflow, not a giant policy doc. If you want, send the workflow your agent touches and I’ll point out the first control gap I’d check.

### Partner-fit DM
Looks like your clients may be experimenting with AI agents. We’re packaging an Agent Governance Audit / Black Box Sprint around access, approvals, logs, rollback, and ROI. Worth sending you the partner one-pager?

---

## Suppression rules
Suppress all nurture and retargeting when:
- contact books audit/consult
- contact purchases audit
- contact unsubscribes or opts out
- email bounces
- contact is in active sales conversation
- company is disqualified
- contact lacks consent for the selected channel
- contact is partner-fit and should receive partner branch only

## Measurement
Minimum dashboard:
- lead magnet page views
- form submits
- checklist-to-audit click rate
- audit-page visit-to-booking rate
- reply rate by segment
- booked calls
- qualified opportunities
- cost per qualified opportunity
- suppression/unsubscribe/bounce rate

## Recommended staged launch order
1. Organic/manual reply CTA: `Reply audit`.
2. Checklist landing page + thank-you CTA.
3. Email nurture to opted-in contacts.
4. Audit-page retargeting.
5. ROI/support partner branches.
6. Paid LinkedIn validation budget after tracking is verified.