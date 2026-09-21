# Secure Agent Governance Intake

**Handling notice:** Do not paste passwords, API keys, tokens, private keys, CUI, PHI, PCI account data, production customer records, or other sensitive content into this form. Describe the data and provide sanitized evidence through YaRo Security’s approved secure channel after scope confirmation.

## A. Organization and engagement

- Legal organization name:
- Primary business location/time zone:
- Website:
- Industry and regulated/contractual obligations (CMMC/NIST 800-171, HIPAA, SOC 2, PCI DSS, GLBA, privacy, customer terms, etc.):
- Requested service: $750 Audit / $4,500 Starter Sprint / $8,500 Expanded Sprint / Unsure
- Executive sponsor (name/role):
- Technical coordinator (name/role):
- Security/compliance coordinator (name/role):
- Desired start date / deadline / triggering event:
- Authorized to approve assessment access and production changes? (roles only):

## B. Agent inventory

Repeat for each in-scope agent/workflow.

- Agent/workflow name and internal ID:
- Status: idea / pilot / production / retired
- Environment/tenant:
- Business purpose and expected outcome:
- Business owner and technical owner:
- Users or triggering systems:
- Platform/orchestrator (Copilot Studio, n8n, LangChain, CrewAI, custom, etc.):
- Model/provider and hosting arrangement:
- RAG, memory, vector database, or knowledge sources:
- MCP servers, plugins, APIs, browser/computer-use tools, and subagents:
- Dedicated identity, delegated user identity, shared credential, or unknown:
- Credential storage/rotation/revocation method (no secret values):
- Systems and repositories accessible:
- Data classes accessible (public, internal, confidential, PII, PHI, PCI, CUI/FCI, secrets, customer data):
- Read actions:
- Create/update/delete/send/publish/execute/admin actions:
- Volume, rate, dollar, destination, or field restrictions:
- Human approvals—what action, who approves, and how enforced:
- Logs available and retention:
- Kill switch / account revocation method:
- Rollback, restore, or compensation method:
- Last test/review and known incidents/exceptions:

## C. Architecture and data flow

- Where can instructions enter (users, email, tickets, websites, documents, APIs, retrieved content)?
- Which sources are untrusted or externally controlled?
- Where are prompts, outputs, memory, telemetry, and tool results stored?
- Can data leave the organization, tenant, region, or authorized compliance boundary?
- Are model/vendor training and retention settings documented?
- What network, DLP, content-filter, or egress controls apply?
- Does the agent invoke other agents or tools recursively?
- Attach or reference a sanitized architecture/data-flow diagram if available.

## D. Governance and operations

- Is there an AI/agent acceptable-use or governance policy?
- Who can create, approve, deploy, modify, and retire agents?
- Is risk tiering required before pilot/production?
- How are model, prompt, connector, identity, and permission changes approved?
- How often are access, exceptions, logs, and owners reviewed?
- How are incidents detected, escalated, contained, and reported?
- What evidence must be shown to auditors, customers, insurers, primes, or assessors?
- What would constitute unacceptable impact (financial, legal, mission, privacy, safety, customer, operational)?

## E. Evidence checklist

Indicate **Available / Partial / Not available / Not applicable**. Provide sanitized exports or read-only access later.

- Agent/workflow inventory
- Architecture and data-flow diagram
- Identity/RBAC/service-principal configuration
- Connector/MCP/plugin inventory and approvals
- Data classification and handling policy
- AI acceptable-use/governance policy
- Approval workflow configuration
- Sample action/tool-call logs and retention settings
- Change/deployment history
- Kill-switch/revocation procedure and last test
- Rollback/restore procedure and last test
- Incident-response plan and agent-specific escalation
- Vendor security/privacy terms and enterprise settings
- Prior assessments, exceptions, and risk acceptance

## F. Scope confirmation

- Number of agents/workflows:
- Number of connected systems/tools:
- Business units/environments:
- Primary sensitive-data boundary:
- Requested control/framework mapping:
- Systems explicitly out of scope:
- Known blackout/change-freeze dates:
- Required report audience and format:
- Is any production testing requested? If yes, describe; separate written authorization is required:

## G. Attestation

I confirm that the information is accurate to the best of my knowledge, that the organization is authorized to assess the listed systems, and that no prohibited secrets or regulated records are included in this form.

- Name / role:
- Signature or approval reference:
- Date:
