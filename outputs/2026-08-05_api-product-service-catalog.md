# API-to-Revenue Product & Service Catalog

**Date:** 2026-08-05  
**Objective:** Build a high-margin, recurring, increasingly autonomous revenue operation from the named services—without using or exposing credentials, making financial promises, conducting unauthorized outreach, or publishing publicly.

## Operating assumptions and guardrails

- **The price ranges below are recommended client prices**, not provider subscription/API prices. Provider usage, hosting, taxes, and pass-through messaging/data charges should be quoted separately.
- “Autonomous” means automated research, drafting, routing, measurement, and internal operations. **Humans retain approval** for external messages, public posts, payments/refunds, account changes, regulated advice, contract submissions, and live financial transactions.
- Use least-privilege service accounts, encrypted secret storage, audit logs, client data-processing terms, retention limits, and a documented kill switch. Never place credentials in prompts, source control, screenshots, or deliverables.
- Do not scrape or contact people where terms, consent, privacy law, robots rules, or platform policy prohibit it. Apply CAN-SPAM/TCPA/GDPR/CCPA and sector rules as applicable.
- Market-data and trading products are educational/operational unless appropriately licensed. Do not promise outcomes or characterize model output as individualized investment advice.
- **Status meanings:** **Activate** = commercially useful now; **Test** = controlled pilot/sandbox; **Hold** = do not operationalize until ambiguity, permissions, or compliance is resolved; **Retire** = remove from near-term stack.

---

## Catalog

### A. Agent orchestration, channels, billing, and foundation models

