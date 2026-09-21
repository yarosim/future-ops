# The 15-Minute Agent Privilege Audit

**Purpose:** A fast screening tool for AI agents, copilots, automations, and MCP/plugin-connected workflows. It is not a certification, penetration test, or legal/compliance opinion.

## How to use

Pick one production or pilot agent that has the greatest business impact. For each item, select **Yes (2)**, **Partial/Unknown (1)**, or **No (0)**. Record evidence, not intent. Maximum score: **20**.

| # | Control question | Yes — 2 | Partial/Unknown — 1 | No — 0 | Evidence / notes |
|---|---|---|---|---|---|
| 1 | **Named owner:** Is one accountable business/technical owner recorded? | Owner and backup named | Informal/shared ownership | No owner | |
| 2 | **Purpose and status:** Are use case, environment, lifecycle status, and users documented? | Current record | Some fields missing | Not recorded | |
| 3 | **Scoped identity:** Does the agent use a dedicated, non-human identity rather than a shared/user credential? | Dedicated identity | Mixed/delegated access | Shared or personal credential | |
| 4 | **Least privilege:** Are system, data, tool, and read/write permissions explicitly restricted to need? | Allow-listed and reviewed | Broad or incompletely reviewed | Unbounded/admin/unknown | |
| 5 | **Connector provenance:** Are MCP servers, plugins, tools, models, and vendors approved and versioned? | Approved inventory | Partial inventory/review | Unapproved or unknown | |
| 6 | **Sensitive-data boundary:** Are rules and technical controls defined for CUI, PHI, PCI, PII, secrets, and customer data as applicable? | Enforced and tested | Policy-only or incomplete | No boundary | |
| 7 | **High-risk approval:** Do external messages, financial actions, production changes, record deletion, code execution, and other consequential writes require appropriate approval? | Risk-based gates enforced | Some gates/manual convention | Autonomous high-risk writes | |
| 8 | **Action logging:** Can reviewers attribute prompts/context, tool calls, approvals, actor/agent identity, outputs, and outcomes with protected retention? | End-to-end, searchable logs | Partial/short-lived logs | Material actions unlogged | |
| 9 | **Stop and recovery:** Is there a tested kill switch, credential revocation path, rollback/recovery method, and incident owner? | Documented and tested | Exists, not fully tested | Missing/unknown | |
| 10 | **Evidence and review:** Are risk tier, approvals, exceptions, testing, changes, and periodic access reviews retained? | Current evidence package | Ad hoc/incomplete | No defensible evidence | |

## Interpretation

- **Green — 16–20:** Baseline governance appears present. Validate effectiveness, resolve partial items, and schedule recurring review. Green is not proof of compliance or security.
- **Yellow — 10–15:** Material governance gaps exist. Restrict high-impact writes, credentials, and sensitive-data access until evidence and ownership are complete.
- **Red — 0–9:** Privileged-agent risk is not adequately controlled. Pause or isolate consequential actions and sensitive-data access pending formal review.

### Critical override

Regardless of total score, classify **Red** if any of the following is true:
- An agent has admin, production, payment, deletion, or external-send capability with no approval gate.
- CUI, PHI, PCI data, credentials, or regulated/customer data may be sent to an unapproved service.
- There is no practical way to stop the agent or revoke its credentials.
- Material actions cannot be attributed or reconstructed from logs.

## Immediate next step

Inventory every agent and workflow, then validate identities, connectors, permissions, data paths, approval gates, logs, and recovery. YaRo Security’s **$750 Agent Privilege Audit** converts this screening result into an evidence-backed executive risk memo; the fee is credited toward a qualifying Governance Sprint started within 30 days.
