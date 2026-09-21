# Agent Monitoring Scorecards

**Purpose:** Governance isn't the audit you do quarterly — it's the numbers you look at weekly. These two scorecards catch the three failure modes that actually burn companies: runaway spend, silent error loops, and permission drift.

**The rule that makes this work:** someone looks at these every week, on a schedule, and writes one line of commentary. A scorecard nobody reviews is decoration.

---

## Daily Scorecard (per high-blast-radius agent — 5 min/day, automated where possible)

| Metric | Definition | Green | Yellow | Red | My agent |
|---|---|---|---|---|---|
| **Spend today** | Total $ on agent actions (API + tools + purchases) | < 70% of daily cap | 70–100% | > cap / hard-stop hit | $____ / cap $____ |
| **Actions today** | Count of tool actions taken | in normal range | 2× baseline | 5×+ baseline (loop suspect) | ____ |
| **Error rate** | Failed/error tool calls ÷ total calls | < 2% | 2–10% | > 10% | ____% |
| **Denied attempts** | Actions blocked by permission/cap guardrails | 0–2 | 3–10 | >10 (agent "fighting" its limits) | ____ |
| **Human approvals pending** | Actions sitting in approval queue | < 5 | 5–20 | >20 (gate is becoming a bottleneck) | ____ |
| **External sends** | Emails/messages/posts sent | in normal range | 2× baseline | unexpected external sends at all | ____ |
| **Cost per successful outcome** | Spend ÷ completed useful tasks | stable | +50% | doubling (retry loop or quality collapse) | $____ |
| **Anomalies / notes** | Anything odd, one line | none | — | — | |

**Daily escalation rule:** any Red triggers same-day action — throttle, restrict mode, or kill switch. Don't "watch it another day."

> ⚠️ **Retry-loop signature to memorize:** actions spike, cost-per-outcome spikes, error rate moderate — the agent is repeating a failing action and paying for it each time. Cap retries at the platform level; alert on action-count vs. baseline.

---

## Weekly Scorecard (whole fleet — 20 min/week, reviewed by governance owner)

### 1. Cost view

| Agent | Spend this wk | vs. last wk | vs. budget | Cost/outcome trend | Flag |
|---|---|---|---|---|---|
| ops-automation-01 | $1,120 | +8% | ✅ | stable | — |
| _…one row per agent_ | | | | | |

Watch: week-over-week growth >20% for two consecutive weeks = investigate before it's a fire.

### 2. Reliability view

| Agent | Total actions | Error rate | Top error | Approval-gate rejects | Uptime/heartbeat |
|---|---|---|---|---|---|
| | | | | | |

Watch: a *rising* error rate with stable volume means an upstream tool is degrading — the agent will compensate in expensive or weird ways.

### 3. Permission drift view (the one everyone skips — don't)

| Agent | Granted tools vs. matrix | New grants this wk | Drift? | Revoked this wk | Owner re-confirmed |
|---|---|---|---|---|---|
| ops-automation-01 | 7/7 match | 0 | ✅ none | 0 | ✅ |

Drift check procedure (15 min, weekly):
1. Diff each agent's *live* tool grants/scopes against its permission-matrix row.
2. Investigate every delta: who granted it, when, why. If you can't answer in 5 minutes → revoke and ask afterward.
3. Check for new credentials/API keys created for each agent (unexpected keys = drift or compromise).
4. Confirm each agent's data-scope access is unchanged (new tables/collections/buckets appear constantly).

Watch: **any drift = same-week fix.** Drift is never benign by default; it's either someone's shortcut or an attacker's first step.

### 4. Governance health view

| Item | This week | Target |
|---|---|---|
| Alerts fired / acknowledged | ___ / ___ | 100% acknowledged <24h |
| Hard-stop breaches | ___ | 0 (each one = incident review) |
| Agents in restricted/shadow mode | ___ | known list, with exit dates |
| Approvals overdue (>48h) | ___ | 0 |
| Scorecard weeks completed in a row | ___ | streak matters — review cadence is the whole system |

---

## Weekly Review Ritual (how the numbers become governance)

1. **Scan for Red first.** Any red row → decide now: fix, restrict, or kill.
2. **Read the deltas, not the absolutes.** Stable-but-bad hides; change reveals.
3. **Write one line of commentary per agent** ("credit spend up due to promo week — expected"). Future-you, and your auditor, will thank you.
4. **Pick one improvement per week.** One new alert, one revoked grant, one automated metric. Compounding beats overhauls.

## Automation notes

- Most of this pulls from logs you already have: spend from billing/provider APIs, actions and errors from tool-call logs, approvals from your gate workflow. A simple script or BI dashboard beats a spreadsheet you update by hand — hand-updated scorecards die within a month.
- Minimum viable automation: daily spend + error rate alerting (any threshold alert), plus the weekly drift diff script. Start there, expand only if you keep reviewing.
