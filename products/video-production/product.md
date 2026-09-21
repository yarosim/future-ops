# AI Video Production Pipeline — Revenue Lane F

## Overview
Autonomous long-form AI video production using a disciplined agentic pipeline.
NOT "one-click movie studio." This is a production ops wrapper around AI video tools (Cinemation, Kling, Runway, etc.) that solves the real problem: consistency and quality across longer sequences.

## Why This Fits the 4-Layer Stack

### LLM Layer
- Script generation, narration, dialogue, scene beat writing
- Thumbnail copy, title/description optimization
- Character bible generation from concept prompts

### RAG Layer
- Character bibles (locked identity, wardrobe, voice, reference assets)
- Style guides per channel/brand
- Niche research database (what works, what doesn't)
- Shot prompt templates that maintain consistency
- Past performance data (which formats/niches convert)

### AI Agent Layer
- 8 specialized execution agents (see below)
- Each handles a discrete production step with clear inputs/outputs
- Tool integration: video gen APIs, TTS, music libraries, editing tools, YouTube API

### Agentic AI Layer
- Alex orchestrates the full pipeline
- Forecaster identifies trending niches and optimal publish timing
- Productizer packages successful formats into repeatable templates
- Memory Librarian maintains character bibles and style consistency across projects

## The 8-Agent Pipeline

### 1. Trend/Niche Scout (trend-scout)
Finds high-demand niches, story formats, trending topics.
- Input: market signals, YouTube trends, competitor analysis
- Output: niche-brief.md with topic, audience, estimated demand

### 2. Script Architect (script-architect)
Converts topic into full production script.
- Input: niche-brief.md
- Output: script.md (outline, narration, dialogue, scene beats, timing)

### 3. Character Bible Agent (character-bible)
Locks character identity for consistency across all scenes.
- Input: script.md character requirements
- Output: character-bible.md (identity, style, wardrobe, voice, reference images)
- CRITICAL: This is the consistency anchor. Drift prevention starts here.

### 4. Storyboard / Shotlist Agent (storyboard)
Converts script into shot-by-shot production plan.
- Input: script.md + character-bible.md
- Output: shotlist.md (per-shot prompts, camera directions, reference images, scene continuity notes)

### 5. Render Orchestrator (render-orchestrator)
Manages batch rendering through video generation tools.
- Input: shotlist.md + character references
- Output: raw clips (versioned), render-log.md (credits used, retries, failures)
- Handles: batching, credit tracking, retry logic, output versioning

### 6. Consistency QA Agent (consistency-qa)
Reviews rendered clips for drift and quality issues.
- Input: raw clips + character-bible.md + shotlist.md
- Output: qa-report.md (face drift, clothing drift, background mismatch, pacing issues, subtitle sync)
- Action: flags clips for re-render or manual review

### 7. Editor / Assembly Agent (editor-assembly)
Stitches approved clips into final video.
- Input: approved clips + script.md (narration/timing) + music/SFX assets
- Output: final-video.mp4, thumbnail.png, captions.srt, metadata.json

### 8. Publisher Agent (publisher)
Uploads and distributes across platforms.
- Input: final-video.mp4 + metadata.json
- Output: publish-log.md (URLs, scheduled times, platform-specific cuts)
- Handles: YouTube upload, Shorts/Reels repackaging, performance tracking

## Revenue Models

### A. Faceless YouTube Channels (owned)
- Build and operate AI-generated content channels
- Revenue: AdSense + sponsorships + affiliate
- High autonomy, low marginal cost per video after pipeline is proven

### B. Client Video Production (service)
- Sell video production as a subscription to businesses
- Revenue: $2,000-$5,000/mo per client for X videos/month
- Delivery is largely automated via the pipeline

### C. Productized Video Templates (product)
- Package successful formats as sellable templates
- Revenue: one-time + recurring (template updates, new niches)
- Productizer identifies which formats to package

## Key Risk: Consistency
The hardest problem in long AI video is character and scene drift across stitched clips.
Mitigation strategy (per industry best practice):
- Reference images locked in character bible
- Controlled prompts with explicit consistency anchors
- Shot batching (related scenes rendered together)
- QA review pass before assembly
- Assembly workflow with manual override capability

## Trust Note on Cinemation
- cinemationai.org explicitly states it is NOT affiliated with the official Cinemation platform
- Treat its pricing/feature claims as provisional
- Verify capabilities directly inside vendor product before committing
- The pipeline design is tool-agnostic — works with any video gen backend

## Status
- **Phase:** To be developed. Revenue Lane F.
- **Priority:** After core business lanes are generating revenue, unless a quick-win niche is identified.