| API/service | Capability | One sellable product/service | Ideal buyer | Recommended client pricing | MVP workflow | Required approvals / compliance | Key dependency | Status |
|---|---|---|---|---|---|---|---|---|
| **OpenClaw** | Tool-using agent runtime for browser, files, messaging, research, and scheduled workflows. | **Managed AI Operations Desk** that triages requests, drafts outputs, and updates systems of record. | 5–50 person professional-services firm. | $3k–$8k setup + $1k–$4k/mo. | Intake → classify → use approved tools → draft/action queue → human approval → log KPI. | Client tool authorization; least privilege; external-action approval; audit/retention policy. | Reliable integrations and scoped operator permissions. | **Activate** |
| **Paperclip** | Self-hosted multi-agent orchestration with goals, org charts, budgets, governance, and cost tracking. | **AI Team Control Plane implementation** for firms running several agents. | AI-native agency, studio, or internal automation team. | $7.5k–$25k implementation + $1.5k–$5k/mo support. | Map roles → deploy self-hosted instance → define budgets/approval gates → connect agents → governance dashboard. | Architecture/security review; board/admin authority for agent creation; model-use and data policies. | Stable agent adapters and Postgres/hosting. | **Test** |
| **Hermes** | Self-improving agent with memory/skills and an OpenAI-compatible server. | **Private Knowledge Worker appliance** hosted for one approved team. | Technical founder, research team, or consultancy. | $4k–$12k setup + $750–$3k/mo. | Deploy isolated instance → connect approved model/tools → seed SOPs → test memory → gated task queue. | Explicit consent for persistent memory; deletion/export controls; no sensitive terminal access by default. | Secure hosting and supported model/tool backend. | **Test** |
| **Telegram** | Bot-based chat, notifications, files, commands, and lightweight workflow UI. | **Client Delivery & Alert Bot** for approved customers or staff. | Agencies, property operators, field teams, membership businesses. | $1.5k–$6k setup + $300–$1.5k/mo. | Opt-in user → bot command/form → workflow → approved response/file → log. | User opt-in, bot disclosure, privacy notice; no unsolicited DMs. | Bot hosting and verified chat/user mapping. | **Activate** |
| **Stripe** | Checkout, subscriptions, invoices, payment links, customer portal, webhooks. | **Productized-service billing stack** with onboarding and recurring billing. | Consultants, agencies, SaaS/pre-SaaS operators. | $1.5k–$5k setup + $200–$750/mo, plus Stripe fees. | Approved offer → hosted checkout → webhook → onboarding record → invoice/renewal dashboard. | Merchant approval; refund/tax/chargeback terms; PCI scope minimized through hosted pages; human approval for refunds. | Clear offer, legal entity, bank/tax setup. | **Activate** |
| **Anthropic / Claude** | Long-context reasoning, writing, extraction, tool use, and structured outputs. | **Proposal/SOP Copilot** that produces evidence-linked drafts from client material. | Consultancies, GovCon firms, operations teams. | $2.5k–$10k setup + $500–$3k/mo. | Ingest approved corpus → retrieval → structured draft → factual checks → human sign-off. | Data-processing terms; copyright/confidentiality review; disclose AI assistance where required. | High-quality source corpus and evaluation set. | **Activate** |
| **OpenAI** | Multimodal generation, transcription, embeddings, structured outputs, and agent tooling. | **Multimodal Intake-to-Deliverable automation** for documents, images, and calls. | Agencies, clinics (non-diagnostic), brokers, service desks. | $3k–$12k setup + $750–$4k/mo. | Upload/record → extract → classify → generate draft → QA → approved delivery. | Consent for recording; sensitive-data rules; human review; avoid medical/legal/financial determinations. | Controlled data flow and testable output schema. | **Activate** |
| **OpenRouter** | Unified access/routing across many model providers, with usage controls. | **Cost/quality model-routing layer** for an existing AI workflow. | AI startups and agencies with variable workloads. | $2k–$8k setup + $500–$2k/mo + usage. | Benchmark task set → route by task/risk → fallback → cost/quality dashboard → monthly optimization. | Provider-by-provider data terms; no silent routing of restricted data; budget caps. | Representative evaluation suite. | **Activate** |
| **Perplexity** | Web-grounded search/research with citations. | **Executive Market Brief subscription** with source-linked weekly intelligence. | PE operating partners, agencies, founders, sales leaders. | $750–$3k/mo per niche. | Approved questions → search → verify primary sources → synthesize → editorial review → private delivery. | Respect source rights; avoid copying paywalled content; label uncertainty. | Strong niche taxonomy and editorial QA. | **Activate** |
| **Venice** | Privacy-oriented model inference and OpenAI-compatible generative APIs, subject to plan/policy. | **Privacy-sensitive drafting gateway** for non-regulated internal content. | Boutique legal/finance operations teams needing reduced data exposure. | $2.5k–$8k setup + $500–$2k/mo. | Classify data → route allowed prompts → redact → generate → human review → audit. | Vendor/security review; verify retention and model terms; do not infer compliance from marketing. | Documented data-handling assurances. | **Test** |
| **Gemini** | Multimodal reasoning and generation integrated with Google’s AI stack. | **Workspace Document Analyst** for summaries, comparisons, and draft decisions. | Google Workspace-based SMBs and professional teams. | $2.5k–$10k setup + $600–$3k/mo. | Select Drive files → permission-aware processing → structured analysis → reviewer queue → save approved output. | Workspace admin consent; sharing controls; sensitive-data classification. | Google Workspace permissions and stable schemas. | **Activate** |
| **Hugging Face** | Model/dataset hub, inference endpoints, Spaces, and open-source ML tooling. | **Private domain model evaluation & endpoint deployment**. | Product teams with repeatable NLP/vision workloads. | $5k–$25k project + $1k–$5k/mo ops. | Define task → shortlist licensed models → benchmark → deploy endpoint → monitor drift/cost. | Model/dataset license review; bias/safety testing; data provenance. | Labeled evaluation data and suitable infrastructure. | **Test** |
| **ElevenLabs** | Text-to-speech, voice design/cloning, dubbing, and audio agents. | **Approved-voice audio localization package** for courses and internal training. | Course publishers, enablement teams, media studios. | $1.5k–$8k/project or $750–$3k/mo. | Script → pronunciation/voice approval → synthesize → human audio QA → private delivery. | Documented voice-owner consent; no impersonation; disclose synthetic voice where required. | Rights-cleared voice and scripts. | **Activate** |
| **Modal** | Serverless CPU/GPU execution for model inference, batch jobs, and scheduled compute. | **Managed serverless AI backend** for bursty document/media jobs. | AI startups and agencies without DevOps staff. | $5k–$20k setup + $1k–$5k/mo + compute. | Containerize job → secrets via vault → queue → autoscale → observability → cost caps. | Security review; dependency licenses; regional/data requirements. | Production-ready code and workload profile. | **Test** |

### B. Email, communications, search, and web/data acquisition

