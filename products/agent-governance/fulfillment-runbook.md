# Secure Agent Governance Sprint — Fulfillment Runbook

## 1. Outcome and guardrails

Deliver a point-in-time, evidence-backed inventory, permission model, risk assessment, control design, and remediation roadmap. Never imply certification or guaranteed security. Do not collect raw secrets when screenshots, configuration exports, hashes, references, or supervised read-only review will suffice.

## 2. Roles

- **Engagement lead:** scope, schedule, client communication, QA, final readout
- **Security assessor:** evidence review, identity/permission/data-flow findings
- **Control engineer:** approval/logging/recovery design and remediation estimates
- **Client sponsor:** decisions, risk acceptance, escalation
- **Client technical owner:** access, evidence, configuration validation
- **Client security/compliance owner:** boundary, policy, evidence, framework context

One YaRo person may hold multiple internal roles, but final QA must be explicit.

## 3. Preflight — before the delivery clock starts

- [ ] Signed service order, scope tier, assumptions, exclusions, and payment terms confirmed
- [ ] Agent/system/business-unit limits confirmed
- [ ] Client authority and contacts confirmed
- [ ] Secure evidence workspace created; access tested; retention/deletion date recorded
- [ ] Intake reviewed; prohibited sensitive content removed/escalated
- [ ] Kickoff and final readout scheduled
- [ ] Read-only access preferred; production testing/change activity excluded unless separately authorized
- [ ] Engagement folder created: `00-admin`, `01-intake`, `02-evidence`, `03-analysis`, `04-deliverables`, `05-qa`

If evidence is incomplete, issue a dated request list. Unknowns remain findings; do not infer controls.

## 4. Ten-business-day workflow

### Day 1 — Kickoff and boundaries

- Confirm business outcomes, risk tolerance, critical actions, data classes, compliance/customer obligations, and incident contacts.
- Validate in-scope environments and explicit exclusions.
- Establish evidence IDs (for example `E-001`) and finding IDs (`AG-01`).
- Start decision/assumption log.

**Exit:** signed-off scope map and evidence request list.

### Day 2 — Inventory and ownership

- Normalize agent, subagent, MCP/plugin, model, RAG/memory, trigger, owner, status, and environment records.
- Reconcile declared inventory against available platform/admin/configuration evidence.
- Flag orphaned, duplicate, shadow, retired-but-active, or unknown agents.

**Exit:** draft agent registry; every row has owner or an ownership finding.

### Days 3–4 — Identity and permissions

- Trace each agent to service principals/accounts, OAuth grants, API keys, vault/PAM, roles, tokens, and revocation owner.
- Build resource-level permission rows: read/create/update/delete/send/execute/admin.
- Record constraints, inherited privilege, shared credentials, rotation, and review dates.
- Identify privilege chains through tools and subagents.

**Exit:** validated permission matrix and identity findings.

### Day 5 — Tool and data-flow mapping

- Map instruction sources, trust boundaries, retrieval/memory, model/provider, tools, destinations, telemetry, and retained artifacts.
- Identify regulated/sensitive data and egress, residency, retention, and vendor boundary assumptions.
- Highlight untrusted-input-to-privileged-action paths.

**Exit:** current-state data/tool-flow diagram with unresolved assumptions marked.

### Day 6 — Approval and action controls

- Classify actions: low, medium, high, critical.
- Validate whether approvals are technically enforced, attributable, timely, and independent enough for the consequence.
- Review allow-lists, thresholds, rate/value/destination limits, sandboxing, idempotency, and separation of duties.

**Exit:** risk-tier/approval design and immediate containment recommendations.

### Day 7 — Logging, stop, recovery, and incident path

- Sample logs for identity, agent/version, context reference, tool calls, before/after state, approver, result, and timestamp.
- Verify retention, access protection, time synchronization, alerting, and evidence retrieval.
- Walk through kill switch, credential revocation, rollback/restore, and incident escalation.
- Do not trigger production shutdown or rollback without authorization; use tabletop or non-production test where possible.

**Exit:** evidence sufficiency, recovery readiness, and incident-path findings.

### Day 8 — Analysis and roadmap

For each finding record:
- Condition and affected asset/action
- Evidence IDs and any limitation
- Threat/business impact
- Likelihood and severity rationale
- Immediate containment
- Recommended fix, owner, effort/dependency, and target date
- Applicable control/reference mapping, stated as mapping—not certification

Prioritize 0–7 days, 8–30 days, 31–60 days, and 61–90 days.

### Day 9 — Validation and QA

- Hold factual-validation session; client may correct facts but risk ratings require evidence to change.
- Remove unsupported absolutes and marketing claims.
- Check registry/matrix/diagram/finding consistency.
- Verify no secrets or unnecessary personal data are present.
- Independent read-through against acceptance checklist.

### Day 10 — Delivery and readout

Deliver:
- Executive report and top-10 risks
- Agent registry
- Permission matrix
- Tool/data-flow diagram
- Approval/risk-tier standard
- Governance standard/policy recommendations
- Evidence index and limitations
- 30/60/90-day remediation roadmap

Conduct readout, document decisions, explain remediation/managed-service options without pressure, and obtain receipt acknowledgment.

## 5. Finding severity

- **Critical:** Credible path to severe/irreversible impact, regulated-data boundary breach, security administration, payment/destructive action, or mission/safety impact without adequate preventive control.
- **High:** Material confidentiality, integrity, availability, legal, contractual, or customer impact is plausible and controls are missing/weak.
- **Medium:** Control weakness increases risk but consequence/exploit path is bounded or compensating controls exist.
- **Low:** Hygiene, documentation, or defense-in-depth improvement with limited direct impact.
- **Observation:** Context or improvement opportunity without a demonstrated control failure.

Severity is not solely a compliance score. Document rationale and uncertainty.

## 6. Escalation protocol

Immediately notify the client sponsor and designated security contact if evidence indicates active compromise, exposed credentials, uncontrolled critical writes, or prohibited regulated-data flow. Stop related testing, preserve evidence, recommend containment, and defer incident response to the client or a separately authorized engagement. Never alter production unilaterally.

## 7. QA acceptance checklist

- [ ] Counts match contracted scope
- [ ] Every agent has purpose, status, environment, and owner or a finding
- [ ] Every consequential action maps to identity, resource, approval, log, stop, and recovery
- [ ] Evidence IDs support every material factual claim
- [ ] Unknowns and client assertions are labeled
- [ ] Critical/high findings have immediate containment and owner
- [ ] Recommendations are implementable and prioritized
- [ ] Control mappings include a non-certification caveat
- [ ] Deliverables contain no credentials or unnecessary regulated/personal data
- [ ] Pricing, dates, and next steps match the service order

## 8. Closeout and data handling

- Export final read-only deliverables and checksum/version them.
- Record client receipt, accepted risks, and open evidence requests.
- Remove temporary access and ask the client to revoke engagement accounts.
- Delete or archive evidence according to the agreement; log completion.
- Schedule managed-service onboarding only under a separate signed order.
- Capture internal lessons without retaining client secrets.
