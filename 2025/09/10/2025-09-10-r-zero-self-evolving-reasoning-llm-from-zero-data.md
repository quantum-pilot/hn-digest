# R-Zero: Self-Evolving Reasoning LLM from Zero Data

- Score: 106 | [HN](https://news.ycombinator.com/item?id=45192194) | Link: https://arxiv.org/abs/2508.05004

### TL;DR

R-Zero proposes co-evolving two models initialized from one base language model: a Challenger generates tasks near the Solver’s capability boundary, while the Solver learns to answer them. Separate rewards are intended to produce an automatically targeted curriculum without a human-curated task set or labels. The paper reports reasoning-benchmark gains across backbones, including improvements for Qwen3-4B-Base. Commenters challenged the phrase “zero data,” noting the substantial pretraining already embedded in the base model and questioning whether external judging or self-generated tasks can remain grounded rather than amplify errors.

### Comment pulse

- Several readers compared the adversarial setup with GANs, while debating what serves as a reliable discriminator or grounding signal.
- The name was criticized for colliding with an earlier DeepSeek model called R-Zero.

### LLM perspective

- View: R-Zero removes curated task data from one stage, not data or external knowledge from the system.
- Impact: Automated curricula could reduce fine-tuning labor, but gains may remain bounded by judge and base-model competence.
- Watch next: Examine ablations, judge dependence, task diversity, contamination controls, and performance after repeated co-evolution cycles.
