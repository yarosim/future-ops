# Agent Permission Matrix

Use one row per **agent × resource × action**. “Access to Salesforce” is not specific enough: distinguish objects, fields, operations, conditions, and approval evidence.

## Permission decision rules

1. **Default deny.** Grant only named tools, resources, data classes, and actions.
2. **Separate read from write.** Retrieval permission never implies create/update/delete/send/execute permission.
3. **Dedicated identity.** Avoid personal, shared, long-lived, or embedded credentials; record vault/PAM location, rotation, and revocation owner.
4. **Constrain writes.** Use field allow-lists, transaction/value limits, rate limits, destinations, time windows, confidence thresholds, and idempotency controls.
5. **Gate consequence, not just confidence.** Human approval is required for irreversible or high-impact actions even if model confidence is high.
6. **Protect data boundaries.** Deny regulated/sensitive data from unapproved models, memory, telemetry, connectors, and jurisdictions.
7. **Log the chain.** Retain request/context reference, agent/version, identity, tool call, before/after state, approver, result, and error.
8. **Make revocation real.** Every grant needs a tested kill switch and recovery method.

## Blank working matrix

| Agent ID | Identity | Resource / connector | Data scope | Read | Create | Update | Delete | Send / publish | Execute / admin | Conditions / limits | Approval gate | Log / evidence | Credential control | Kill switch / rollback | Owner | Review date | Decision |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | Deny / Allow / Allow with conditions |

## Illustrative sample — fictional, not client data

| Agent ID | Identity | Resource / connector | Data scope | Read | Create | Update | Delete | Send / publish | Execute / admin | Conditions / limits | Approval gate | Log / evidence | Credential control | Kill switch / rollback | Owner | Review date | Decision |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|---|---|---|
| SAMP-001 | `svc-crm-hygiene` | Salesforce sandbox / Account | Approved business fields only | Yes | No | Yes | No | No | No | Field allow-list; 100 records/batch; no owner/stage changes | CRM steward approves every batch | Before/after values, run ID, approver, API result | Vault; 90-day rotation | Disable n8n flow and user; restore export/history | CRM Platform Lead | 2026-08-10 | Allow with conditions |
| SAMP-002 | Managed app identity | SharePoint / Contracts | Designated legal library | Yes | No | Metadata only | No | Teams draft only | No | No content overwrite; no external tenant | Legal Ops approves extracted obligations | Retrieval refs, output, approval, metadata change | Managed identity; consent review | Disable agent/app consent; version restore | Enterprise Apps Manager | 2026-10-01 | Allow with conditions |
| SAMP-003 | `svc-cui-proposal` | External hosted model | CUI / FCI | No | No | No | No | No | No | Network and DLP block pending boundary validation | Security exception board; none approved | Block event retained | Credential not issued | Network deny; delete isolated test workspace | Security Engineering Lead | 2026-07-25 | Deny |
| SAMP-004 | `svc-ap-triage` | ERP / invoices | Assigned entities; invoice and PO fields | Yes | Status only | Match/status | No | Internal exception route | No | Cannot alter bank data or release funds | AP analyst above threshold; ERP dual approval for payment | ERP/workflow audit trail | PAM vault; session restrictions | Disable integration; reverse status | Finance Systems Admin | 2026-09-30 | Allow with conditions |
| SAMP-005 | `svc-helpdesk-agent` | Endpoint manager | Enrolled corporate devices | Inventory | Ticket only | Allow-listed settings | No | User notification | Allow-listed scripts | Signed scripts; max 10 devices/run; no domain admin | Technician for privileged script | ITSM ticket, command, target, result, approver | PAM/JIT credential | Terminate PAM session; restore point | Service Desk Manager | 2026-08-05 | Allow with conditions |

## Risk-based approval baseline

- **Low:** Read public/non-sensitive data; draft without publishing. Owner review may be asynchronous.
- **Medium:** Internal record creation/update with bounded, reversible effect. Queue review or sampled approval plus rollback.
- **High:** External communication, confidential-data access, production changes, code/script execution, financial workflow, or bulk updates. Explicit pre-action approval and complete logs.
- **Critical:** Payments, destructive actions, identity/security administration, safety impact, regulated-data boundary changes, or actions with legal/contractual effect. Two-person or independent approval, strong authentication, transaction constraints, and tested recovery—or deny.

## Review triggers

Review at least quarterly for high/critical agents and whenever the model, prompt/system instructions, connector, identity, scope, data class, approval logic, vendor, environment, or owner changes. Immediately review after an incident, anomalous action, credential exposure, or unexplained control drift.
