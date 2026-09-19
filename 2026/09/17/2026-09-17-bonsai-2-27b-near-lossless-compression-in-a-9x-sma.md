# Bonsai 2 27B: Near-Lossless Compression in a 9x Smaller Footprint

- Score: 563 | [HN](https://news.ycombinator.com/item?id=49746618) | Link: https://prismml.com/news/bonsai-2-27b

### TL;DR

PrismML presents Bonsai 2 27B, a ternary-weight reasoning model packed into 5.9 GB at 1.75 bits per weight, with vision, tool calling, selectable reasoning effort, and a 262K-token context. The team claims 98.2% retention of its FP16 baseline’s benchmark performance, but current formats require PrismML’s llama.cpp fork and careful runtime selection. HN users reported roughly 20–40 generated tokens per second on consumer hardware, yet independent experiments questioned “near-lossless” quality, especially for longer agentic coding tasks.

### Comment pulse

- Extreme compression enables local inference → users ran Bonsai 2 within 8 GB VRAM, while related Bonsai models worked directly in browsers.
- Benchmark retention may overstate usability → testers report competent short outputs but severe degradation on long or agentic workloads.
- Runtime compatibility remains fragile → Bonsai 2 needs fork-specific binaries, correct packing, and platform workarounds until required changes reach upstream.

### LLM perspective

- View: Memory efficiency is demonstrated more clearly than near-lossless task quality.
- Impact: GPU-constrained users gain private local vision and tools, accepting extra setup and uncertain long-horizon reliability.
- Watch next: Compare against standard 2-bit and 4-bit quantizations on independent coding, vision, reasoning, latency, and energy tests.
