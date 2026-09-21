# AI Agent Incident Runbook

**When to use:** An agent did something wrong, is doing something wrong, or you suspect it might be. During an incident you don't want to be designing process — you want a checklist. Follow phases in order. Speed matters most in Phase 1.

**Severity levels:**
- **SEV-1:** Money moving, customer-facing comms, data leaving the company, prod systems being changed/deleted. Drop everything.
- **SEV-2:** Wrong-but-contained actions (internal spam, wrong tickets, staging mess). Fix today.
- **SEV-3:** Cosmetic/wrong-output, no side effects. Fix in normal workflow.

---

## Phase 1 — STOP THE BLEEDING (first 15 minutes, SEV-1/2)

### 1.1 Kill the agent

Execute the **kill switch** from the agent's permission-matrix row — in order of preference:

1. **Revoke/disable its service account or API key** (fastest, works everywhere, kills all its tool access at once).
2. **Disable the agent runtime** (its scheduler/cron/framework "pause" flag) — use only if credential revocation is slower and the agent's dangerous capability is specific.
3. **Platform-side block** (revoke the specific OAuth grant, disable the integration, firewall the egress) — use when you only need to cut one capability, e.g., let it keep working but stop external sends.

⚠️ If multiple agents share credentials, killing the shared key kills all of them. That is the *correct* move during SEV-1 — sort out collateral damage later.

### 1.2 Stop the money

- If spend occurred: cancel/void pending transactions, reverse what's reversible (refunds, credit reversals), and check whether anything is *scheduled* to run later (queued actions, delayed jobs, recurring tasks) — kill those too. A paused agent's queue can still fire.

### 1.3 Stop the messages

- If external comms were affected: retract/deleted what can be deleted, post a holding statement if customer-facing and wrong (draft it with a human, send as a human), notify your support team with a one-liner so they don't get blindsided.

### 1.4 Declare it

Post in the incident channel: agent ID, severity, what's stopped, who's incident lead (default: agent owner), time stopped. Ten seconds of typing, saves an hour of confusion.

---

## Phase 2 — CONTAIN & ASSESS (next 1–4 hours)

### 2.1 Blast-radius triage — answer these five questions in order

1. **What could it access?** Pull its permission-matrix row — that's your ceiling of possible damage. If the agent could touch it, assume it might have.
2. **What did it actually do?** Read the audit log backward from detection time. List every action: tool call, target, spend, message, file/data touched.
3. **What's irreversible?** Split the action list into *reversible* (fix methodically in Phase 3) vs *irreversible* (handle first: sent messages, executed payments, deleted data, external disclosures).
4. **Did data leave?** Any tool that sends data externally (email, API calls to non-company endpoints, file uploads, pasted-to-LLM context) gets special scrutiny. If PII/regulated data may have left → legal/compliance notification clock may already be running. Loop in counsel now, not after cleanup.
5. **Is anyone else compromised?** If the trigger was a compromised credential (vs. a hallucination/injection), the credential may have been used outside the agent too. Check its auth logs for human-logins or unfamiliar IPs.

### 2.2 Classify the cause (pick one; more than one is possible)

| Cause | Signature | Implication |
|---|---|---|
| **Hallucination / bad decision** | Plausible-but-wrong action, no external input | Prompt/tooling/limit fix; add approval gate on that action class |
| **Prompt injection** | Agent acted on untrusted content it read (email, web page, ticket, doc) | Remove untrusted inputs from its context or require approval for actions triggered by them; treat injected instructions as attacker input |
| **Compromised credential** | Auth anomalies, actions at odd hours, unfamiliar IPs | Full credential rotation (Phase 3.2), treat as security incident |
| **Permission drift** | Agent did something its matrix didn't allow | Revoke extra grants, find how they were granted, audit who/what grants permissions |
| **Bad deploy/change** | Started after an update to its prompt, model, tools, or config | Roll back the change; add change-review for agent configs |
| **Upstream/dependency failure** | External service misbehaved and the agent trusted it | Validate external data before acting on it; cap trust in tools |

