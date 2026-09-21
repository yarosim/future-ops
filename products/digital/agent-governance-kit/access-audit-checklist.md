# AI Agent Fleet Access Audit — 50-Point Checklist

**How to use:** Run this quarterly, and after any agent incident. Score each item ✅ pass / ⚠️ partial / ❌ fail / N/A. Anything ❌ in Section A–C is a same-week fix. Target: 45+ passes, zero fails.

**Golden rule you're auditing against:** *Every agent should be killable in under 5 minutes by one named human, with a clear picture of what it can touch, what it can spend, and what it did last night.*

---

## Section A — Inventory & Ownership (8 points)

1. ☐ A written inventory exists of every agent/automation running anywhere (including "quick scripts" someone's laptop).
2. ☐ Every agent has a named human owner (not a team, not a distribution list).
3. ☐ Every agent has a documented business purpose — "we've always had it" doesn't count.
4. ☐ Every agent has a blast-radius rating on file (see permission-matrix.md).
5. ☐ Orphan agents (no owner, no purpose) have been disabled, not ignored.
6. ☐ Personal agents/experiments are inventoried separately from production and verified to not touch prod resources.
7. ☐ Agent inventory is updated within a week whenever an agent is added or changed.
8. ☐ Someone is *accountable* for the whole fleet (one name, one role).

## Section B — Credentials & Auth (10 points)

9. ☐ Every agent uses a dedicated service account or API key — zero shared credentials with humans or other agents.
10. ☐ No agent uses a founder/admin/staff personal account or personal API key.
11. ☐ Credentials are stored in a secrets manager or encrypted vault — not in code, config files, chat messages, or prompts.
12. ☐ Secrets have been scanned out of git history (and any leaked keys were rotated, not just deleted).
13. ☐ Credential rotation schedule exists and is actually being executed (check last rotation dates).
14. ☐ Credentials use least-privilege scopes (an agent that only reads tickets shouldn't have tickets:admin).
15. ☐ No master/root/admin keys anywhere in the fleet unless explicitly documented and gated.
16. ☐ OAuth grants held by agents have been reviewed and revoked where unused.
17. ☐ MFA/phishing-resistant auth is enforced on accounts that manage agent infrastructure.
18. ☐ You can identify which credentials belong to which agent in under 10 minutes (there's a mapping).

## Section C — Tool Grants & Permissions (10 points)

19. ☐ Each agent's actual granted tools match its permission matrix row (check for drift — this is the #1 finding in real audits).
20. ☐ Tools that are dangerous-but-unused have been *revoked*, not just flagged.
21. ☐ Write access is separated from read access where the platform supports it.
22. ☐ No agent can grant permissions to other agents or modify its own access.
23. ☐ External-communication tools (email, SMS, social, mass messaging) are gated behind explicit review for every agent that has them.
24. ☐ Financial tools (payments, refunds, credits, purchases) have per-action and daily caps enforced at the *platform* level, not just in the prompt.
25. ☐ Shell/code-execution tools, where granted, are sandboxed and network-restricted.
26. ☐ Agents cannot access other agents' credentials, memory, or session data.
27. ☐ Recent tool-grant changes (last 90 days) were made deliberately and are documented.
28. ☐ Every tool grant maps to a real current business need ("might be useful later" = revoke).

## Section D — Data Exposure (8 points)

29. ☐ You know what data each agent reads (sources listed) and writes (destinations listed).
30. ☐ PII and regulated data (payment, health, ID numbers) are explicitly denied or field-limited per agent.
31. ☐ No agent sends internal data to external LLM APIs without knowing where that data goes (check provider data-retention settings).
32. ☐ Data egress destinations are enumerated and approved (the agent can't email your customer list anywhere).
33. ☐ Agent memory/context stores (conversation logs, vector DBs) are access-controlled and treated as sensitive data.
34. ☐ Test/staging agents do not have prod data access.
35. ☐ Retention exists: agent logs and memories are kept for a defined period, then purged.
36. ☐ Nothing in agent prompts/context contains secrets (passwords, keys, tokens get pasted into prompts — find them).

## Section E — Logging & Observability (6 points)

37. ☐ Every agent action (tool calls, sends, spends) is logged to a central, append-only store.
38. ☐ Logs capture *who/what*: agent ID, action, target, timestamp, cost, and outcome.
39. ☐ You can answer "what did this agent do yesterday?" in under 5 minutes.
40. ☐ Alerts fire on anomalies: spend spikes, error-rate spikes, denied-permission attempts, new tool grants.
41. ☐ Log access is restricted (logs contain sensitive context) and tamper-evident.
42. ☐ Someone actually looks at dashboards/scorecards at least weekly (there's evidence: review notes).

## Section F — Spend Caps & Human Approval Gates (5 points)

43. ☐ Per-action and daily spend caps exist for every agent that can move money, and are enforced technically.
44. ☐ A hard-stop mechanism auto-disables an agent when caps are breached — tested at least once.
45. ☐ Irreversible and high-risk actions (payments >threshold, external sends, deletions, contract actions) require human approval, enforced in workflow — not by asking the agent to "please ask first."
46. ☐ Approval routing works: approved requests go to a responsive human, with a defined fallback/timeout behavior.
47. ☐ First-run/shadow mode exists for new agents (read-only or draft-only before live actions).

## Section G — Rollback, Kill Switch & Recovery (3 points)

48. ☐ A documented kill switch exists per agent (revoke credential/disable flag), executable in <5 minutes by its owner, and has been *tested*.
49. ☐ Each agent's actions are reversible or recoverable (versioned content, reversible financial ops where possible, config history) — and you know the procedure per action type.
50. ☐ A restore-from-incident rehearsal has happened in the last 6 months (even a tabletop exercise counts).

---

## Scoring & Action Rules

| Score | Meaning |
|---|---|
| 45–50 ✅ | Fleet is governed. Keep the quarterly rhythm. |
| 35–44 | Real gaps. Fix all ❌s in Sections B, C, F within 2 weeks. |
| <35 | Your fleet is running ungoverned. Consider pausing non-critical agents until Sections A–C pass. |

**Highest-leverage fixes if you only have one day:** (1) map and revoke orphaned/shared credentials, (2) enforce spend caps at platform level, (3) test every kill switch. Those three close most of the real-world damage scenarios.
