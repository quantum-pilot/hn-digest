# Qwen 3.8 follows GPT-5.5 Pro reasoning prefills

- Score: 228 | [HN](https://news.ycombinator.com/item?id=49630026) | Link: https://gist.github.com/wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3

### TL;DR

A 45-problem experiment inserted the first 1% of GPT-5.5 Pro reasoning into several open models, then measured overlap between their first 100 answer tokens and the teacher’s visible answer. Qwen3.8 A95B rose 18.18 percentage points overall, including 26.99 points on STEM; other models changed far less. The author says this suggests Qwen learned from GPT-5.5 Pro or a related model. Commenters emphasize that this is suggestive, not proof, because exposed traces or shared training solutions could confound attribution.

### Comment pulse

- Qwen’s conditional convergence is unusual → its unprefilled answers differed, then became much more GPT-like after a tiny reasoning prefix.
- Data contamination remains plausible → Qwen’s release followed publication of recovered traces that could have entered training data.
- Method access is constrained → only model providers can conduct stronger longitudinal analysis using private, complete reasoning traces.

### LLM perspective

- View: The experiment detects behavioral compatibility with a teacher trace, not a documented training-data lineage.
- Impact: Model labs gain a lightweight distillation audit signal, while accusations require stronger controls and provenance evidence.
- Watch next: Expand models and private puzzles, vary teachers and prefix lengths, and test contamination-resistant datasets.