| API/service | Capability | One sellable product/service | Ideal buyer | Recommended client pricing | MVP workflow | Required approvals / compliance | Key dependency | Status |
|---|---|---|---|---|---|---|---|---|
| **Gmail SMTP** | Transactional/manual email sending through a Google mailbox; limited compared with dedicated ESPs. | **Low-volume approved client notification workflow**. | Very small service firm with existing Workspace. | $500–$2k setup + $100–$400/mo. | Trigger → approved template → send to existing customer/staff → archive/log → bounce review. | Workspace admin approval; SPF/DKIM/DMARC; no cold campaigns; Google limits. | Healthy authenticated domain/mailbox. | **Test** |
| **Resend** | Developer-focused transactional and broadcast email API with domains, templates, and webhooks. | **Transactional lifecycle email implementation**. | SaaS and productized-service companies. | $1.5k–$6k setup + $250–$1k/mo + usage. | Domain verify → template → event trigger → send → webhook → suppression/analytics. | Consent and purpose limitation; CAN-SPAM/GDPR; unsubscribe for marketing; DMARC. | Product events and verified sending domain. | **Activate** |
| **SendGrid (disabled)** | Transactional/marketing email delivery and analytics. | Potential **legacy email modernization** service. | Existing SendGrid users with deliverability debt. | $2k–$8k migration project. | Audit only → design migration/remediation → execute only after re-enabled and approved. | **Currently disabled**; sender consent; suppression handling; deliverability rules. | Explicit enablement and account authorization. | **Hold** |
| **Twilio (disabled)** | SMS, voice, WhatsApp, verification, and communications workflows. | Potential **opt-in appointment reminder system**. | Clinics, home services, appointment businesses. | $2.5k–$8k setup + $300–$1.5k/mo + usage. | Consent capture → reminder queue → approved template → send → STOP handling → log. | **Currently disabled**; TCPA/CTIA/A2P registration; call recording consent; no unsolicited outreach. | Explicit enablement, verified sender, documented consent. | **Hold** |
| **Brave Search** | Web/news/image search API with independent index and structured results. | **Niche monitoring feed** for competitors, regulations, or prospects’ public signals. | Agencies, compliance teams, B2B operators. | $500–$2.5k/mo. | Saved queries → search → deduplicate → source validation → private digest → feedback loop. | Search terms must be lawful; source copyright/robots compliance; no personal profiling. | Well-defined query set and review policy. | **Activate** |
| **Tavily** | Search/extract/crawl optimized for LLM research workflows. | **Research pipeline implementation** for grounded reports. | AI teams, analysts, consultancies. | $2k–$8k setup + $500–$2k/mo. | Query plan → search → extract → evidence store → LLM synthesis → citation QA. | Respect source terms; do not republish protected content; maintain citations. | Reliable evaluation of source quality. | **Activate** |
| **Firecrawl** | Web crawling, extraction, mapping, and structured page conversion for AI pipelines. | **Website-to-knowledge-base build** for an owned/authorized domain. | SaaS support teams, franchises, documentation-heavy firms. | $2k–$10k setup + $300–$2k/mo. | Confirm ownership/permission → crawl allowlist → extract → dedupe → index → scheduled refresh. | Written crawl authorization; robots/ToS/rate limits; PII filtering. | Stable site structure and crawl scope. | **Activate** |
| **NewsAPI** | Programmatic news article discovery and metadata. | **Brand/industry news digest** with analyst commentary. | PR teams, investors’ ops teams, trade associations. | $500–$2k/mo. | Topics/sources → retrieve → dedupe → relevance score → summarize/link → private digest. | Check commercial plan and display rights; link rather than reproduce full text. | Correct license tier and editorial review. | **Test** |
| **Apify** | Cloud actors for scraping/browser automation, datasets, and schedules. | **Authorized public-web data pipeline**. | Market researchers, recruiters, e-commerce analysts. | $3k–$15k setup + $500–$3k/mo + usage. | Legal/ToS review → select/build actor → rate limit → normalize → QA → deliver dataset. | Written purpose; robots/ToS/privacy review; no bypassing access controls; deletion process. | Clearly permitted sources and resilient actors. | **Test** |

### C. Market data, databases, commerce, product analytics, and customer systems

