# He asked AI to count carbs 27000 times. It couldn't give the same answer twice

- Score: 233 | [HN](https://news.ycombinator.com/item?id=47947490) | Link: https://www.diabettech.com/i-asked-ai-to-count-my-carbs-27000-times-it-couldnt-give-me-the-same-answer-twice/

### TL;DR

A preprint tested four multimodal models by submitting 13 meal photographs 26,904 times at their lowest randomness settings. Every model varied its carbohydrate estimates, sometimes enough to imply dangerous insulin-dose swings; Gemini 2.5 Pro’s paella estimates ranged from 55g to 484g. Consistency was not accuracy: three models repeatedly estimated a labeled 40g cheese sandwich near 28g, while GPT-5.4 averaged about 74g. Self-reported confidence poorly tracked correctness. The author concludes generic LLMs should never autonomously calculate insulin doses from food photos.

### Comment pulse

- Critics call photo-only estimation ill-posed because hidden ingredients are unavailable — counterpoint: consumer apps already market exactly this workflow.
- Several readers wanted a human baseline, while the author emphasizes that within-model spread makes any single unseen draw risky.
- Others proposed grounding with labels or databases; the experiment instead used a production-style prompt adapted from iAPS.

### LLM perspective

- Medical apps should treat vision estimates as suggestions requiring human verification, never direct dosing inputs.
- Calibration must measure systematic error and tail risk across repeated identical queries.
- Interfaces should surface uncertainty distributions and ingredient assumptions instead of one confident number.
