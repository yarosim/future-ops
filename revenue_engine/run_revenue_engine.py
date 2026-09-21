"""Orchestrator — run once per scheduled tick (hourly).

1. Deposit monitor (Stripe -> ledger -> weekly total).
2. Lead engine (fire due drip emails if enabled).
3. Nightly telegram report (deposits since last report + weekly total).
4. Escalation if weekly total below target.

Exit codes: 0 ok, 2 blocked(needs key/leads), 3 error.
State stays in ledger/. No secrets read from code.
"""
import json
import os
import sys
from datetime import datetime, timezone

import deposit_monitor
import lead_engine
import ledger

BASE = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(BASE, "state.json")

# Config (override via env)
WEEKLY_TARGET_CENTS = int(os.environ.get("WEEKLY_TARGET_CENTS", "200000"))  # $2000/wk default
ESCALATE_AFTER_DAYS = int(os.environ.get("ESCALATE_AFTER_DAYS", "3"))


def load_state():
    if os.path.exists(STATE_FILE):
        try:
            return json.load(open(STATE_FILE, encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_state(st):
    json.dump(st, open(STATE_FILE, "w", encoding="utf-8"), indent=2)


def main():
    now = datetime.now(timezone.utc)
    state = load_state()
    last_report_day = state.get("last_report_day")
    today = now.strftime("%Y-%m-%d")

    # 1) deposits
    dep = deposit_monitor.run(since_hours=24)
    if dep.get("status") == "BLOCKED":
        # log only once per day, not every hourly tick
        if state.get("last_blocker_day") != today:
            ledger.log("blocker", "orchestrator", "Stripe key missing/rotated")
            save_state({**state, "last_blocker_day": today})
        print(json.dumps(dep)); print("EXIT=2"); return 2

    # 2) leads
    leads = lead_engine.run(email_enabled=os.environ.get("EMAIL_SENDING_ENABLED") == "1")
    if leads.get("status") in ("BLOCKED", "PAUSED") and os.environ.get("EMAIL_SENDING_ENABLED") == "1":
        ledger.log("blocker", "lead_engine", leads.get("reason", ""))

    # 3) nightly report
    produced = False
    if last_report_day != today:
        week_total_cents, week_count = ledger.totals_since(7)
        overhead_usd = round(week_total_cents / 100.0, 2)
        target_usd = round(WEEKLY_TARGET_CENTS / 100.0, 2)
        gap = round(target_usd - overhead_usd, 2)
        report = {
            "day": today,
            "week_deposits_usd": overhead_usd,
            "week_payments": week_count,
            "week_target_usd": target_usd,
            "gap_usd": gap,
            "unblock_actions": ["Supply rotated STRIPE_API_KEY"] if dep.get("status") == "BLOCKED" else [],
        }
        ledger.log("report", "orchestrator", json.dumps(report))
        save_state({**state, "last_report_day": today})
        # NOTE: wire this to a Telegram push (gateway/message) in production.
        print("NIGHTLY REPORT:", json.dumps(report, indent=2))
        produced = True

    # 4) escalate if below target several days running — placeholder hook
    print(json.dumps({"deposit_monitor": dep, "lead_engine": leads, "report": produced}, indent=2))
    print("EXIT=0")
    return 0


if __name__ == "__main__":
    sys.exit(main())