| API/service | Capability | One sellable product/service | Ideal buyer | Recommended client pricing | MVP workflow | Required approvals / compliance | Key dependency | Status |
|---|---|---|---|---|---|---|---|---|
| **Polygon** | Legacy name/endpoint for market data provider now branded Massive. | **Legacy Polygon-to-Massive migration audit**. | Fintech with older Polygon endpoints/SDKs. | $2k–$7.5k one-time. | Inventory endpoints → compatibility tests → update base/SDK → regression test → cutover plan. | Data license review; no redistribution beyond entitlement. | Existing legacy integration. | **Retire** for new builds; maintain only for migration |
| **Finnhub** | Real-time/historical market, company, news, and alternative financial data APIs. | **Internal market-research dashboard** (not trading advice). | Research boutiques, IR teams, finance educators. | $3k–$12k setup + $500–$3k/mo + data. | Licensed symbols/data → dashboard → alerts → source attribution → analyst review. | Market-data display/redistribution license; disclaimer; no performance promises. | Correct exchange/data entitlements. | **Test** |
| **Massive** | REST, WebSocket, and flat-file market data across major asset classes. | **Licensed internal market-intelligence dashboard**. | Fintech teams and research shops. | $5k-$20k setup + $1k-$5k/mo + data. | Entitlements → ingest → permitted analytics → dashboard/alerts → QA. | Exchange/vendor licensing; attribution and redistribution limits; not personalized advice. | Suitable commercial data plan. | **Test** |
| **Airtable** | Flexible relational tables, forms, interfaces, automations, and API. | **SMB Operations Command Center** for intake, fulfillment, and KPIs. | Agencies, consultancies, field-service teams. | $2.5k-$10k setup + $400-$2k/mo. | Process map → schema → forms → views/automations → permissions → training. | Workspace owner approval; PII controls; backup/export plan. | Stable process owner and schema governance. | **Activate** |
| **Pinecone** | Managed vector database for semantic retrieval and metadata filtering. | **Private RAG knowledge assistant backend**. | Support, enablement, and research teams. | $4k-$15k setup + $750-$3k/mo + usage. | Prepare corpus → embed/index → retrieval tests → grounded response → monitor. | Document rights; tenant isolation; deletion/update process. | Good source corpus and embeddings. | **Activate** |
| **Notion** | Docs, databases, wiki/workspace, forms, and APIs. | **Company OS + SOP system** with AI-assisted upkeep. | 5-50 person service businesses. | $2k-$8k setup + $300-$1.5k/mo. | Audit → architecture → migrate → templates/permissions → review cadence. | Admin approval; confidentiality/sharing controls; human policy owner. | Engaged process owner. | **Activate** |
| **Supabase** | Hosted Postgres, auth, storage, realtime, edge functions, and APIs. | **Client portal backend accelerator**. | Agencies, SaaS MVPs, memberships. | $7.5k-$30k build + $1k-$5k/mo. | Schema → RLS → auth/storage → API → test → monitored deployment. | Privacy/security review; RLS tests; backups; residency requirements. | Sound schema and product requirements. | **Activate** |
| **Auth0 / Postgres** | Identity/access management plus durable relational storage. | **Secure B2B portal foundation**. | Professional-services and compliance-conscious SaaS firms. | $10k-$40k setup + $1.5k-$6k/mo. | Define tenants/roles → configure auth → schema → authorization tests → deploy. | Security architecture, MFA, breach/retention policies, DPIA where required. | Experienced engineering and threat model. | **Activate** |
| **Etsy** | Marketplace listings, orders, inventory, and shop management. | **Etsy listing operations & analytics** for a seller-owned shop. | Established handmade/vintage/digital sellers. | $750-$3k setup + $300-$1.5k/mo. | Seller authorizes → audit → draft changes → owner approves → update → measure. | Etsy terms; IP rights; truthful claims; seller approval. | Seller-owned products and shop authorization. | **Test** |
| **PostHog** | Product analytics, funnels, replay, flags, experiments, and surveys. | **Activation & retention instrumentation sprint**. | SaaS and product-led startups. | $4k-$15k setup + $750-$3k/mo. | Tracking plan → instrument → validate → funnels → approved experiments → insights. | Consent rules; replay masking; no dark patterns. | Reliable product events. | **Activate** |
| **Sentry** | Error/performance monitoring, tracing, releases, and issue triage. | **Application reliability monitoring setup**. | SaaS teams without mature observability. | $2.5k-$10k setup + $500-$2k/mo. | SDK → redact PII → release mapping → alerts → runbook → review. | Scrub secrets/PII; incident escalation authority. | Engineering access and release process. | **Activate** |
| **HubSpot (contact write disabled)** | CRM/pipeline data; contact writes are unavailable under the stated restriction. | **Read-only CRM intelligence & hygiene audit**. | HubSpot-using B2B SMBs. | $1.5k-$6k audit + $300-$1k/mo reporting. | Read authorized records → quality analysis → dashboards → recommendations → human applies edits. | **No contact writes**; admin approval; lawful basis; no unauthorized outreach. | Read permissions and field dictionary. | **Test** read-only; hold writes |
| **Intercom** | Customer messaging, support inbox, knowledge base, bots, and tickets. | **AI-assisted support operations setup**. | SaaS and digital-product teams. | $4k-$15k setup + $750-$4k/mo. | Audit tickets → build KB → draft assistant → escalation → QA → metrics. | Bot disclosure; sensitive-data handling; human escalation. | Quality KB and support owner. | **Activate** |
| **Linear** | Issue/project tracking, roadmaps, cycles, triage, and API. | **Product delivery operating system implementation**. | Software startups and agencies. | $2k-$8k setup + $300-$1.5k/mo. | Map workflow → teams/templates → connect intake → dashboards → cadence. | Admin approval; permissions; no autonomous priority changes. | Executive/process owner. | **Activate** |
| **Calendly** | Scheduling links, routing forms, round robin, reminders, webhooks. | **Qualified booking & handoff funnel** for inbound leads. | Consultants, agencies, sales/service teams. | $750-$3k setup + $150-$600/mo. | Approved inbound page → route → schedule → task/CRM → reminders → follow-up draft. | Consent/privacy; fair routing; no purchased-list outreach. | Existing inbound/referral traffic. | **Activate** |
| **X / Twitter** | Public posts/search access and social signals depending on API tier. | **Private social listening & draft queue**. | Founders, comms teams, niche analysts. | $750-$2.5k/mo + API tier. | Approved queries → collect permitted posts → summarize → draft → human approves. | Platform terms; copyright/privacy; **no autonomous public posting or unsolicited DMs**. | Suitable tier and editorial owner. | **Test** |
| **Discord** | Bots, community events, roles, commands, moderation, and webhooks. | **Member support and resource bot** for an owned community. | Paid communities, game studios, developer programs. | $1.5k-$6k setup + $300-$1.5k/mo. | Member invokes → retrieval/action → response → mod escalation → analytics. | Server-owner authorization; bot disclosure; moderation/youth-safety rules. | Active community and curated KB. | **Activate** |

