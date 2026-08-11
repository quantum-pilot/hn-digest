# Unsloth Dynamic 2.0 GGUFs

- Score: 193 | [HN](https://news.ycombinator.com/item?id=47192505) | Link: https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs

### TL;DR

Unsloth's updated quantization chooses formats separately for each model and layer, works across dense and mixture-of-experts architectures, and uses a curated calibration set exceeding 1.5 million tokens. The team claims better size-quality tradeoffs than standard imatrix and some QAT releases on MMLU, Aider and KL divergence, while documenting how templates and tokenization can distort benchmarks. GGUF files run in common local engines. Hacker News focused on Qwen3.5 speed and memory configurations, larger low-bit versus smaller high-bit models, and confusion caused by submitting an older overview page for a newer update.

### Comment pulse

- Larger low-bit models often win → one reader's rule was to favor scale when the quantization process is sound.
- Hardware reports need full configuration → VRAM, system RAM, context length, engine and offloading determine fit and throughput.
- The submission looked stale → Qwen3.5 benchmarks were new, but the linked overview and old comments obscured that update.

### LLM perspective

- **View:** Model-specific layer sensitivity is more credible than applying one quantization recipe uniformly.
- **Impact:** Better compression expands useful local inference on consumer GPUs and Apple or ARM systems.
- **Watch next:** Independent reproductions across tasks, engines, context lengths and equal-size baselines.
