# Mercury 2: Fast reasoning LLM powered by diffusion

- Score: 337 | [HN](https://news.ycombinator.com/item?id=47144464) | Link: https://www.inceptionlabs.ai/blog/introducing-mercury-2

### TL;DR
Mercury 2 is a diffusion-based language model that generates many tokens in parallel, refining whole drafts instead of decoding sequentially. Inception claims >5× speedups (≈1,000 tok/s on Blackwell), low prices, 128K context, tools, and OpenAI-compatible APIs, targeting latency-sensitive coding, agentic workflows, voice, and RAG. Hacker News is intrigued by “intelligence per second” as a metric and faster agent loops, but reports mixed early quality, energy-efficiency concerns, and technical questions about caching, reasoning behavior, and ties to classic transformer models.

---

### Comment pulse
- Speed as a first-class quality metric → people propose “intelligence per second” combining capability, tokens/sec, and energy/hardware cost to judge models in iterative agent loops.  
- Early user tests flag weak quality → simple queries (e.g., Maradona) answered slowly with obvious errors, raising doubts that raw speed offsets lower reliability.  
- Strong curiosity → co-founder fields questions on KV caching, reasoning blocks, TTFT, diffusion–transformer links; others tout 1k tok/s enabling multi-shot prompting—counterpoint: batching makes transformers fast.  

---

### LLM perspective
- View: Diffusion LMs shift the decode bottleneck, but must prove they match AR models on robustness, tooling, and edge-case behavior.  
- Impact: Fast “good-enough” models benefit IDE copilots, agents, voice bots, and RAG systems where iteration speed beats single-shot optimality.  
- Watch next: Independent latency–quality–energy benchmarks, TTFT for voice, and hybrid pipelines mixing small planners with large diffusion generators.
