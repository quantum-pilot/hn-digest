# Kimi Linear: An Expressive, Efficient Attention Architecture

- Score: 208 | [HN](https://news.ycombinator.com/item?id=45766937) | Link: https://github.com/MoonshotAI/Kimi-Linear

- TL;DR
  - MoonshotAI’s Kimi Linear mixes Kimi Delta Attention (a linear, finite‑state mechanism) with periodic global MLA layers (≈3:1) to cut memory and boost speed for long contexts. It supports up to 1M tokens, reduces KV cache by up to 75%, and reports up to 6× faster decoding while matching or beating full attention on long‑range tasks (e.g., RULER 84.3 with ~4× speedup; MMLU‑Pro 51.0 at 4k). They released 48B checkpoints (~3B activated) and an open KDA kernel; HN debated efficiency vs demand and cloud‑model privacy.

- Comment pulse
  - Hybrid linear attention = mostly linear layers + some global attention → linear state gives O(n) memory; sparse global blocks preserve expressivity.
  - Algorithmic gains avert 'AI datacenter apocalypse' → small models, routing, price cuts show efficiency — counterpoint: Jevons paradox often turns efficiency into higher demand.
  - Assume cloud LLMs can be surveilled → governments can pressure providers; only local or self-hosted inference meaningfully reduces spying risk.

- LLM perspective
  - View: Blending finite-state linear attention with sparse global blocks is becoming the pragmatic path for long contexts.
  - Impact: Inference providers and long-context apps gain throughput and cost reductions; fewer GPUs needed for million-token retrieval, coding, and RL workloads.
  - Watch next: Independent benchmarks beyond RULER, stability at 1M tokens, KV-cache savings in production, and deep integration in vLLM/Transformers.
