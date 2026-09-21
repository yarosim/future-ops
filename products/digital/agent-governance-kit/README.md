# AI Agent Governance Starter Kit

**Practical governance for companies running AI agents and automations** — the minimum viable operating system for a fleet of agents that touch your data, your customers, and your money.

If your company runs agents, copilots, automations, or LLM pipelines that take *actions* (not just answer questions), you have an agent fleet. Most companies have no idea what those agents can actually do, what they cost, or what happens when one goes wrong. This kit fixes that in an afternoon of setup — not a six-month compliance program.

## What's Inside

| File | What it is | Use it when |
|---|---|---|
| **permission-matrix.md** | Template matrix mapping every agent to its owner, tools, data scopes, spend caps, approval gates, and blast-radius rating — with a filled example for an ops automation agent | Setting up governance, onboarding a new agent |
| **access-audit-checklist.md** | 50-point checklist across 7 areas: inventory, credentials, tool grants, data exposure, logging, spend/approval gates, rollback | Quarterly audits, post-incident, or the first time you ask "wait, what CAN our agents do?" |
| **incident-runbook.md** | Incident response for agents: kill-switch procedures, credential rotation, blast-radius triage, cause classification, post-incident review template | An agent misbehaves — or before it does |
| **monitoring-scorecards.md** | Daily per-agent and weekly fleet scorecards for cost, error rate, and permission drift | Keeping governance alive after week one |

## The 5-Step Implementation Guide (~one afternoon)

**Step 1 — Inventory (30 min).** List every agent/automation that takes actions. Name, owner, purpose. Include the "quick script" someone's laptop runs nightly — those are your biggest unknown risks. *(permission-matrix.md)*

**Step 2 — Rate and cap (30 min).** Give each agent a blast-radius rating (🟢🟡🟠🔴) and set spend caps: per-action, daily, and a hard stop that auto-disables the agent. Anything rated 🟠/🔴 gets approval gates on irreversible actions. *(permission-matrix.md)*

**Step 3 — Audit the gap (60–90 min).** Run the 50-point checklist against reality. Fix the three highest-leverage items first: revoke orphaned/shared credentials, enforce spend caps at the platform level, and test every kill switch. *(access-audit-checklist.md)*

**Step 4 — Prepare for the bad day (30 min).** Document each agent's kill switch (target: disabled in <5 minutes by one named human) and rehearse it once. Skim the runbook so you've seen it before you need it. *(incident-runbook.md)*

**Step 5 — Make it stick (15 min/week).** Set up the daily spend/error alerting and a 20-minute weekly scorecard review. Weekly cadence is what separates governance from a binder. *(monitoring-scorecards.md)*

Then: quarterly, re-run the audit checklist and review every permission-matrix row.

## Who This Is For

- Ops, security, and engineering leads running agents in production
- Founders who've accumulated automations faster than controls
- Teams that need to answer a customer/auditor/board question: *"How do you govern your AI agents?"*

## What This Is Not

- Not legal or compliance advice — see disclaimer
- Not a substitute for your security program; it slots into it
- Not vendor-specific — the templates work with any agent framework, LLM provider, or tool stack

## Disclaimer

This kit provides general operational templates for educational and internal governance purposes. It is not legal, security, financial, or compliance advice, and it does not address every regulatory regime (e.g., data-protection notification deadlines vary by jurisdiction — know yours *before* an incident). Consult qualified counsel and security professionals for your specific situation. No warranty is expressed or implied; you are responsible for how you implement and operate these practices.

---

*Version 1.0 — September 2026*
