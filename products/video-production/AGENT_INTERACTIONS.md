# AI Video Production Pipeline — Full Agent Interaction Protocol

## Pipeline Flow Diagram

```
[Trend Scout] → [Script Architect] → [Character Bible] → [Storyboard]
                                                              ↓
[Publisher] ← [Editor/Assembly] ← [Consistency QA] ← [Render Orchestrator]
     ↓
[Revenue Analyst / Campaign Analyst] → feedback loop → [Trend Scout]
```

---

## STAGE 1: Opportunity Discovery

### Who: Trend/Niche Scout
### Trigger: Daily cron OR Alex command brief
### Input:
- YouTube trending data
- Competitor channel analysis
- Search intent signals (Google Trends, keyword tools)
- Past performance data from Revenue Analyst
- Niche scoring from CloserForge (if cross-selling)

### Process:
1. Scan trending topics in target verticals (faceless channels, explainers, storytelling)
2. Score niches using CloserForge's profit_score formula
3. Identify 3 highest-potential video concepts per day
4. Check RAG for existing character bibles and templates that could be reused

### Output:
- `outputs/YYYY-MM-DD_trend-scout_discovery_v1/niche-brief.md`
- Contains: topic, target audience, estimated demand, suggested format, monetization angle

### Handoff:
- `sessions_send` → Script Architect with niche-brief.md path
- `sessions_send` → Alex with daily discovery summary
- Write to Master Brain OS: `episodic` namespace (what was found today)

---

## STAGE 2: Script Creation

### Who: Script Architect
### Trigger: Receives niche-brief.md from Trend Scout via sessions_send
### Input:
- niche-brief.md from Trend Scout
- RAG: style guides, successful script patterns, brand voice
- Master Brain OS: procedural memory (proven script structures)
- Existing character bibles (if reusing characters)

### Process:
1. Parse niche-brief for topic, audience, format
2. Query RAG for relevant templates and past successful scripts
3. Generate full script: outline → narration → dialogue → scene beats → timing
4. Include character requirements (new or existing)
5. Include visual direction notes per scene

### Output:
- `outputs/YYYY-MM-DD_script-architect_[topic]_v1/script.md`
- Contains: title, outline, full narration, dialogue, scene beats with timing, character list, visual notes

### Handoff:
- `sessions_send` → Character Bible Agent with script.md path + character requirements
- Write to Master Brain OS: `procedural` (if new script structure worked well)

---

## STAGE 3: Character Locking

### Who: Character Bible Agent
### Trigger: Receives script.md from Script Architect via sessions_send
### Input:
- script.md character requirements
- RAG: existing character bibles (reuse if possible)
- Reference image assets
- Style guide from RAG

### Process:
1. Check if characters already exist in character bible library
2. If new: generate full character profile (identity, appearance, wardrobe, voice, mannerisms)
3. Generate or source reference images for each character
4. Lock consistency anchors: face structure, clothing palette, background style
5. Create voice direction notes (for TTS/narration)

### Output:
- `outputs/YYYY-MM-DD_character-bible_[project]_v1/character-bible.md`
- Contains: per-character profile, reference images, voice notes, consistency rules
- Reference images saved to `assets/characters/[character-name]/`

### Handoff:
- `sessions_send` → Storyboard Agent with script.md + character-bible.md paths
- Write to RAG: character bibles for reuse across future projects
- Write to Master Brain OS: `semantic` (character design patterns that work)

### CRITICAL GATE:
Character Bible must be APPROVED before Storyboard proceeds.
If client project: `sessions_send` → Alex for client approval.
If owned channel: auto-approve if reusing existing characters.

---

## STAGE 4: Shot Planning

### Who: Storyboard / Shotlist Agent
### Trigger: Receives script.md + character-bible.md from Character Bible Agent
### Input:
- script.md (scene beats, timing, visual notes)
- character-bible.md (reference images, consistency rules)
- RAG: shot prompt templates, camera direction library
- Master Brain OS: procedural (past successful prompts)

### Process:
1. Break each scene into individual shots
2. Generate per-shot AI video prompts with:
   - Character references (locked from bible)
   - Scene description with continuity anchors
   - Camera angle and movement
   - Lighting and mood
   - Props and background
3. Group shots by scene for batch rendering (related scenes together)
4. Add continuity notes between shots

### Output:
- `outputs/YYYY-MM-DD_storyboard_[project]_v1/shotlist.md`
- Contains: numbered shots, per-shot prompts, camera directions, continuity notes, batch groupings
- `outputs/YYYY-MM-DD_storyboard_[project]_v1/batch_plan.md` (rendering order)

