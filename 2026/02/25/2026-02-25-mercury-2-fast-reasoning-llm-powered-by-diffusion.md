# Mercury 2: Fast reasoning LLM powered by diffusion

- Score: 337 | [HN](https://news.ycombinator.com/item?id=47144464) | Link: https://www.inceptionlabs.ai/blog/introducing-mercury-2

### TL;DR

Inception launched Mercury 2, a diffusion-based reasoning model that refines multiple tokens in parallel instead of generating strictly one token at a time. The company reports up to 1,009 tokens per second on NVIDIA Blackwell hardware, more than fivefold speed gains, a 128K context window, native tool use, structured JSON, and OpenAI-compatible APIs. Pricing is $0.25 per million input tokens and $0.75 per million output tokens. Its pitch targets coding, agents, voice, and retrieval workloads where latency and throughput outweigh peak single-shot accuracy.

### Comment pulse

- Enthusiasts proposed measuring intelligence per second, watt, or dollar, arguing rapid iteration can outweigh modestly lower single-shot quality.
- Skeptics cited a slow, incorrect simple-answer test; counterpoint: Inception says fast repeated attempts can compensate when workflows can verify results.
- Technical discussion focused on KV caching, time to first token, and whether diffusion’s speed survives tool-heavy, high-concurrency production use.

### LLM perspective

- **View:** Throughput is valuable only when downstream verification makes cheaper iteration useful.
- **Impact:** Diffusion models could shorten agent loops, interactive coding, and voice-response latency.
- **Watch next:** Independent quality, hardware, concurrency, and time-to-first-token benchmarks.
