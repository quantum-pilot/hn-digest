# Qwen3-Coder-Next

- Score: 550 | [HN](https://news.ycombinator.com/item?id=46872706) | Link: https://qwen.ai/blog?id=qwen3-coder-next

### TL;DR

Qwen3-Coder-Next is an open-weight mixture-of-experts coding model built from Qwen3-Next-80B-A3B-Base, activating 3B parameters per inference. Qwen says executable task synthesis, environment interaction, expert trajectories, distillation and reinforcement learning train it for long-horizon tool use and failure recovery. The team reports over 70% on SWE-Bench Verified with SWE-Agent and competitive efficiency against larger open models, while proprietary models still lead. Early commenters found local quantizations feasible on 28–64GB systems, but several judged real coding quality below the implied Sonnet 4.5 comparison.

### Comment pulse

- Local users reported roughly 17–60 tokens per second across varied hardware, contexts and quantizations, making “usable” highly workload-dependent.
- Enthusiasts praised 3B active parameters; skeptics encountered simple mistakes, thinking loops and performance closer to Haiku than Sonnet.
- Commenters want standardized hardware benchmarks separating speed, memory and total task time from model accuracy.

### LLM perspective

- View: Sparse activation improves inference economics, but total model memory still determines whether “local” deployment is practical.
- Impact: Capable self-hosted coding agents could reduce recurring inference costs and preserve code privacy.
- Watch next: Independent agent evaluations, quantization effects and sustained performance on large repositories rather than toy applications.
