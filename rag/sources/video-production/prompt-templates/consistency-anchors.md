# Consistency Anchor Prompt Templates

## Purpose
These templates ensure character and scene consistency across multi-shot AI video generation.
Every prompt sent to a video generation tool MUST use these anchors.

---

## Character Anchor Template

```
[CHARACTER_NAME] is a [AGE]-year-old [GENDER] with [SKIN_TONE] skin,
[HAIR_COLOR] [HAIR_STYLE] hair, [EYE_COLOR] eyes.
Wearing: [SPECIFIC_CLOTHING_DESCRIPTION].
Body type: [BUILD].
Distinguishing features: [FEATURES].
Expression: [CURRENT_EMOTION].
Pose: [CURRENT_ACTION].
Camera: [ANGLE] shot, [DISTANCE].
Lighting: [LIGHTING_STYLE].
Background: [SCENE_DESCRIPTION].
Style: [ART_STYLE], [QUALITY_MODIFIERS].
```

## Scene Continuity Template

```
Scene [NUMBER] of [TOTAL].
Previous shot: [BRIEF_DESCRIPTION_OF_LAST_SHOT].
This shot continues: [CONTINUITY_NOTES].
Same location: [YES/NO — if yes, repeat background exactly].
Same lighting: [YES/NO — if yes, repeat lighting setup].
Same wardrobe: [YES/NO — if yes, repeat clothing exactly].
Time of day: [SAME/CHANGED].
Camera transition: [CUT/PAN/ZOOM from previous].
```

## Batch Grouping Rules

1. **Same scene = same batch.** Render all shots from one scene together.
2. **Same character = prioritize grouping.** Keeps the model's "memory" of the character fresh.
3. **Interiors before exteriors.** Interior scenes have more controllable backgrounds.
4. **Close-ups before wide shots.** Lock the face first, then place in scene.
5. **Max 5-8 shots per batch.** Prevents quality degradation in long batches.

## Anti-Drift Modifiers

Add these to EVERY prompt:
- "consistent with reference image"
- "same character as previous frame"
- "identical wardrobe to scene [X]"
- "matching lighting conditions"
- "photorealistic / [style] consistency"

## Quality Modifiers (append to all prompts)

```
8K resolution, cinematic lighting, sharp focus, detailed textures,
professional color grading, film grain [optional], depth of field [optional]
```