### Handoff:
- `sessions_send` → Render Orchestrator with shotlist.md + batch_plan.md + character references
- Write to Master Brain OS: `procedural` (prompt patterns that maintain consistency)

---

## STAGE 5: Rendering

### Who: Render Orchestrator
### Trigger: Receives shotlist.md + batch_plan.md from Storyboard Agent
### Input:
- shotlist.md (per-shot prompts)
- batch_plan.md (rendering order)
- Character reference images
- API credentials for video generation tool (Cinemation, Kling, Runway, etc.)

### Process:
1. Check API credit balance — if low, alert Alex + Cost agent
2. Submit batches in order (related scenes together for consistency)
3. Track each render: status, duration, credits consumed, retries
4. On failure: retry up to 3x, then flag for manual review
5. Version all outputs: v1, v2, etc.
6. Save raw clips with metadata (shot number, scene, character, take number)

### Output:
- `outputs/YYYY-MM-DD_render_[project]_v1/clips/` (raw rendered clips)
- `outputs/YYYY-MM-DD_render_[project]_v1/render-log.md` (credits, retries, failures, timing)

### Handoff:
- `sessions_send` → Consistency QA Agent with clips path + character-bible.md + shotlist.md
- `sessions_send` → Cost Agent with render-log.md (credit usage tracking)
- Write to Master Brain OS: `episodic` (render costs, failure patterns)

### COST GATE:
If credits consumed > budget threshold:
- `sessions_send` → Alex + Atlas for approval to continue
- Pause remaining batches until approved

---

## STAGE 6: Quality Assurance

### Who: Consistency QA Agent
### Trigger: Receives rendered clips from Render Orchestrator
### Input:
- Raw rendered clips
- character-bible.md (comparison reference)
- shotlist.md (expected output per shot)
- QA checklist from RAG

### Process:
1. Compare each clip against character bible:
   - Face consistency check
   - Clothing/wardrobe check
   - Background/setting check
   - Style/mood check
2. Check scene continuity between consecutive shots
3. Check pacing against script timing
4. Check for artifacts, glitches, or quality issues
5. Score each clip: PASS / MINOR_ISSUE / RE-RENDER
6. For RE-RENDER: send back to Render Orchestrator with specific notes

### Output:
- `outputs/YYYY-MM-DD_qa_[project]_v1/qa-report.md`
- Contains: per-clip scores, issues found, re-render requests, approved clips list

### Handoff:
- If clips PASS: `sessions_send` → Editor/Assembly Agent with approved clips list
- If RE-RENDER needed: `sessions_send` → Render Orchestrator with re-render requests + notes
- Write to Master Brain OS: `episodic` (common drift patterns), `procedural` (QA improvements)

### QUALITY GATE:
No clip proceeds to assembly without QA pass.
If > 30% clips need re-render: escalate to Alex for project review.

---

## STAGE 7: Assembly

### Who: Editor / Assembly Agent
### Trigger: Receives approved clips from Consistency QA Agent
### Input:
- Approved clips
- script.md (narration/timing)
- Music/SFX assets from RAG library
- Caption/subtitle requirements
- Thumbnail requirements
- Platform-specific format requirements

### Process:
1. Stitch clips in script order
2. Add narration audio (TTS or recorded)
3. Add background music and sound effects
4. Generate and sync captions/subtitles
5. Create thumbnail (AI-generated or templated)
6. Add intro/outro if applicable
7. Export in platform-specific formats:
   - YouTube (16:9, full length)
   - Shorts/Reels (9:16, clips)
   - Social clips (square, 60s highlights)
8. Generate metadata: title, description, tags, timestamps

### Output:
- `outputs/YYYY-MM-DD_assembly_[project]_v1/final-video.mp4`
- `outputs/YYYY-MM-DD_assembly_[project]_v1/shorts/` (platform clips)
- `outputs/YYYY-MM-DD_assembly_[project]_v1/thumbnail.png`
- `outputs/YYYY-MM-DD_assembly_[project]_v1/captions.srt`
- `outputs/YYYY-MM-DD_assembly_[project]_v1/metadata.json`

### Handoff:
- `sessions_send` → Publisher Agent with final assets
- If client project: `sessions_send` → Alex for client approval before publish
- Write to Master Brain OS: `procedural` (assembly workflow improvements)

### APPROVAL GATE (client projects only):
Client must approve final video before publishing.
Alex coordinates approval via Correspondence agent.

---

## STAGE 8: Publishing & Distribution

