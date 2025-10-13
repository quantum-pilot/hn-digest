# AdapTive-LeArning Speculator System (ATLAS): Faster LLM inference

- Score: 189 | [HN](https://news.ycombinator.com/item?id=45556474) | Link: https://www.together.ai/blog/adaptive-learning-speculator-system-atlas

- TL;DR
  - Together AI’s ATLAS adds an online-learning speculator alongside a static one, with a confidence controller that adapts lookahead in real time. Result: up to ~4× faster decoding (DeepSeek-V3.1 105→501 TPS; Kimi-K2 ~460 TPS on B200), with outsized gains on narrow workloads and >60% RL rollout time reduction as acceptance rises during training. HN debates quality (verification should preserve fidelity), clarifies why verification can be faster (compute vs memory), and questions adaptation details and whether speedups lower prices.

- Comment pulse
  - Quality degraded on Kimi tests → Together shows many tool-call failures; likely API/sampler differences, not speculation — counterpoint: verification should retain base-model output distribution.
  - How is verification faster? → Prefill is compute-bound, decoding is memory-bound; small draft guesses, big model verifies tokens in one pass; analogous to branch prediction.
  - Will 4× speed cut prices? → Lower latency and rollout time help, but per-token pricing hinges on margins, hardware utilization, and demand, not speed alone.

- LLM perspective
  - View: Adaptive, confidence-controlled dual speculators are practical: performance compounds with quantization and kernel work; benefits grow as traffic stabilizes.
  - Impact: Inference providers, RL labs, and latency-sensitive apps gain throughput; custom endpoints see sustained gains on narrow domains.
  - Watch next: Open benchmarks of acceptance over time, disclose adaptation method (e.g., LoRA), pricing impacts, and GPU utilization under mixed, shifting workloads.
