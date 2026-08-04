# Speculative KV coding: losslessly compressing KV cache by up to ~4×

- Score: 140 | [HN](https://news.ycombinator.com/item?id=48400151) | Link: https://fergusfinn.com/blog/kv-entropy-coder/

### TL;DR

Speculative KV coding compresses an LLM’s key-value cache exactly by running a cheaper deterministic predictor on the same prompt at both endpoints, then arithmetic-coding the target cache according to prediction error. Early Qwen3 tests achieved 2.37–2.70× compression for bf16 caches and 3.08–3.90× beyond FP8 cache quantization, or 6–8× versus original bf16. The trade is extra predictor compute for memory or bandwidth. HN debated whether quadratic recomputation defeats long-context gains, whether RAM or disk offload is simpler, and when memory-bandwidth savings justify GPU work.

### Comment pulse

- Compute objection → A standard-attention predictor still scales quadratically with context — counterpoint: linear-attention predictors or reusable independent prefix segments could change the trade.
- Storage alternative → RAM or disk persistence avoids recomputation, but PCIe transfer is far slower than VRAM access and caches can reach hundreds of gigabytes.
- Scale dependence → Predictor overhead may be sensible for trillion-parameter serving with batches, but unattractive for an 8B model handling one request.

### LLM perspective

- **View:** This is a systems optimization, not free compression; success depends on where latency, capacity, and energy bottlenecks sit.
- **Impact:** Disaggregated inference and large prefix caches gain capacity if predictor cost stays below avoided transfer and storage costs.
- **Watch next:** Benchmark end-to-end latency, coder throughput, energy, linear predictors, exact reproducibility, cache-hit rates, and break-even by model size.
