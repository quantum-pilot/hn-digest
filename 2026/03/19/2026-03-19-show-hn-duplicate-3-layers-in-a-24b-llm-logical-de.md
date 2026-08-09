# Show HN: Duplicate 3 layers in a 24B LLM, logical deduction .22→.76. No training

- Score: 235 | [HN](https://news.ycombinator.com/item?id=47431671) | Link: https://github.com/alainnothere/llm-circuit-finder

### TL;DR

A toolkit applies David Ng’s RYS method by duplicating selected transformer layers in GGUF models without retraining. Repeating Devstral-24B layers 12–14 raised BBH logical-deduction accuracy from 0.22 to 0.76 on 50 examples and improved several other tasks; repeating Qwen2.5-Coder-32B layers 7–9 boosted a custom reasoning probe from 76.5% to 94.1%. The modification adds roughly 1.5 GiB and 7.5% latency for three Devstral layers. HN found the result plausible but challenged the “reasoning circuit” explanation, small evaluation, novelty, and untested regressions.

### Comment pulse

- Skeptics proposed duplication may disrupt a post-training degradation mechanism rather than rerun an indivisible cognitive unit.
- Defenders pointed to residual connections and shared representation spaces, which make middle layers unusually compatible and iterative.
- Prior experiments span LLMs and image models — counterpoint: this project contributes systematic sweeps and standard benchmark tooling.

### LLM perspective

- **View:** Architecture surgery can alter capability profiles without changing weights, but causal labels remain speculative.
- **Impact:** Local model users gain a cheap search space trading memory and speed for narrow-task gains.
- **Watch next:** Larger held-out evaluations, ablations, cross-model replication, and annealing after surgery.
