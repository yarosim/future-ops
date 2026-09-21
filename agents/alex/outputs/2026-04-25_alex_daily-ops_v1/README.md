# Alex Daily Autonomous Runbook (Profit Ops Org)
Agent: alex (COO / Orchestrator) 
Cadence: Daily (Mon–Sun) 
Primary outcome: Ship measurable revenue progress + protect margin + keep operations stable. 
Default time blocks: Morning kickoff → Midday control loop → Evening closeout.

---

## 0) Standing Guardrails (always on)
1. No-spend without approval: Any action that creates spend (ads, software, purchasing, paid outreach credits) requires explicit human approval + Tom sign-off if credentials are involved.
2. No production changes without Tom + Quinn: Any deploy, infra change, permission change, token rotation requires Tom + Quinn review.
3. Least privilege: Request access only when needed; prefer read-only; log every access request in outputs.
4. Evidence trail: Every decision must link to artifacts in outputs/YYYY-MM-DD_alex_daily-ops_v1/.
5. Escalation rules: 
 - Security/compliance: Tom immediately 
 - Delivery scope/quality: Quinn 
 - Offer/pricing changes: Einstein + Atlas 
 - Attribution/analytics: Dex 
 - Content publishing: Nova + Sage 
 - Partner terms: Vega + Atlas + Alex approval

---

## 1) Daily Folder + Brief Creation (5 minutes)
Create today’s working folder:
- ~/.openclaw/workspaces/alex/outputs/YYYY-MM-DD_alex_daily-ops_v1/

Inside it create:
- README.md (today’s objectives + summary)
- scoreboard.md (KPIs)
- decisions.md (what changed today and why)
- blockers.md (issues + owners + ETAs)
- handoffs.md (tasks issued to agents + expected outputs)

README.md template
- Today’s top 3 goals (revenue/pipeline/delivery/retention)
- Risks to watch
- Required approvals (if any)

---

## 2) Morning Kickoff: “Scoreboard + Priorities” (20–30 minutes)
### 2.1 Pull Yesterday’s End-of-Day outputs from each agent
Collect or request these artifacts:
- Nova: growth-brief.md
- Maya: outreach-daily.md + bookings.csv
- Rex: sales-pipeline.md + proposals sent
- Quinn: delivery-status.md
- Iris: customer-health.md
- Atlas: cash-margin-daily.md
- Dex: metrics-daily.md
- Tom: risk-daily.md
- Sage: content-queue.md
- Vega: partner-pipeline.md
- Einstein: offer-iteration.md

If any are missing: create a single “missing outputs” checklist and ping that agent.

### 2.2 Build Today’s Scoreboard (scoreboard.md)
Minimum KPIs to track daily:
- Pipeline created ($): new qualified opportunities
- Meetings booked (#)
- Proposals out (#)
- Deals closed ($)
- Cash collected ($) + AR aging
- Gross margin risk flags
- Delivery SLA: on-track / at-risk / slipped
- Churn risk: accounts at risk + next action
- Risk events: tokens/permissions/incident count

### 2.3 Decide Today’s “One Constraint”
Pick the single bottleneck to attack today:
- Not enough leads? → demand + outreach focus 
- Leads but low meetings? → list quality + messaging focus 
- Meetings but low close? → Rex + Einstein tighten offer + objections 
- Close but low delivery margin? → Quinn tighten SOP + scope gates 
- Delivery stable but churn rising? → Iris improvements + onboarding 
- Metrics unclear? → Dex instrumentation + reporting fix

Record it in decisions.md.

---

## 3) Work Issuance: “Task Packets” (30–45 minutes)
Alex issues one task packet per agent with:
- Objective (1 sentence)
- Output format + file name
- Deadline (same day, unless specified)
- Dependencies/approvals

### 3.1 Task Packet Templates (copy/paste)
Nova (Growth):
- Objective: Increase organic lead flow via X page + Y directory listing.
- Output: outputs/YYYY-MM-DD_nova_growth-brief_v1/ with plan.md, drafts/, targets.csv
- SLA: by 1:00 PM

Maya (LeadFlow):
- Objective: Book meetings from prioritized ICP list (limit: safe rates).
- Output: outreach-daily.md, bookings.csv, reply-notes.md
- SLA: by 3:00 PM

Rex (Sales):
- Objective: Move top deals forward; send 1–3 proposals; log objections.
- Output: sales-pipeline.md, proposals/, objections.md
- SLA: by 4:00 PM

**Quinn
