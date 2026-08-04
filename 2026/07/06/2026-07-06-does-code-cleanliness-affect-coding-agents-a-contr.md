# Does code cleanliness affect coding agents? A controlled minimal-pair study

- Score: 190 | [HN](https://news.ycombinator.com/item?id=48798815) | Link: https://arxiv.org/abs/2605.20049

### TL;DR

A controlled study varied code cleanliness while holding tasks and Claude Code constant across six behaviorally matched Java/Python repository pairs. In 660 Sonnet 4.6 trials over 33 hidden-test tasks, cleaner code barely changed pass rate (91.3% versus 92.1%) but reduced input tokens 7.1%, output tokens 8.5%, reasoning text 11.1%, messages 7.0%, and post-edit file revisits 33.8%. Benefits concentrated in multi-module work; refactored hotspots sometimes increased navigation. HN found the question credible but challenged AI-generated “clean/messy” pairs and the omission of unrelated regression tests, arguing cost comparisons need equivalent solution quality.

### Comment pulse

- Clean structure should reduce search cost → semantic filenames and smaller modules help agents find relevant code before context fills.
- Measurement quality is the main objection → hidden-task success cannot prove equivalent patches when untouched repository tests were never rerun.
- Synthetic pairs divide readers → analyzer-guided transformations isolate violations — counterpoint: AI-cleaned repositories may not represent genuinely well-designed systems.

### LLM perspective

- **View:** Cleaner code appears to buy coding agents efficiency and confidence, not higher short-horizon task accuracy.
- **Impact:** A 7–8% token reduction could compound materially at scale, but only if patch quality and regressions remain equivalent.
- **Watch next:** Replicate across models, natural repository histories, full test suites, longitudinal maintenance, and cleanliness measures beyond SonarQube violations.
