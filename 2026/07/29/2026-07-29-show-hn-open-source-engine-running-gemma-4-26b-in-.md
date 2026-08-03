# Show HN: Open-source engine running Gemma 4 26B in 2 GB RAM on any M-series Mac

- Score: 594 | [HN](https://news.ycombinator.com/item?id=49098510) | Link: https://github.com/drumih/turbo-fieldfare

### TL;DR

TurboFieldfare is an Apache-licensed Swift and Metal runtime that runs the text-only Gemma 4 26B-A4B model on Apple Silicon using roughly 2 GB of weights and 4K KV cache. It keeps the 1.35 GB shared core resident while streaming only selected mixture-of-experts weights from a 14.3 GB SSD installation, overlapping reads with GPU work. Measured decode reaches 5.1–6.3 tokens/second on an 8 GB M2 and 31–35 on an M5 Pro. HN focused on why selective loading is difficult, whether tuned pread beats mmap or llama.cpp, and older-macOS compatibility.

### Comment pulse

- Selective loading is model-dependent → arbitrary dense weights lack semantic labels, while Gemma’s routed experts expose per-token subsets that can be cached and streamed.
- I/O strategy needs comparison → plain mmap can meet the memory target, but reactive paging cannot anticipate expert selection or overlap reads deliberately.
- Community testing widened compatibility → an M1 on macOS 15 reportedly reached 5–6 tokens/second after bypassing Metal 4 language settings, with reduced prefill speed.

### LLM perspective

- View: SSD streaming trades latency for larger sparse models, making expert prediction, caching, and I/O scheduling as important as quantization.
- Impact: Eight-gigabyte Mac owners gain local access to a 26B model, but only through model-specific code and substantial disk storage.
- Watch next: Benchmark against llama.cpp SSD offload under matched cold-cache conditions, context lengths, output lengths, memory pressure, and drive characteristics.
