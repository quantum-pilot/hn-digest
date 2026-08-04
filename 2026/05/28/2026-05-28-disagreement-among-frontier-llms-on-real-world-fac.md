# Disagreement among frontier LLMs on real-world fact-checks

- Score: 483 | [HN](https://news.ycombinator.com/item?id=48307887) | Link: https://lenz.io/research/llm-disagreement

### TL;DR

Lenz gave 1,000 recent user-submitted claims to GPT-5.4, Claude Opus 4.7, Gemini 3 Pro with and without search, and Sonar Pro, forcing one of four verdicts without explanations. At least one model differed on 67% of claims; 34% contained a gap of two or more buckets, while only 33% were unanimous. The study explicitly measures label consistency, not accuracy, because it lacks human ground truth. HN argued the headline is inflated by undefined overlapping labels, no abstain option, forced guessing on post-cutoff facts, retrieval nondeterminism, and missing within-model variance.

### Comment pulse

- The rubric is underdefined → True, Mostly True, Misleading, and False can overlap semantically, so label differences need not reflect factual disagreement.
- Forced choice creates artificial errors → parametric models must guess recent or unknowable claims because Unknown and Cannot Verify are unavailable.
- The result still has value → critics rejected it as a fact-check benchmark — counterpoint: others saw a useful catalog of common evaluation-design failures.

### LLM perspective

- **View:** Disagreement is diagnostic, but translating it into model error requires a clear rubric, repeated runs, and adjudicated labels.
- **Impact:** Production fact-checking should expose uncertainty and evidence, not collapse ambiguous claims into a mandatory categorical verdict.
- **Watch next:** Human-labeled follow-up, abstention baselines, per-model reruns, retrieval audits, rubric examples, and accuracy stratified by domain and recency.
