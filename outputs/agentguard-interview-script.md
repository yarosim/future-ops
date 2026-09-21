# AgentGuard AI — Validation Interview Script (v1)

**Goal:** Validate the thesis that orgs lack visibility & control over autonomous AI agents, and that an "agent identity/runtime-governance" product is worth building.
**Target:** 10–15 security / GRC / platform practitioners (CISO, AppSec, SecOps, GRC analyst, platform/identity engineer).
**Length per interview:** 25–30 min. Prioritize practitioners who already have >20 agents in production (the shadow-AI comment thread is the richest vein).

---

## A. Recruiting / who to talk to (ranked)

1. **Security practitioners reporting shadow AI** — the 08-19 "shadow AI worse than shadow IT" crowd. The strongest convert candidates.
2. **Platform/DevOps engineers who run agents against APIs** — the "50 agents, hundreds of API calls, no observability" type.
3. **GRC analysts who answered security questionnaires** — aligns w/ VendorShield but surfaces the access/governance overlap.
4. **Identity/SSO & OAuth admins** — they own the "agent identities / permissions" half.
5. **Any org actively rolling out AI agents** (>20) — they've felt the pain of no central inventory.

Ask each: "Name one agent that surprised you — that you didn't know existed or couldn't see what it touched."

---

## THE QUESTIONS (grouped; use as a guide, don't read off robotically)

### A. Inventory & discovery (does the org know what agents exist?)
1. How many AI agents / API-consuming automations does your org run today? Is there any single list or inventory of them?
2. What was the last time an agent appeared in your environment that nobody had intentionally provisioned? How was it found?
3. Where do agents get their credentials and identities — a human's service account, the human's own SSO, or a dedicated agent identity?

### B. Identities & permissions (can they map who can do what?)
4. For a typical agent, can you say exactly which tools, APIs, and internal data sources it can reach? Is that documented, or tribal knowledge?
5. When an agent is created/onboarded, does anyone review what permissions it gets before it starts running? (least privilege or auto-grant?)
6. Do you have a way to see which OAuth grants / service accounts belong to an agent vs. a human? (the "who-actually-is-this" problem)

### C. MCP / tool access (the newest, bleeding-edge gap)
7. Are any of your internal agents hooked into MCP (Model Context Protocol) servers or LLM tools that reach company data?
8. If yes — who permissions those tool connections, and is there logging of which tool call did what?

### D. Observability / attribution (the "why did it do that?" problem)
9. When an agent makes an API call, can you trace WHY it made it — the intent, the request, which run? Or is it a black box?
10. Do you log the tool calls / prompt → action mappings for audit? Could you reconstruct a full agent run 6 months from now?
11. Have you ever needed to answer "which agent touched THIS data / did THIS action?" — how hard was that?

### E. Cost attribution (secondary but real)
12. If you get your LLM/agent spend bill, can you break it down by agent, by department, by customer? Or is it one rolling total?
13. Has an agent ever silently burned budget (loops, runaway tool calls, re-runs)? What happened?

### F. Control & emergency action (the closing & the "kill switch")
14. When you need to stop an agent RIGHT NOW — revoke its access mid-run, kill a capability — can you? How fast, and does it require a human?
15. Do you have an approval gate before an agent takes a consequential action (message a customer, change data, transfer money), or does it just go?
16. *(the money question)* If you had a pane showing every agent, its owner, its credentials, its permissions, its data access, and its live tool activity — with one-click revoke — would you use it weekly? What would make you buy it this quarter?

---

## SCORING / what to listen for

For each interview, score 0–3 per dimension. A validated thesis ≈ avg ≥2 on A–D + F.

| Dimension | Promising | Dead |
|---|---|---|
| **A. No central inventory** | "We have no idea; each team runs their own" | "We have full agent inventory already" |
| **B. Credential sprawl** | agents share human/service creds, no least privilege | all agents have dedicated scoped roles |
| **C. MCP/tool access** | MCP connected w/o perms control | no agents reach internal MCP/tools |
| **D. No attribution** | "can't explain why an agent acted" | full tool-call audit exists & used |
| **E. Cost opacity** | "one rolling LLM bill, can't slice" | per-agent cost attribution exists |
| **F. No kill switch** | "we'd have to find the repo and revoke a token" | emergency revoke is instant & tested |

**Go signal:** ≥3 interviewees describe shadow/discovery pain (A), ≥2 describe NO kill switch (F), and ≥2 describe tool/MCP access without a permission boundary (C). That matches the 08-19 complaint.
**No-go / downgrade signal:** most already have inventory + least-privilege + tool-call audit, or say the conversations is "a vendor problem, not ours."

---

## Interpretation & decision triggers

- **8+ of 15** report both "can't inventory" (A<2) and "can't revoke fast" (F<2) → **development triggers immediately** — proceed to AgentGuard BUILD with those early sales as the seed list.
- **Mixed** (strong discovery pain, weak control pain) → re-position: ship "discovery + inventory + permission map" first, move monitoring/revocation later.
- **Weak** → keep VALIDATE, expand sourcing beyond security to platform/identify engineers before spending build.

## End each interview
- Ask: "Who's the person with a budget line for this? What would make you sign in the next 90 days?"
- Collect quotes with permission. 2–3 verbatim "it's a black box, we don't know what it runs" quotes are your seed marketing copy.

---

## Quick script (this is the backup 5-question version if a call runs short)
1. How does your org discover and inventory the agents that run today? (A)
2. What identities/credentials do agents run as — shared, human, or dedicated? (B)
3. When an agent acts, can you trace WHICH agent did WHAT and WHY? (D)
4. If an agent went rogue right now, how fast do you stop it — and does it need a human? (F)
5. "We build/pay for this" — yes/no and what changes your mind before you budget? (F/$)