### D. Finance/trading, productivity, infrastructure, automation, and public contracting

| API/service | Capability | One sellable product/service | Ideal buyer | Recommended client pricing | MVP workflow | Required approvals / compliance | Key dependency | Status |
|---|---|---|---|---|---|---|---|---|
| **Alpaca** | Brokerage/trading and market-data APIs, including paper trading. | **Paper-trading strategy evaluation environment**. | Fintech educators and internal quant teams. | $5k-$20k setup + $1k-$4k/mo. | Historical test → paper account → risk limits → simulated orders → reports. | No live trading initially; legal review and disclosures; no promises. | Paper environment and licensed data. | **Hold** live; **Test** paper only |
| **Bankr** | Agent-accessible crypto research, wallet, token, transfer, swap, NFT, and transaction capabilities. | **Read-only crypto treasury monitor**. | Web3 startups/DAOs with existing wallets. | $3k-$12k setup + $750-$3k/mo. | Authorized wallet watch → balances/exposure → alerts → reconciliation → human decision. | No transfers/swaps/deployment in MVP; owner approval; sanctions/tax review. | Read-only wallet/address scope. | **Hold** transactions; **Test** read-only |
| **Coinbase** | Crypto account, wallet, market-data, commerce/trading capabilities depending product. | **Crypto transaction reconciliation feed**. | Businesses already accepting/holding crypto. | $3k-$12k setup + $500-$2.5k/mo. | Read-only sync → categorize → fiat values → exception review → accounting export. | Tax/AML/sanctions obligations; no custody/discretionary trades. | Read-only access and accountant mapping. | **Test** |
| **Google Workspace** | Gmail, Drive, Docs, Sheets, Calendar, Meet, admin/collaboration APIs. | **Workspace workflow automation package**. | Google-centric SMBs. | $3k-$12k setup + $500-$3k/mo. | Admin scopes → intake → artifacts/events → review → audit. | Domain-admin approval; minimal OAuth scopes; sharing/retention policy. | Workspace admin and defined workflow. | **Activate** |
| **GitHub** | Repos, issues, Actions, releases, security, review, APIs/webhooks. | **Engineering automation & release governance**. | SaaS firms and technical agencies. | $4k-$15k setup + $750-$3k/mo. | Audit → templates → CI/security checks → protected releases → alerts. | Org-owner approval; secret scanning; human merge/release authority. | Maintained repo and tests. | **Activate** |
| **AWS** | Cloud compute, storage, databases, queues, AI, security, monitoring. | **Secure automation hosting foundation**. | SMB SaaS, agencies, regulated pilots. | $8k-$35k setup + $1.5k-$8k/mo + cloud. | Landing zone → IAM/network → workload → logs/backups → cost controls. | Security architecture; DPA/residency; incident plan. | Skilled cloud operations. | **Activate** |
| **Contabo** | VPS/VDS, dedicated servers, storage, and networking. | **Budget private-agent hosting** for non-critical work. | Bootstrapped agencies and labs. | $1.5k-$5k setup + $250-$1k/mo + hosting. | Harden VPS → firewall/VPN → containers → backups/monitoring → deploy. | Hardening and restore tests; avoid critical/regulated use until validated. | Competent sysadmin. | **Test** |
| **n8n** | Low-code workflow automation with nodes, webhooks, branching, and code. | **Revenue Operations Automation Sprint**. | B2B SMBs with fragmented SaaS. | $3k-$15k setup + $500-$3k/mo. | Map workflow → build/test → approvals/idempotency → deploy → monitor. | Connector authorization; secret vault; human gates for external writes. | Stable source systems. | **Activate** |
| **SAM.gov** | Official U.S. opportunities, entity/award data, and APIs. | **GovCon Opportunity Watch & Bid Readiness brief**. | Registered small federal contractors. | $750-$3k/mo + $2k-$8k onboarding. | Profile → query → transparent score → extract requirements → analyst review → private alert. | API owner approval; client owns representations; no bid submission or win promises. | Accurate capability profile. | **Activate** |
| **CONRINFO** | Exact service identity/capabilities were not verifiable from authoritative public documentation. | **No offer until vendor discovery**. | TBD. | Discovery only: $0-$1k internal validation. | Confirm legal vendor/domain → docs/terms → sandbox → security/license review. | Do not connect/buy until identity, provenance, rights, and security are verified. | Authoritative vendor docs. | **Hold** |
| **Systeme.io** | Funnel pages, email, courses, affiliates, and automations. | **Productized-service funnel setup** for warm/inbound traffic. | Solo consultants, coaches, educators. | $1.5k-$6k setup + $300-$1.5k/mo. | Offer → landing/checkout → opt-in → nurture → onboarding → analytics. | Truthful claims; consent/unsubscribe; refunds/tax; no earnings promises. | Validated offer and audience. | **Activate** |
| **Brevo** | Email/SMS/WhatsApp marketing and transactional messaging, CRM, automation. | **Consent-based lifecycle messaging system**. | E-commerce and service SMBs. | $2k-$8k setup + $400-$2k/mo + usage. | Permissioned contacts → segment → templates → approval → automation → suppression. | Consent proof; CAN-SPAM/GDPR/TCPA; authentication; STOP/unsubscribe. | Clean permissioned list. | **Activate** |
| **DropSpin** | Score-synced metronome using uploaded MusicXML and group sharing. | **Ensemble digital rehearsal setup**. | School music programs and orchestras. | $500-$2.5k setup + $100-$500/mo. | Rights-cleared XML → upload → collections/groups → invite authorized players → training. | Music rights; minor privacy; institution approval; API not publicly verified. | Rights-cleared scores. | **Test** manually; hold API automation |
| **NotebookLM** | Source-grounded notebooks, summaries, Q&A, study guides, and audio. | **Private research notebook build**. | Consultants, educators, deal/research teams. | $750-$3k/project. | Curate sources → notebook → briefs/questions → fact-check → private handoff. | Source rights/confidentiality; admin policy; human validation. | Rights-cleared sources. | **Test** |
| **AI Studio** | Gemini prompt/model prototyping and API experimentation. | **Gemini prototype & evaluation sprint**. | Product teams validating an AI feature. | $3k-$12k sprint. | Cases → prototype schema → evaluate → safety/cost tests → handoff. | No production secrets/sensitive data in prototypes; data-use review. | Representative test set. | **Test** |
| **MT4 / OANDA** | Forex/CFD charting, trade history, broker execution/data APIs by jurisdiction/account. | **Read-only trading journal and risk reporting**. | Self-directed traders or training firms. | $2.5k-$10k setup + $300-$1.5k/mo. | Read/export trades → normalize → descriptive metrics → journal → user review. | No autonomous execution; jurisdiction rules; risk disclaimers; no return promises. | Read-only trade history. | **Hold** execution; **Test** reporting |

