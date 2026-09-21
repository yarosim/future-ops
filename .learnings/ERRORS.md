# Errors

Command failures and integration errors.

---

## [ERR-20260914-RAG] memory_search_embedding_quota

**Logged**: 2026-09-14T01:00:00-04:00
**Priority**: high
**Status**: pending
**Area**: infra

### Summary
Semantic memory search remains unavailable because the embedding provider has exhausted its quota.

### Error
```text
429 insufficient_quota / credit_balance_exhausted
```

### Context
- Operation: `memory_search` during daily self-analysis.
- File-based memory fallback remains available and was used.

### Suggested Fix
Top up the embedding provider or switch to an approved local/provider embedding backend, then verify `memory_search` returns results.

### Metadata
- Reproducible: yes
- Related Files: `MEMORY.md`, `memory/2026-09-14.md`
- See Also: recurring RAG blocker in prior daily reviews

---

## [ERR-20260815-001] shell-path-null-redirection

**Logged**: 2026-08-15T01:00:00-04:00  
**Priority**: low  
**Status**: resolved  
**Area**: infra

### Summary
A PowerShell-invoked listing command used Unix-style `/dev/null` redirection and failed because the Windows environment mapped it to an invalid path (`C:\dev\null`).

### Error
```text
Could not find a part of the path 'C:\dev\null'.
```

### Context
Initial attempt to inspect daily memory files used `2>/dev/null`; the workspace runs Windows PowerShell.

### Suggested Fix
Use PowerShell-native `Test-Path`, `Get-ChildItem`, or `$null` redirection in this environment.

### Metadata
- Reproducible: yes
- Related Files: TOOLS.md

---

## [ERR-20260815-002] semantic-memory-search

**Logged**: 2026-08-15T01:00:00-04:00  
**Priority**: medium  
**Status**: pending  
**Area**: infra

### Summary
Semantic memory retrieval is unavailable because the configured OpenAI embeddings provider has exhausted quota.

### Error
```text
429 insufficient_quota — credit balance exhausted
```

### Context
`memory_search` failed during the daily self-analysis. Direct reads of daily memory files remain available.

### Suggested Fix
Restore embedding quota or configure and test a fallback embedding provider.

### Metadata
- Reproducible: yes
- Related Files: memory/2026-08-15.md, outputs/improvement-plan-2026-08-15.md

---
