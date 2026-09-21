# Agent Permission Matrix — Template

**Purpose:** Every AI agent in your fleet should have exactly one row in this matrix. If you can't fill out a row for an agent, that agent has no business running in production.

**The core principle:** Agents get the *minimum* tool, data, and spend access needed for their job — the same way you'd treat a junior employee with root access to your payment processor. An agent's "blast radius" is what it can destroy (money, data, reputation, uptime) if it misbehaves, hallucinates, or gets prompt-injected.

---

## How to Use

1. List every agent/automation with a name and owner (a human, always a human).
2. Assign each agent a blast-radius rating using the scale below.
3. Grant tools, data scopes, and spend limits *consistent with* that rating — not whatever the agent currently has.
4. Any agent rated High or Critical must have approval gates on irreversible actions.
5. Review quarterly, and immediately after any agent incident.

### Blast Radius Scale

| Rating | Definition | Examples |
|---|---|---|
| 🟢 Low | Actions are reversible or confined to sandbox; no money, no PII | Draft docs, internal search, test environments |
| 🟡 Medium | Reversible with effort; touches internal-only data; small spend (<$100/day) | Content publishing to CMS, ticket creation, code PRs |
| 🟠 High | Affects customers, external comms, or meaningful spend; PII access; semi-irreversible | Customer emails, production deploys, purchase approvals |
| 🔴 Critical | Irreversible financial/external actions; regulated data; mass-reach capability | Payments/refunds, contract execution, bulk messaging, prod data deletion |

### Spend Limits — Rules of Thumb

- **Per-action cap** = largest single loss you'd accept from one hallucinated decision.
- **Daily cap** = per-action cap × 5–10, depending on how many autonomous actions per day.
- **Hard stop** = daily cap × 2. Breaching this disables the agent automatically and pages the owner.
- Any action above the per-action cap requires human approval. No exceptions.

---

## The Matrix Template

| Field | Value |
|---|---|
| **Agent name / ID** | |
| **Owner (human)** | |
| **Business function** | |
| **Blast radius** | 🟢 / 🟡 / 🟠 / 🔴 |
| **Allowed tools** | |
| **Explicitly denied tools** | |
| **Data scopes (read)** | |
| **Data scopes (write)** | |
| **PII / regulated data access** | None / Limited (fields listed) / Full |
| **Spend: per-action cap** | $ |
| **Spend: daily cap** | $ |
| **Spend: hard stop** | $ |
| **Approval gates** | Actions requiring human sign-off |
| **Environment** | prod / staging / sandbox |
| **Auth method** | Dedicated service account? Shared key? (Should be dedicated.) |
| **Credential rotation** | Interval + method |
| **Logging destination** | |
| **Kill switch method** | |
| **Rollback capability** | How are its actions undone? |
| **Last review date** | |
| **Next review date** | |

---

## Filled Example: Ops Automation Agent

> A backend agent that triages support tickets, drafts customer responses, applies account credits for goodwill, and manages infrastructure scaling via cloud API.

| Field | Value |
|---|---|
| **Agent name / ID** | ops-automation-01 |
| **Owner (human)** | Head of Support Ops (@jsmith) |
| **Business function** | Support ticket triage, draft responses, small goodwill credits, off-hours infra scaling |
| **Blast radius** | 🟠 High (customer-facing comms + spend + prod infra) |
| **Allowed tools** | `support_desk.read_tickets`, `support_desk.update_ticket`, `support_desk.draft_reply`, `crm.read_customer`, `billing.issue_credit` (≤$50), `cloud.scale_autoscaler`, `slack.post_internal` |
| **Explicitly denied tools** | `email.send_external`, `billing.issue_credit` >$50, `billing.refund`, `cloud.delete_resource`, `db.raw_query`, any social media tool |
| **Data scopes (read)** | Support tickets, CRM contact records, billing account summaries, infra metrics |
| **Data scopes (write)** | Ticket status/notes, reply drafts, credits ≤$50, autoscaler bounds |
| **PII / regulated data access** | Limited: contact name, email, plan tier. **Denied:** payment card fields, SSN/ID numbers, health data |
| **Spend: per-action cap** | $50 (single credit) |
| **Spend: daily cap** | $250 total credits |
| **Spend: hard stop** | $500 — auto-disable + page owner |
| **Approval gates** | Any credit >$50; any reply sent *directly* to customer without human review during first 90 days; any infra change during business hours; any action on enterprise-tier accounts |
| **Environment** | Production (read-only shadow mode for first 30 days) |
| **Auth method** | Dedicated service account `svc-ops-automation-01`; no shared keys |
| **Credential rotation** | Every 60 days, automated; immediately on incident |
| **Logging destination** | Central audit log (append-only), retained 1 year |
| **Kill switch method** | Revoke `svc-ops-automation-01` (1 CLI command, documented); also auto-disable on hard-stop breach |
| **Rollback capability** | Credits reversible via billing UI; tickets versioned; autoscaler changes reverted via config history. Customer replies are drafts only (no auto-send), so nothing external is irreversible |
| **Last review date** | 2026-09-01 |
| **Next review date** | 2026-12-01 |

### Why these choices (the reasoning that makes this a $99 doc)

- **Draft-only replies** for the first 90 days: the highest-risk tool for a support agent is *speaking to customers on your behalf*. Let it draft; a human clicks send. Promote to auto-send only after error-rate scorecards stay clean for a full quarter.
- **Credits under $50 with a $250/day ceiling:** goodwill credits are the classic runaway-spend vector. The hard stop at $500 means even a prompt-injection loop can't drain real money.
- **Denied `email.send_external` entirely:** the agent doesn't need it. If a future feature does, that's a *new permission request with a new review*, not a quiet scope creep.
- **Enterprise-tier approval gate:** one hallucinated credit or tone-deaf reply to your largest customer costs more than a year of the agent's value.

---

## Fleet Summary View (keep this at the top of your governance doc)

| Agent | Owner | Blast radius | Daily spend cap | Approval gates | Last reviewed |
|---|---|---|---|---|---|
| ops-automation-01 | @jsmith | 🟠 | $250 | Credits >$50, direct replies, enterprise accounts | 2026-09-01 |
| _…add rows_ | | | | | |

**Red flags to hunt for during review:**
- An agent whose *actual* tool grants exceed its matrix row (permission drift — check monthly)
- Shared credentials across agents (can't kill one without killing all)
- No named human owner (orphan agents get disabled, not adopted)
- "It's just a test agent" running in prod with prod credentials
