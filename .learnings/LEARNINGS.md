# Learnings

Corrections, insights, and knowledge gaps captured during development.

**Categories**: correction | insight | knowledge_gap | best_practice

---

## [LRN-20260917-001] best_practice

**Logged**: 2026-09-17T01:00:00-04:00
**Priority**: high
**Status**: pending
**Area**: workflow

### Summary
A scheduled job firing is fresh evidence that supersedes historical documentation claiming the job is paused.

### Details
The self-analysis record described cron `fe9f5d87` as self-paused/deadlocked, but this scheduled invocation occurred at 01:00 EDT. The correct state is active but unreconciled. Operational reviews must separate observed-now, verified-previously, assumed-unchanged, and blocked/unverified states.

### Suggested Action
Keep future reviews delta-only, reconcile the cron to an intentional approved cadence, and require live scheduler verification before documenting any pause or state transition.

### Metadata
- Source: self-analysis
- Related Files: `memory/2026-09-17.md`, `outputs/improvement-plan-2026-09-17.md`, `MEMORY.md`
- Tags: scheduler, telemetry, state-reconciliation, self-analysis
- Pattern-Key: verify.runtime_state_before_claiming_pause
- Recurrence-Count: 1
- First-Seen: 2026-09-17
- Last-Seen: 2026-09-17

---
