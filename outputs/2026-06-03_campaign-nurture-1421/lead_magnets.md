# Campaign Nurture — Lead Magnet Refresh
Run time: 2026-06-03 14:21 ET  
Campaign: Agent Governance / Verifiable Agent Logs  
Mode: staged / copy-ready; no pages or files published

## Publishing guardrail
These assets are ready for page/PDF/buildout, but not live. Before launch, confirm URLs, form consent language, thank-you pages, email delivery, file hosting, analytics, and suppression tags.

---

## Lead Magnet 1 — Agent Access Audit Checklist
**Primary segment:** `new_agent_interest`, `audit_intent`  
**Promise:** In 10 minutes, identify the AI agent workflow with the highest governance risk.

### Landing page copy
**Headline:** Your AI agent is not a chatbot. It is an employee with API keys.

**Subhead:** Use this checklist to map what one agent can access, what it can change, what needs approval, and whether you can prove what happened.

**Bullets:**
- Inventory every tool, repo, CRM, file store, browser session, API, or support queue the agent can reach.
- Identify whether the agent is draft-only, recommend-only, execute-with-approval, or execute-alone.
- Find missing approval gates, rollback paths, kill switches, owners, and audit logs.
- Create a first-pass risk score before giving the agent more access.

**Form fields:** first name, work email, company, role, primary agent workflow, autonomy level.  
**CTA button:** Get the checklist  
**Fallback CTA:** Reply `audit` and I’ll send the checklist.

### PDF/checklist outline
1. Agent identity: name, purpose, owner, business process.
2. Access map: systems, data types, read/write scope, credential exposure.
3. Autonomy level: draft, recommend, execute-with-approval, execute-alone.
4. Approval gates: customer replies, code/file changes, CRM/account updates, spend/API actions, sensitive data.
5. Audit trail: tool calls, file diffs, API actions, approvals, policy flags, rollback point, final outcome.
6. ROI layer: task completed, time saved, cleanup time, cost per successful outcome, revenue influenced.
7. Risk decision: highest missing control, next governance action, audit-needed yes/no.

### Thank-you page
**Headline:** Your checklist is ready.

Start with one workflow. If the agent can touch real business systems, do not scale access until you can answer what it did, what it touched, what changed, and how you would roll it back.

**CTA:** Book an Agent Governance Audit: {{book_agent_governance_audit_link}}

---

## Lead Magnet 2 — Blast Radius Calculator
**Primary segment:** `audit_intent`, `engaged_no_booking`  
**Promise:** Score agent risk using Access × Autonomy × Reversibility.

### Landing page copy
**Headline:** Know the blast radius before the agent gets more access.

**Subhead:** A lightweight calculator for founders, CTOs, ops leaders, and AI teams deploying agents into real workflows.

**Core framework:**
- **Access:** What can the agent reach?
- **Autonomy:** Can it act without review?
- **Reversibility:** How hard is the action to undo?

**CTA button:** Score my agent workflow

### Calculator scoring
**Access score**
1 = public/read-only  
2 = internal docs  
3 = customer/support/CRM data  
4 = repos, APIs, payment systems, private files, credentials-adjacent systems

**Autonomy score**
1 = draft only  
2 = recommendation only  
3 = execute with approval  
4 = execute alone

**Reversibility score**
1 = easy undo  
2 = moderate rollback  
3 = hard rollback / customer-visible  
4 = irreversible or compliance-sensitive

**Output bands**
- 1–8: low urgency; log and monitor.
- 9–24: moderate; define approval gates before expansion.
- 25–48: high; audit access, logging, rollback, and ownership.
- 49–64: urgent; freeze additional access until governance controls exist.

### Delivery blurb
Here is the Blast Radius Calculator.

Use it on the one workflow where an agent has the most real access. The first governance win is usually not a company-wide policy. It is putting controls around the workflow that can do the most damage.

**Audit CTA:** {{book_agent_governance_audit_link}}

---

## Lead Magnet 3 — Sample Agent Audit Log Template
**Primary segment:** `engaged_no_booking`, audit-page visitors  
**Promise:** Show what “agent receipts” actually look like.

### Landing page copy
**Headline:** Chat history is not an audit trail.

**Subhead:** See the fields a serious agent workflow should capture before it touches repos, CRMs, files, support tickets, APIs, or customer data.

**Template fields:**
- timestamp
- requester / approving human
- agent/workflow name
- business objective
- model/tool stack
- input references
- tool call / API action
- data touched
- file diff / record changed
- approval required Y/N
- approver
- policy violation flag
- rollback point
- final outcome
- business metric impacted
- cost per run

**CTA button:** Send me the template

### Thank-you page
**Headline:** This is what agent receipts look like.

If you cannot reconstruct what an agent touched, changed, approved, spent, exposed, escalated, and returned, you do not have an audit trail yet.

**CTA:** Book a black-box review: {{book_agent_governance_audit_link}}

---

## Lead Magnet 4 — AI Agent ROI Dashboard Spec
**Primary segment:** `roi_intent`, founders/CFO/operators  
**Promise:** Measure successful outcome cost instead of AI usage.

### Landing page copy
**Headline:** “We use AI agents” is not ROI.

**Subhead:** Use this dashboard spec to see which agents save time, create revenue, reduce errors, or create cleanup work.

**Dashboard panels:**
1. Weekly ops: tasks attempted, completed, rejected, reviewed, human cleanup time, spend.
2. Outcome: successful outcome count, cost per successful outcome, revenue influenced, tickets resolved, PRs merged, workflows completed.
3. Risk: policy violations, escalations, rollback events, sensitive-data touches.
4. Decision: scale, constrain, retrain, kill.

**CTA button:** Get the dashboard spec

### Thank-you page
**Headline:** Your ROI dashboard spec is ready.

If your agents cannot be tied to outcomes, they are experiments. The dashboard turns them into operating assets — or tells you which ones to shut down.

**CTA:** Book an ROI-oriented governance audit: {{book_agent_governance_audit_link}}

---

## Lead Magnet 5 — Partner One-Pager: Agent Black Box Sprint
**Primary segment:** `partner_fit`  
**Promise:** Give MSPs, AI consultants, and security partners a clear referral/co-delivery offer.

### One-pager sections
- **Problem:** Clients are deploying agents before access, approvals, logs, rollback, and ROI are clear.
- **Offer:** Agent Governance Audit / Agent Black Box Sprint.
- **Deliverables:** workflow inventory, access map, autonomy map, approval gap analysis, audit-log requirements, blast-radius score, ROI dashboard gaps, 30-day roadmap.
- **Best-fit clients:** support automation, internal ops agents, sales/revenue agents, coding agents, compliance-heavy workflows.
- **Partner paths:** referral, white-label strategy, co-delivered audit, implementation upsell.
- **CTA:** Reply `partner` or book partner call: {{partner_call_link}}

---

## Build priority
1. Agent Access Audit Checklist — highest utility as universal entry point.
2. Blast Radius Calculator — strongest retargeting asset for audit intent.
3. Sample Audit Log Template — best for converting abstract governance interest into concrete need.
4. ROI Dashboard Spec — strong founder/CFO branch.
5. Partner One-Pager — manual outbound/relationship asset.