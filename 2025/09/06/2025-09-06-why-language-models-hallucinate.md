# Why language models hallucinate

- Score: 275 | [HN](https://news.ycombinator.com/item?id=45147385) | Link: https://openai.com/index/why-language-models-hallucinate/

TL;DR
- OpenAI argues LLM hallucinations persist because training and accuracy-only evaluations reward guessing over expressing uncertainty. They propose uncertainty-aware scoreboards: penalize confident errors over abstentions, reward calibrated “I don’t know,” and report abstention/error/accuracy separately. Next-token pretraining explains why low-frequency facts yield confident fabrications, while structured patterns don’t. HN debates definitions, the language-vs-truth gap, and creative vs factual use cases, with suggestions like negative marking and verification layers. Calibration may be easier than accuracy; smaller models can better know limits.

Comment pulse
- Narrow, operational definition of hallucination → Enables comparing models and targeting uncertainty vs reasoning/causal errors — counterpoint: all outputs are guesses; term misleads.
- Accuracy-only metrics incentivize guessing → Use negative marking and partial credit for abstention; SAT-style penalties cited; timed tests reward probabilistic elimination strategies.
- Models predict language, not truth → Pretraining can’t resolve rare facts; add abstention/verification layers; cognition likely needs checking beyond next-token prediction.

LLM perspective
- View: Shift leaderboards to cost-sensitive scoring: weight errors > abstentions; require calibrated confidence and refusal rates in model cards.
- Impact: Benchmark authors, API providers, and buyers pivot KPIs from accuracy to expected utility/risk, favoring retrieval+verification and tool-use over pure generation.
- Watch next: Standardized uncertainty-aware evals, per-domain calibration studies, confidence APIs, and audits measuring abstention impact on safety, cost, and user satisfaction.
