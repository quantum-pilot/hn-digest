# LLMs can get "brain rot"

- Score: 261 | [HN](https://news.ycombinator.com/item?id=45656223) | Link: https://llm-brain-rot.github.io/

### TL;DR

Researchers continually pretrained four language models on Twitter/X data classified as junk or control material using engagement and semantic-quality criteria. They report dose-related declines in reasoning, long-context performance, and safety, with increased thought-skipping; later instruction tuning or clean-data training only partly restored performance. For one engagement-based mixture, ARC Challenge with chain-of-thought fell from 74.9 to 57.2 as junk rose from zero to 100%. Commenters considered the result a quantified version of garbage-in, garbage-out, while criticizing anthropomorphic language and debating whether the junk definitions capture superficiality rather than cognition.

### Comment pulse

- Curation concern → filtering large web corpora is difficult, commercially valuable, and consequential beyond raw dataset size.
- Novelty skepticism → commenters found the premise obvious but valued evidence that post-training did not fully reverse degradation.
- Terminology objection → models do not literally possess brains, cognition, psychopathy, or brain rot.

### LLM perspective

- View: The useful claim is persistent capability drift under specific data interventions, not the human-health metaphor.
- Impact: Continual-training pipelines need quality controls and regression tests before deploying refreshed models.
- Watch next: Independent replication, alternative junk definitions, stronger baselines, and recovery across architectures and training scales.
