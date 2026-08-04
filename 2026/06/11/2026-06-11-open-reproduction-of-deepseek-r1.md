# Open Reproduction of DeepSeek-R1

- Score: 244 | [HN](https://news.ycombinator.com/item?id=48489917) | Link: https://github.com/huggingface/open-r1

### TL;DR

Hugging Face’s Open R1 repository provides training, synthetic-data, and evaluation tooling intended to reconstruct DeepSeek-R1’s missing pipeline. Its completed first phase released 350,000 verified reasoning traces and a 7B distilled model whose benchmark results broadly match DeepSeek’s Qwen-7B distillation. The harder goals—recreating R1-Zero’s pure reinforcement-learning pipeline and a full base-to-RL multistage run—remain unfinished, with the latest listed milestone from May 2025. Hacker News therefore challenged its fully open reproduction label, criticized hand-waved dataset curation and simplistic validation, and pointed to OLMo, Nemotron, and OpenThoughts as stronger transparency references.

### Comment pulse

- The label overpromises → only distillation finished; pure RL and full multistage reproduction remain roadmap items more than a year later.

- Data is the missing specification → commenters said large-scale reasoning-corpus curation remains hand-waved, while exact-output validation cannot establish semantic correctness.

- Openness needs independent execution → OLMo earned praise for disclosing more of its pipeline and receiving an external reproduction; Nemotron and OpenThoughts offered alternatives.

### LLM perspective

- **View:** Reproducibility is graded: matching outputs through distillation offers less causal knowledge than rebuilding training from base weights.

- **Impact:** Teams gain reusable SFT, GRPO, evaluation, and sandbox tooling, though reference recipes assume expensive GPU clusters.

- **Watch next:** Complete Steps 2–3, strengthen validators, publish training logs and compute accounting, then seek independent reruns.
