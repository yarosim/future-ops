# Consistency QA Checklist

## Purpose
Standard checklist for Consistency QA Agent to evaluate every rendered clip before assembly.

---

## Per-Clip Checks

### 1. Character Consistency
- [ ] Face matches character bible reference? (structure, features, proportions)
- [ ] Hair color and style match?
- [ ] Skin tone consistent?
- [ ] Eye color correct?
- [ ] Age appearance consistent?
- [ ] Body type/build consistent?

### 2. Wardrobe Consistency
- [ ] Clothing matches character bible for this scene?
- [ ] Colors accurate?
- [ ] Accessories present and correct?
- [ ] No random wardrobe changes mid-scene?

### 3. Background/Setting Consistency
- [ ] Location matches shotlist description?
- [ ] Background elements consistent between shots in same scene?
- [ ] No random objects appearing/disappearing?
- [ ] Time of day consistent within scene?

### 4. Lighting Consistency
- [ ] Light direction consistent between shots in same scene?
- [ ] Color temperature consistent?
- [ ] Shadow direction consistent?
- [ ] No sudden brightness/darkness shifts?

### 5. Style Consistency
- [ ] Art style matches project style guide?
- [ ] Color grading consistent?
- [ ] Level of detail consistent?
- [ ] No sudden shifts between realistic/stylized?

### 6. Technical Quality
- [ ] No visible artifacts or glitches?
- [ ] Resolution meets minimum standard?
- [ ] No unnatural distortions (hands, faces, text)?
- [ ] Motion is smooth and natural?

### 7. Continuity Between Shots
- [ ] Character position makes sense from previous shot?
- [ ] Props in correct position?
- [ ] Emotional expression matches narrative beat?
- [ ] Camera angle transition is logical?

### 8. Pacing
- [ ] Clip duration matches script timing?
- [ ] Action pacing matches intended mood?
- [ ] No dead frames or unnecessary pauses?

## Scoring

| Score | Meaning | Action |
|-------|---------|--------|
| PASS | Meets all criteria | → Editor/Assembly |
| MINOR_ISSUE | 1-2 small issues that won't break viewer experience | → Editor can fix in post |
| RE-RENDER | Significant drift or quality failure | → Back to Render Orchestrator with notes |

## Escalation Triggers
- > 30% clips need RE-RENDER → escalate to Alex for project review
- Character face completely wrong → halt rendering, review Character Bible
- Consistent background issues → review Storyboard prompts
- Repeated same failure → flag to Memory Librarian for procedural update