### Who: Publisher Agent
### Trigger: Receives final assets from Editor/Assembly Agent (+ approval if client)
### Input:
- Final video + shorts + thumbnail + captions + metadata
- Publishing schedule (from Alex or content calendar)
- Platform API credentials

### Process:
1. Upload to YouTube with optimized metadata
2. Schedule publish time (based on audience data)
3. Create and upload Shorts/Reels versions
4. Create social media promotional posts
5. Log all publish URLs and timestamps
6. Set up performance tracking for first 24h / 48h / 7d

### Output:
- `outputs/YYYY-MM-DD_publisher_[project]_v1/publish-log.md`
- Contains: URLs, scheduled times, platform-specific details, tracking setup

### Handoff:
- `sessions_send` → Campaign Analyst with publish-log.md (start tracking)
- `sessions_send` → Traffic Agent (promote across channels)
- `sessions_send` → Billing Agent (if client project: trigger invoice)
- Write to Master Brain OS: `episodic` (publish event), `tactical` (what's live now)

---

## STAGE 9: Performance Tracking & Feedback

### Who: Campaign Analyst + Revenue Analyst (Dex)
### Trigger: 24h / 48h / 7d after publish
### Input:
- YouTube analytics (views, watch time, CTR, subscriber gain)
- Revenue data (AdSense, sponsorships, client payments)
- Engagement data (comments, shares, likes)
- Cost data from Render Orchestrator + Cost Agent

### Process:
1. Pull performance metrics at each interval
2. Calculate ROI: (revenue - production cost) / production cost
3. Identify what worked: hook, topic, format, thumbnail, timing
4. Identify what underperformed and why
5. Compare against past videos for trend analysis

### Output:
- `outputs/YYYY-MM-DD_analyst_[project]_v1/performance-report.md`
- Contains: metrics, ROI, what worked, what didn't, recommendations

### Handoff:
- `sessions_send` → Trend Scout (feed back winning patterns for next discovery cycle)
- `sessions_send` → Alex (revenue impact, strategic decisions)
- `sessions_send` → Einstein (if offer/pricing adjustments needed for client packages)
- Write to Master Brain OS: `semantic` (what content patterns work), `episodic` (this video's results)

### FEEDBACK LOOP CLOSES HERE:
Performance data feeds directly into Stage 1 (Trend Scout) for the next cycle.
This is how the system learns and improves autonomously.

---

## CROSS-AGENT LEARNING MECHANISMS

### After Every Completed Video:
1. **Script Architect** reviews performance → updates script templates in procedural memory
2. **Character Bible Agent** reviews drift reports → tightens consistency rules
3. **Storyboard Agent** reviews which prompts maintained consistency → updates prompt library
4. **Render Orchestrator** reviews cost/quality tradeoffs → optimizes batch strategies
5. **Consistency QA** reviews re-render rates → refines QA checklist
6. **Editor/Assembly** reviews engagement data → adjusts pacing, music, caption style
7. **Publisher** reviews platform-specific performance → updates metadata templates

### Weekly R&D Review (Alex-led):
- What new tools/models should we test?
- What video formats are emerging?
- What niches are growing/dying?
- What operational bottlenecks need solving?
- What should be productized and sold as a service?

### Memory Librarian Monthly Audit:
- Clean up stale character bibles
- Archive underperforming video data
- Promote winning patterns to semantic/procedural
- Update RAG with new templates and playbooks

---

## WHERE REVENUE LANDS

### Revenue Stream A: Owned Channels (AdSense + Sponsorships)
- Publisher uploads → YouTube monetization active
- Revenue deposits to: linked AdSense/bank account
- Tracking: Dex monitors daily/weekly AdSense earnings
- Atlas tracks margin (production cost vs ad revenue)

### Revenue Stream B: Client Video Production
- Seller/CloserForge closes client → Billing sends invoice
- Client pays deposit (50% upfront typical) → funds hit payment processor
- Fulfillment delivers video → client approves → Billing sends final invoice
- Deposits to: Stripe/payment processor → linked bank account
- Tracking: Atlas monitors AR aging, Billing handles renewals

### Revenue Stream C: Video Templates (Productized)
- Productizer packages successful formats into templates
- Einstein prices them (one-time or subscription)
- Seller lists on marketplace or direct sales page
- Payment via: Stripe/Gumroad/similar → linked bank account
- Tracking: Billing + Dex monitor sales volume

### Payment Flow:
```
Client/Platform → Payment Processor (Stripe/PayPal/AdSense) → Bank Account
                         ↓
              Billing Agent logs transaction
                         ↓
              Atlas confirms margin
                         ↓
              Alex updates scoreboard
```