## Top 5 bundled offers

Scores are **1-5**, with 5 best. For effort and risk, higher means lower effort/risk.

| Rank | Bundled offer | Core services | Time-to-revenue | Margin | Low effort | Low risk | Recurring | Rationale |
|---:|---|---|---:|---:|---:|---:|---:|---|
| **1** | **GovCon Opportunity Intelligence Desk** | SAM.gov, OpenClaw, Tavily/Brave, Airtable, Claude/OpenAI, Resend, Stripe | **5** | **5** | **4** | **4** | **5** | Start as a reviewed subscription using public/authorized data; clear pain and little custom software. |
| **2** | **B2B Research & Executive Briefing** | Perplexity, Tavily, Brave, NewsAPI, OpenClaw, Notion, Resend, Stripe | **5** | **5** | **5** | **4** | **4** | Very fast service-led launch and reusable niche templates; needs editorial/source-rights QA. |
| **3** | **SMB Revenue Operations Automation** | n8n, Airtable, Calendly, Stripe, Workspace, Resend/Brevo, PostHog | **4** | **4** | **3** | **4** | **5** | Strong setup and maintenance fees; integration variability raises effort. |
| **4** | **Private Knowledge & Support Copilot** | Pinecone, Firecrawl, OpenAI/Claude/Gemini, Intercom/Discord/Telegram, Supabase/Auth0 | **3** | **4** | **2** | **3** | **5** | Sticky once embedded, but requires security, permission-aware retrieval, and evaluation. |
| **5** | **AI Operations Control Plane** | Paperclip, OpenClaw, Hermes, OpenRouter, Modal/AWS/Contabo, GitHub, Sentry, Linear | **2** | **4** | **1** | **3** | **5** | Defensible recurring infrastructure, but governance and integration make it slowest. |

