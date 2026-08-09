# Flash-MoE: Running a 397B Parameter Model on a Laptop

- Score: 290 | [HN](https://news.ycombinator.com/item?id=47476422) | Link: https://github.com/danveloper/flash-moe

### TL;DR

Flash-MoE streams Qwen3.5-397B-A17B expert weights from an M3 Max MacBook’s SSD, keeping fixed weights and scratch near 6GB while activating four routed experts plus a shared expert per layer. Its 4-bit configuration claims 4.36 tokens per second with reliable tool calling; a 2-bit path reaches 5.74 tokens per second but corrupts JSON. Hand-tuned Metal kernels, packed reads, deferred GPU work, Accelerate BLAS, and the macOS page cache beat elaborate caching and prefetching experiments. HN readers applauded offline inference but disputed quality, particularly low-bit quantization and an alleged expert-count reduction.

### Comment pulse

- Headline skepticism centered on quality → commenters argued 2-bit quantization and fewer active experts make the result unlike standard deployment.
- The project’s own 4-bit result answers part of that critique → it reports better output and tool calling, but at 4.36 tokens/second.
- Alternative local setups exist → one reader reported about 20 tokens/second on a 128GB M1 Ultra using a 2.5-BPW quant.

### LLM perspective

- **View:** The systems contribution is SSD-streamed sparse inference, not proof that parameter count alone predicts usable quality.
- **Impact:** 48GB Apple Silicon owners gain an offline path, accepting slow generation, heavy storage reads, and setup complexity.
- **Watch next:** Independent long-context evaluations, power and SSD-endurance measurements, reproducible quality tests, and expert-routing comparisons.
