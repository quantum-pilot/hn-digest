# Show HN: Running 104GB Qwen3.8-Flash-Next on 48GB Mac with at ~12 tok/s

- Score: 200 | [HN](https://news.ycombinator.com/item?id=49524447) | Link: https://github.com/carloslfu/slotstream

### TL;DR

Slotstream claims to run a 104 GB, 4-bit mixture-of-experts model on memory-constrained Apple Silicon by keeping a 3.8 GB trunk resident and streaming routed experts from SSD into a shared cache. On one 48 GB M5 Pro, the author measured roughly 12 tokens per second with about 32 GB peak memory; lower-memory figures are simulations, not hardware tests. The project offers a Swift binary and partial Ollama/OpenAI APIs, but long prompts remain slow. Commenters question thermals, documentation quality, context limits, and cloud-model comparability.

### Comment pulse

- Streaming expands local options → SSD-backed expert caching makes oversized sparse models possible without loading every weight into memory.
- Evidence is narrow → only the 48 GB M5 Pro was measured; smaller tiers extrapolate from its curve and slower hardware may differ.
- Local priorities vary → some want larger models, while others prefer more context, better thermals, or smaller active-parameter mixtures.

### LLM perspective

- View: Slotstream demonstrates a workable capacity trade, not a general substitute for fully resident or hosted inference.
- Impact: Apple Silicon owners may test large sparse models while accepting substantial disk, prompt-latency, and hardware constraints.
- Watch next: Reproduce results across Mac tiers, sustained thermals, SSD endurance, context lengths, and real agent workloads.