---

## Launch first: GovCon Opportunity Intelligence Desk

### Offer

Deliver a private, human-reviewed shortlist of relevant federal opportunities, requirement summaries, deadlines, and bid-readiness gaps. It **does not** guarantee awards, certify eligibility, or submit bids without explicit client approval.

**Initial niche:** U.S. small professional-services contractors with 1-3 established NAICS codes and limited capture staff. Start with one vertical (for example IT/cybersecurity services, training, or management consulting).

**Pilot pricing:** $500-$1,000 paid 14-day pilot, creditable toward $2,000-$4,000 onboarding; then $750-$1,500/month for reviewed briefs or $2,000-$3,000/month with requirement matrices/watchlists. Usage and proposal writing separate. No percentage-of-award pricing initially.

### MVP workflow

1. Authorized client intake: NAICS/PSC, set-aside, agencies, geography, contract-size band, exclusions, past performance, certifications, keywords.
2. Query SAM.gov through an approved account/API process or use permitted exports/manual search during pilot.
3. Apply hard filters and an explainable relevance score. Models summarize; they do not decide eligibility.
4. Analyst verifies notice status, deadline, place of performance, set-aside, attachments, qualifications, and authoritative links.
5. Store records and rationale in Airtable; generate private Notion/PDF/email brief.
6. Client marks pursue/no-pursue and reasons; feed back into filters. Never auto-submit.
7. Report opportunities screened, verified matches, false positives, decisions, and turnaround—not projected contract value or win probability.

### 14-day plan

| Day | Goal and exit criterion |
|---:|---|
| **1** | Freeze one-page offer, vertical, pricing, and exclusions: no submission, eligibility certification, award guarantee, or unauthorized outreach. |
| **2** | Build capability-profile form and Airtable schema for all matching/disqualifying fields. |
| **3** | Create three narrow SAM.gov search recipes and a documented manual fallback with authoritative notice links. |
| **4** | Create a transparent 100-point rubric with hard disqualifiers and explicit unknowns. |
| **5** | Build controlled intake → search/import → dedupe → draft → analyst queue → Airtable pipeline; no outbound actions. |
| **6** | Produce private brief template and QA checklist for status, deadlines, eligibility, attachments, and links. |
| **7** | Dry-run a fictional/public profile: screen 20+ notices, verify 5-10 examples, record defects; send nothing externally. |
| **8** | Measure precision, analyst minutes, model/search cost, and margin; tune filters. |
| **9** | Prepare sample redacted brief, SOW, privacy summary, and draft/test Stripe payment flow. |
| **10** | Build only a permissioned list of 15-25 warm contacts, inbound leads, referrals, or owner-approved accounts. |
| **11** | Obtain human outreach approval and personalize drafts. Without approval, use only private conversations/referrals/owned inbound. |
| **12** | Conduct 3-5 discovery calls; document vocabulary, filters, price response, objections; make no win claims. |
| **13** | Enroll one paid pilot with signed scope, payment, authorized profile, cadence, and named approver. If none, revise niche/message—not automation breadth. |
| **14** | Deliver first verified brief, collect pursue/no-pursue feedback, log defects, and offer conversion. |

### Acceptance and stop criteria

- Every recommended opportunity links to its authoritative notice and retrieval date.
- 100% of deadlines, status, and set-aside fields are human-verified before delivery.
- Target at least 70% “relevant enough to review” client ratings; this is a quality target, not a revenue/award promise.
- Test tenant isolation and client export/deletion.
- No external email, bid, CRM write, public post, payment/refund, or account change without named human approval.
- Record analyst time, provider costs, margin, and monthly workload.
- Pause if terms/API rights are unclear, client claims cannot be substantiated, notice status cannot be verified, or work would require prohibited enrichment, credential sharing, autonomous submission, or unsupported eligibility advice.

