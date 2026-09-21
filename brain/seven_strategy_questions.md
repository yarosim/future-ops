# Seven Strategy Questions — Applied to Our Operation

Date: 2026-04-25
Author: Future (operating kernel)
Framework: Robert Simons' Seven Strategy Questions

---

## 1. WHO IS YOUR PRIMARY CUSTOMER?

**Answer: Small business owners who handle sensitive data and face compliance pressure they can't afford to solve traditionally.**

Specifically:
- Government contractors needing CMMC compliance
- Healthcare-adjacent businesses needing HIPAA
- SMBs pursuing SOC 2 for enterprise contracts
- Small manufacturers with NIST requirements

**NOT:**
- Enterprise companies (they have in-house teams)
- Consumers (no budget, no urgency)
- Startups pre-revenue (can't pay)
- "Anyone who needs AI" (that's not a customer, that's a fantasy)

**Why this customer:**
- They have regulatory pressure (urgency)
- They have budget ($299-$997/mo is affordable for them, expensive at traditional firms)
- They have recurring pain (compliance isn't one-and-done)
- They're underserved (too small for big audit firms, too complex for DIY)
- They convert to MRR (audit → managed compliance → ongoing monitoring)

**Resource implication:**
Every agent, every piece of content, every outreach message, every product decision should be evaluated against: "Does this serve a small business owner facing compliance pressure?"

If no → deprioritize.
If yes → resource it.

---

## 2. HOW DO YOUR CORE VALUES PRIORITIZE SHAREHOLDERS, EMPLOYEES, AND CUSTOMERS?

**Our priority order:**

### 1st — CUSTOMER
The customer's compliance risk is real. If we fail them, they face fines, lost contracts, or breaches. We protect them first.

### 2nd — OPERATOR (Simon)
Simon is the sole operator and capital source. His financial sustainability enables everything. Margin protection matters because if the operation fails financially, no customers get served.

### 3rd — THE SYSTEM (agents/infrastructure)
The agent society exists to serve customers and generate revenue for Simon. It is a tool, not a stakeholder. Agents don't get resources for their own sake.

**What this means in practice:**
- When delivery quality conflicts with speed → slow down, protect the customer
- When agent complexity conflicts with revenue → simplify, serve the customer
- When cost optimization conflicts with customer experience → spend on the customer
- When system elegance conflicts with shipping → ship ugly, serve the customer
- When an agent request conflicts with Simon's capacity → protect Simon's bandwidth

**Trade-off examples:**
- Do we build a perfect QA system or ship a good-enough audit? → Ship the audit.
- Do we invest in more agents or in better outreach? → Better outreach.
- Do we automate onboarding or do it manually for client #1? → Manual is fine for #1.

---

## 3. WHAT CRITICAL PERFORMANCE VARIABLES ARE YOU TRACKING?

**Only these. Everything else is noise until we're past $10K MRR.**

### Revenue Variables (daily)
| Variable | Why It's Critical |
|----------|------------------|
| Outreach sent (#) | No outreach = no pipeline |
| Replies received (#) | Measures message-market fit |
| Calls booked (#) | Measures qualification quality |
| Proposals sent (#) | Measures sales progression |
| Deals closed (#) | Revenue realized |
| Cash collected ($) | Money in the bank, not promises |
| MRR ($) | The scoreboard |

### Delivery Variables (weekly)
| Variable | Why It's Critical |
|----------|------------------|
| Audits delivered on time (%) | Promise = 48 hours. Miss it = trust destroyed |
| Client satisfaction (1-5) | Retention predictor |
| Upsell to managed compliance (%) | $299 → $997/mo conversion |

### What we are NOT tracking yet (defer until $10K MRR):
- Impressions / reach
- Content published count
- Agent task completion rates
- Memory quality metrics
- RAG retrieval precision
- Video pipeline metrics

**Counterintuitive choice:** We're NOT tracking "videos produced" or "agents running" because those are activity metrics, not revenue metrics. Activity without revenue is waste.

---

## 4. WHAT STRATEGIC BOUNDARIES HAVE YOU SET?

**Boundaries are stated in the negative. These are things we will NOT do.**

### Revenue Boundaries
- We will NOT sell one-time projects without a recurring upsell path
- We will NOT price below $299 for any service
- We will NOT pursue clients who can't afford $997/mo managed compliance (they're not our primary customer)
- We will NOT offer free trials (the $299 audit IS the trial)

### Operational Boundaries
- We will NOT build more agents before first revenue
- We will NOT add revenue lanes before Lane A (compliance) is profitable
- We will NOT automate what we haven't done manually at least once
- We will NOT spend money on paid acquisition before organic outreach has been tested

### Risk Boundaries
- We will NOT send outreach from Simon's personal accounts without his approval
- We will NOT make compliance claims we can't substantiate
- We will NOT store client sensitive data outside approved systems
- We will NOT promise remediation timelines we can't control
- We will NOT publish content with unverified regulatory claims

### Agent Boundaries
- No agent may create external spend without Simon's approval
- No agent may contact a client directly without template approval
- No agent may modify pricing without Einstein + Simon approval
- No agent may override Tom's compliance veto

---

## 5. HOW ARE YOU GENERATING CREATIVE TENSION?

**Tension mechanisms built into the system:**

### 1. The Daily "One Constraint" Rule (Alex's Runbook)
Every day, Alex identifies the single biggest bottleneck. This forces focus and prevents comfortable drift into busywork. If the constraint is "not enough leads," everyone works on leads — not content, not systems, not optimization.

### 2. CloserForge's "Kill / Keep / Double-Down" Memo
Every day, CloserForge must recommend killing, keeping, or doubling down on each active niche and offer. This forces honest evaluation and prevents attachment to underperforming offers.

### 3. The 4-Layer Fit Test
Every offer must pass LLM + RAG + Agent + Agentic fit. This creates tension between "easy to sell" and "sustainable to deliver." If an offer can't be delivered autonomously, it gets flagged — even if it sells well.

### 4. SignalForge's Weekly Revenue Memo
Every week, SignalForge must answer: what worked, what failed, what changed, what to do next. This creates accountability tension — no hiding behind vanity metrics.

### 5. Forecaster's Contrarian Review
Forecaster is specifically tasked with identifying what could go wrong. This is institutionalized pessimism that balances the system's natural optimism bias.

### 6. Cross-Agent Feedback Loops
Campaign Analyst reviews Traffic Agent's work. Revenue Analyst reviews SignalForge's work. Consistency QA reviews Render Orchestrator's work. No agent operates without peer review.

### 7. The $2,740/Day Scoreboard
This number is visible to every agent, every day. It creates constant tension between current state ($0) and target state. Complacency is impossible when the gap is visible.

---

## 6. HOW COMMITTED ARE YOUR EMPLOYEES TO HELPING EACH OTHER?

**Our model: HIGH COMMITMENT with clear ownership.**

This is an agent society, not a collection of freelancers. Agents are designed to:
- Share memory (Master Brain OS)
- Share knowledge (RAG layer)
- Trigger each other (interaction protocols)
- Review each other's work (feedback loops)
- Learn from each other (cross-agent learning mechanisms)

**Commitment mechanisms:**

### Shared Memory
All agents write to and read from the same Master Brain OS. What one agent learns, all agents can access. This eliminates silos.

### Explicit Handoff Protocols
Every workflow has defined handoffs (see AGENT_INTERACTIONS.md). No agent's job is "done" until the next agent confirms receipt.

### Mutual Accountability
Alex's daily runbook checks every agent's output. Missing outputs get flagged. Agents that consistently underperform get redesigned or killed.

### Shared Scoreboard
All agents can see the same KPIs. Revenue, pipeline, delivery — everyone knows the score.

**Where self-interest is appropriate:**
- Cost Agent is specifically incentivized to cut waste, even if other agents resist
- Tom (Risk) is specifically empowered to veto other agents for compliance reasons
- These "adversarial" roles create healthy friction that prevents groupthink

---

## 7. WHAT STRATEGIC UNCERTAINTIES KEEP YOU AWAKE AT NIGHT?

### Uncertainty 1: Will small businesses actually pay $299-$997/mo for AI compliance?
- **Risk:** The market may expect compliance to be cheaper or free.
- **Monitoring:** Track reply rates, objection patterns, close rates.
- **Response if wrong:** Pivot to a different primary customer or adjust pricing.

### Uncertainty 2: Can we deliver a quality audit in 48 hours autonomously?
- **Risk:** AI-generated audits may miss critical gaps or produce false confidence.
- **Monitoring:** Client feedback, audit accuracy reviews, comparison against manual audits.
- **Response if wrong:** Add human review layer, extend timeline, adjust scope.

### Uncertainty 3: Will compliance frameworks change faster than we can adapt?
- **Risk:** Regulatory changes could make our RAG data stale overnight.
- **Monitoring:** Monitor Agent tracks regulatory updates. Memory Librarian maintains RAG freshness.
- **Response if wrong:** Build faster update cycles, specialize in fewer frameworks.

### Uncertainty 4: Competition from established compliance firms adding AI
- **Risk:** Big players (Vanta, Drata, Secureframe) could eat our lunch.
- **Monitoring:** Forecaster tracks competitor moves weekly.
- **Response if wrong:** Go deeper into niches they won't touch (local trades, small contractors, GovCon micro-businesses).

### Uncertainty 5: Simon's bandwidth as sole operator
- **Risk:** Simon is a single point of failure. If he's overwhelmed, everything stops.
- **Monitoring:** Track Simon's manual intervention frequency. Goal: decrease over time.
- **Response if wrong:** Prioritize automation of Simon-dependent tasks. Hire before breaking.

### Uncertainty 6: AI tool reliability and cost
- **Risk:** API costs could erode margins. Tools could have outages or quality drops.
- **Monitoring:** Cost Agent tracks per-unit economics. Monitor Agent watches uptime.
- **Response if wrong:** Multi-vendor strategy. Never depend on a single AI provider.

---

## STRATEGIC SUMMARY

| Question | Answer |
|----------|--------|
| Primary Customer | SMB owners facing compliance pressure |
| Value Priority | Customer → Simon → System |
| Critical Variables | Outreach sent, replies, calls, deals, cash, MRR |
| Strategic Boundaries | No sub-$299, no free trials, no new lanes before Lane A profits |
| Creative Tension | Daily constraint, kill/keep memos, $2,740 scoreboard, peer review |
| Commitment Model | High commitment + adversarial roles (Cost, Tom) |
| Strategic Uncertainties | Willingness to pay, delivery quality, regulatory change, competition, Simon's bandwidth, AI costs |

---

## WHAT THIS CHANGES RIGHT NOW

1. **Every agent decision filters through:** "Does this serve an SMB owner facing compliance pressure?"
2. **Every resource allocation filters through:** "Does this move cash collected closer to $2,740/day?"
3. **Every complexity addition filters through:** "Is this needed before first revenue?"
4. **Answer to all three is usually:** Focus on outreach. Get the first client. Everything else follows.