---

## Phase 3 — REMEDIATE

### 3.1 Fix the damage (reversible items)

Work the reversible list from the customer/money impact down. Version histories, billing reversals, config restores, ticket reverts. Document each undo action as you go — you'll need it for the post-incident review.

### 3.2 Rotate credentials (mandatory for SEV-1, credential-compromise, or suspected injection with data access)

1. Generate new dedicated credentials for the agent (same least-privilege scopes — this is your moment to trim, not re-grant everything).
2. Update the agent's secret store; confirm old credential is **revoked, not just replaced**.
3. Rotate anything the old credential could reach: downstream API keys it used, tokens it could read, session cookies if applicable.
4. If shared secrets existed anywhere in the blast radius: rotate those too, and then eliminate the sharing.
5. Record rotation date in the permission matrix.

### 3.3 Fix the root cause before restarting

Do **not** re-enable an agent until:
- [ ] The classified cause has a specific fix implemented (not "we'll be careful")
- [ ] Its tool grants have been re-audited against the matrix (drift removed)
- [ ] Any new approval gate needed is enforced in workflow, not in the prompt
- [ ] A test/shadow run of its core loop behaves correctly
- [ ] The agent owner signs off in the incident channel

**Restart in restricted mode:** re-enable with reduced capability (e.g., draft-only, capped spend at 25%) for 48–72 hours, then restore full permissions if scorecards are clean.

---

## Phase 4 — POST-INCIDENT REVIEW (within 5 business days)

Blameless, 30–45 minutes, led by the incident lead. The output is a one-page written review. Template:

```markdown
# Incident Review: [agent ID] — [one-line summary]
**Date/Duration:** | **Severity:** | **Incident lead:** | **Reviewer:**

## What happened (timeline)
- T0: [trigger/change]
- T+__ : [first wrong action]
- T+__ : [detected — and *how* (alert? human noticed?)]
- T+__ : [agent stopped]
- T+__ : [contained/remediated]
- T+__ : [restarted in restricted mode]

## Impact
- Financial: $____ (actual + reversed)
- Customers affected: n | Comms sent/retracted: list
- Data exposure: none / suspected / confirmed (fields, records, destinations)
- Downtime/ops disruption:

## Root cause (5-why, one level deeper than feels comfortable)
[Cause classification + the underlying process gap — why did the system *allow* this?]

## What went well / What went badly
[e.g., detection was fast via alert vs. we found out from an angry customer]

## Action items (each: owner, deadline, verification method)
- [ ] Fix ... — @owner — by DATE — verified by HOW
- [ ] Guardrail ... (new cap/gate/log) — @owner — by DATE
- [ ] Runbook/matrix update ... — @owner — by DATE

## Detection gap analysis
[How did we find out? Would X minutes/hours sooner have reduced impact? What alert would have caught it?]

## Blast-radius honesty check
[Was the permission matrix accurate for this agent? If not, that's an action item.]
```

**Rule:** every incident produces at least one *systemic* change (a cap, a gate, an alert, a matrix edit). An incident that only produces "the agent was told not to do that" will recur.

**Track across incidents:** MTTR to kill switch, detection source (alert vs. human), and repeat-cause rate. These three numbers are your governance program's real KPI.

---

## Quick-reference card (print this)

```
1. KILL: revoke credential → disable runtime → block platform grant
2. MONEY: cancel pending + queued actions, reverse what's reversible
3. COMMS: retract, hold-statement, brief support team
4. DECLARE: channel post — agent, severity, lead, time stopped
5. ASSESS: matrix ceiling → audit log → irreversible-first → egress check
6. CLASSIFY: hallucination / injection / credential / drift / change / dependency
7. ROTATE: agent creds + everything it could reach
8. FIX ROOT CAUSE → shadow-mode restart with sign-off
9. REVIEW ≤5 days → ≥1 systemic guardrail change
```
