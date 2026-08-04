# Bonsai 27B: A 27B-Class model that runs on a phone

- Score: 373 | [HN](https://news.ycombinator.com/item?id=48910545) | Link: https://prismml.com/news/bonsai-27b

### TL;DR

PrismML compressed Qwen3.6 27B into two Apache-2.0 Bonsai variants: a 5.9GB ternary model at 1.71 effective bits per weight and a 3.9GB binary model at 1.125 bits, small enough for an iPhone 17 Pro’s app memory budget. Both retain multimodal input, 262K context, reasoning, and tool use; PrismML reports 95% and 90% of full-precision aggregate benchmark performance, respectively. HN welcomed the density leap but questioned comparison fairness, weaker vision and tool calling, mundane demos, and launch-day runtime failures, calling for independent task-specific tests.

### Comment pulse

- Gemma 4 12B became the desired baseline → its roughly 7GB QAT build may trade stronger vision and tools for weaker math and coding.
- Benchmark retention drew skepticism → readers asked whether fine-tuning favoured the suite and wanted comparisons against equally sized recent models.
- Software support lagged weights → official GGUF and MLX downloads failed in LM Studio; custom forks appeared necessary during launch.

### LLM perspective

- **View:** Footprint is a breakthrough only if quality holds on workflows sensitive to multi-step error accumulation.
- **Impact:** Private offline agents become feasible on phones, but app integration—not downloadable weights—determines near-term usefulness.
- **Watch next:** Measure uncached phone speed, KV-cache memory, battery drain, long-context quality, and mainline runtime compatibility.
