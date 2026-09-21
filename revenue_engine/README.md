# Revenue Engine

Autonomous revenue + Stripe deposit automation.
Runs on a schedule (while you work/sleep) and treats **Stripe deposits as the source of truth**.

## Operating rule
No metric without a date + source. Unknowns are labeled `UNKNOWN`, never inferred.
Every funnel event is appended to a dated ledger (`ledger/events.csv`).

## Pipeline (per run / hourly)
```
deposit_monitor.py   -> pull Stripe successful payments -> ledger + deposit totals
lead_engine.py       -> fire due lead actions (email drip) -> ledger
run_revenue_engine.py-> orchestrator: monitor + leads + nightly report + escalation
```

## State machine
`identified -> contacted -> engaged -> converted -> won`
Each lead row: `next_action_date` decides when the runner fires the next step.

## Guardrails
- Stripe key loaded from env ONLY (`STRIPE_API_KEY`). Never hardcoded.
- Email only to consented/warm leads (domain + unsubscribe + consent confirmed).
- If the Stripe key is missing/rotated, the engine reports `BLOCKED` — it never falls back to stale/compromised keys.
- Alert Simon only on: new deposit, goal miss, or blocker. No noise.

## One-time setup (Simon)
1. Supply a rotated `STRIPE_API_KEY` (write to env, not code).
2. Confirm which leads are consent-clean (3 named leads: Scott McKittrick, Andrew Bagrin, Justin Hill — opt-in?).
3. Schedule `run_revenue_engine.py` hourly (registered via Task Scheduler / cron).