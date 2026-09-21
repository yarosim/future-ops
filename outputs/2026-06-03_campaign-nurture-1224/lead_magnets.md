# Campaign Nurture — Lead Magnets
Run time: 2026-06-03 12:24 ET  
Campaign: Agent Governance / Verifiable Agent Logs  
Mode: staged / copy-ready; no pages or files published

## Lead Magnet 1: Agent Access Audit Checklist
**Promise:** In 10 minutes, identify which AI agent workflow has the highest governance risk.

### Landing page section
**Headline:** Your AI agent is not a chatbot. It is an employee with API keys.

**Subhead:** Use this checklist to map what one agent can access, what it can change, what requires approval, and what would prove what happened.

**Bullets:**
- List every tool, repo, CRM, file store, browser session, API, or support queue the agent can reach.
- Identify whether the agent is draft-only, recommend-only, execute-with-approval, or execute-alone.
- Spot missing approval gates, rollback paths, kill switches, and audit logs.
- Create a first-pass blast-radius score before giving the agent more access.

**Form fields:** first name, work email, company, role, primary agent workflow, autonomy level dropdown (`draft only`, `recommend`, `execute with approval`, `execute alone`, `not sure`).

**CTA button:** Get the checklist

**Post-submit redirect:** checklist download + soft CTA to book Agent Governance Audit.

### Checklist content outline
1. **Agent Identity**
   - Name/purpose of agent or workflow
   - Owner / accountable human
   - Business process supported
2. **Access Map**
   - Tools and systems reachable
   - Data types reachable: public, internal, customer, financial, credential-adjacent, PII
   - Write access vs read-only access
3. **Autonomy Level**
   - Draft-only
   - Recommend
   - Execute with approval
   - Execute alone
4. **Approval Gates**
   - Customer-facing messages
   - Code/file changes
   - CRM/account updates
   - Payment/spend/API actions
   - Sensitive data access
5. **Audit Trail**
   - Tool calls logged
   - File diffs captured
   - API actions recorded
   - Human approvals linked
   - Rollback point documented
6. **Risk Decision**
   - highest-risk missing control
   - next governance action
   - whether this workflow needs an audit

### Thank-you page copy
**Headline:** Your checklist is ready.

Start with one workflow. If the agent can touch real business systems, do not scale access until you can answer what it did, what it touched, and what changed.

**CTA:** Book an Agent Governance Audit

---

## Lead Magnet 2: Blast Radius Calculator
**Promise:** Score agent risk using Access × Autonomy × Reversibility.

### Landing page section
**Headline:** Know the blast radius before the agent gets more access.

**Subhead:** A lightweight calculator for founders, CTOs, ops leaders, and AI teams deploying agents into real workflows.

**Core framework:**
- **Access:** What can the agent reach?
- **Autonomy:** Can it act without review?
- **Reversibility:** How easy is it to undo the action?

**CTA button:** Score my agent workflow

### Calculator outline
**Access score:**
1 = public/read-only  
2 = internal docs  
3 = customer/support/CRM data  
4 = repos, APIs, payment, private files, credentials-adjacent systems

**Autonomy score:**
1 = draft only  
2 = recommendation only  
3 = execute with approval  
4 = execute alone

**Reversibility score:**
1 = easy undo  
2 = moderate rollback  
3 = hard rollback / customer-visible  
4 = irreversible or compliance-sensitive

**Output bands:**
- 1–8: low governance urgency; log and monitor.
- 9–24: moderate; define approval gates before expansion.
- 25–48: high; audit access, logging, rollback, and ownership.
- 49–64: urgent; freeze additional access until governance controls exist.

### Email delivery blurb
Here is the Blast Radius Calculator.

Use it on the single workflow where an agent has the most real access. The first governance win is usually not company-wide policy; it is putting controls around the one workflow that can do the most damage.

**Audit CTA:** {{book_agent_governance_audit_link}}

---

## Lead Magnet 3: AI Agent ROI Dashboard Spec
**Promise:** Measure successful outcome cost instead of AI tool usage.

### Landing page section
**Headline:** “We use AI agents” is not ROI.

**Subhead:** Use this dashboard spec to measure which agents save time, create revenue, reduce errors, or create cleanup work.

**Dashboard panels:**
1. **Weekly Ops Panel**
   - tasks attempted
   - tasks completed
   - rejection rate
   - human review time
   - tool/token/API spend
2. **Outcome Panel**
   - successful outcome count
   - cost per successful outcome
   - revenue influenced
   - tickets resolved / meetings booked / PRs merged / workflows completed
3. **Risk Panel**
   - policy violations
   - escalations
   - rollback events
   - sensitive-data touches
4. **Decision Panel**
   - scale
   - constrain
   - retrain
   - kill

**CTA button:** Get the dashboard spec

### Thank-you page copy
**Headline:** Your ROI dashboard spec is ready.

If your agents cannot be tied to outcomes, they are experiments. The dashboard turns them into operating assets — or tells you which ones to kill.

**CTA:** Book an ROI-oriented Agent Governance Audit

---

## Lead Magnet 4: Sample Agent Audit Log Template
**Promise:** Show what “agent receipts” actually look like.

### Landing page section
**Headline:** Chat history is not an audit trail.

**Subhead:** See the fields a serious agent workflow should capture before it touches repos, CRMs, files, support tickets, APIs, or customer data.

**Template fields:**
- timestamp
- user/requester
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

**CTA button:** Send me the template

### Retargeting use
Best for warm prospects who clicked governance/audit content but have not booked. It turns abstract “governance” into a concrete deliverable.