---

## Portfolio decisions

1. Start with **OpenClaw + one primary model + Tavily/Brave + Airtable + Stripe + one transactional email provider**; add redundant vendors only after benchmarks justify them.
2. Automate intelligence and drafts, not consequential action. Communication, account writes, payments, public posting, contract submission, and trading retain human gates.
3. Build new market-data projects against **Massive**; retain Polygon only for legacy migration, subject to licensing.
4. Keep Bankr, Coinbase, Alpaca, and MT4/OANDA read-only, reconciliation, reporting, or paper-only pending legal review and explicit approval controls.
5. Preserve current restrictions: SendGrid/Twilio remain disabled; HubSpot contact writes remain disabled.
6. Keep CONRINFO on hold; treat DropSpin as manual unless an authorized API and commercial terms are confirmed.
7. Configure PostHog consent/masking and Sentry PII/secret scrubbing before collecting telemetry.

---

## Authoritative references

- OpenClaw: <https://docs.openclaw.ai/>
- Paperclip: <https://paperclip.ing/>; <https://github.com/paperclipai/paperclip>
- Hermes: <https://hermes-agent.nousresearch.com/docs/>; <https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server>
- Telegram: <https://core.telegram.org/bots/api>
- Stripe: <https://docs.stripe.com/>
- Anthropic: <https://docs.anthropic.com/> | OpenAI: <https://platform.openai.com/docs/> | OpenRouter: <https://openrouter.ai/docs>
- Perplexity: <https://docs.perplexity.ai/> | Venice: <https://docs.venice.ai/> | Gemini/AI Studio: <https://ai.google.dev/gemini-api/docs>
- Hugging Face: <https://huggingface.co/docs> | ElevenLabs: <https://elevenlabs.io/docs/api-reference/introduction> | Modal: <https://modal.com/docs>
- Workspace/Gmail SMTP: <https://developers.google.com/workspace>; <https://support.google.com/a/answer/176600>
- Resend: <https://resend.com/docs> | SendGrid: <https://www.twilio.com/docs/sendgrid> | Twilio: <https://www.twilio.com/docs/messaging>
- Brave: <https://brave.com/search/api/> | Tavily: <https://docs.tavily.com/> | Firecrawl: <https://docs.firecrawl.dev/> | NewsAPI: <https://newsapi.org/docs> | Apify: <https://docs.apify.com/>
- Massive and Polygon rebrand: <https://massive.com/docs>; <https://massive.com/blog/polygon-is-now-massive>
- Finnhub: <https://finnhub.io/docs/api> | Airtable: <https://airtable.com/developers> | Pinecone: <https://docs.pinecone.io/> | Notion: <https://developers.notion.com/>
- Supabase: <https://supabase.com/docs> | Auth0: <https://auth0.com/docs> | PostgreSQL: <https://www.postgresql.org/docs/>
- Alpaca: <https://docs.alpaca.markets/> | Coinbase: <https://docs.cdp.coinbase.com/>
- GitHub: <https://docs.github.com/> | Etsy: <https://developers.etsy.com/documentation/> | PostHog: <https://posthog.com/docs> | Sentry: <https://docs.sentry.io/>
- HubSpot: <https://developers.hubspot.com/docs/api/overview> | Intercom: <https://developers.intercom.com/> | Linear: <https://developers.linear.app/> | Calendly: <https://developer.calendly.com/>
- X: <https://developer.x.com/> | Discord: <https://discord.com/developers/docs/intro>
- AWS: <https://docs.aws.amazon.com/> | Contabo: <https://api.contabo.com/> | n8n: <https://docs.n8n.io/>
- SAM.gov and official Opportunities API: <https://sam.gov/contracting>; <https://open.gsa.gov/api/get-opportunities-public-api/>
- Systeme.io: <https://help.systeme.io/> | Brevo: <https://developers.brevo.com/> | DropSpin: <https://www.dropspin.io/>
- NotebookLM: <https://support.google.com/notebooklm/> | OANDA: <https://developer.oanda.com/> | MT4: <https://www.metatrader4.com/en/trading-platform/help>

**Verification caveats:** No authoritative exact-match documentation was found for CONRINFO, so it remains on hold. Bankr capabilities were constrained to the provided service context and must be checked against current authorized documentation before any connection—especially transaction features. Recommended prices in this catalog are service prices, not vendor-price claims.
