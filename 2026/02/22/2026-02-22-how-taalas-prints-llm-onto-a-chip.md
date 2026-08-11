# How Taalas “prints” LLM onto a chip?

- Score: 389 | [HN](https://news.ycombinator.com/item?id=47103661) | Link: https://www.anuragk.com/blog/posts/Taalas.html

### TL;DR

The explainer describes Taalas’s fixed-function ASIC for a 3/6-bit-quantized Llama 3.1 8B model, reported at 17,000 tokens per second. Instead of repeatedly fetching weights from external high-bandwidth memory, model weights are encoded into chip logic and activations stream through pipelined layers; on-chip SRAM holds KV cache and LoRA adapters. Taalas claims roughly tenfold speed, energy, and ownership-cost advantages. HN found the structured-ASIC approach plausible but emphasized inflexibility, model-obsolescence risk, prefill latency, and the absence of broader latency evidence.

### Comment pulse

- Hardwiring attacks the memory wall → extreme specialization plausibly trades programmability for speed and power efficiency.
- Local inference could cut network delay and improve control → counterpoint: long-context prefill still requires substantial compute before generation.
- Two-mask customization shortens redesign cycles → two months remains long when models and architectures change rapidly.

### LLM perspective

- **View:** Throughput alone does not establish application latency, quality, utilization, or total economics.
- **Impact:** Stable, high-volume models could move to edge appliances; fast-changing workloads remain better suited to programmable accelerators.
- **Watch next:** Independent power, quality, prefill, first-token, cost, yield, and production-volume measurements.
