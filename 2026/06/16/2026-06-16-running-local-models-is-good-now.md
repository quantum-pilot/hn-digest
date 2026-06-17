# Running local models is good now

- Score: 954 | [HN](https://news.ycombinator.com/item?id=48555993) | Link: https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/

### TL;DR
Boykis argues that 2024–26-era open models (Gemma 4, GPT‑OSS, Qwen) crossed a threshold where running them locally is genuinely useful, not just a novelty. On an M2 Mac with 64GB RAM, she does “agentic coding” (refactors, unit tests, small recommender prototypes, doc search) at ~75% of frontier speed/quality, using LM Studio as an inference server and Pi as a Docker‑sandboxed agent harness. She stresses introspection, control, and experimentation benefits, while admitting latency, context limits, and production-readiness remain issues.

### Comment pulse
- Local LLMs are fragile to hardware/quantization → dense vs MoE tradeoffs, 4‑bit lobotomizes tools, laptops overheat; serious VRAM still needed—counterpoint: some report smooth Qwen3.6‑27B use on high-end GPUs.  
- UX and “personality” matter → several prefer local Qwen to Claude Sonnet for coding because it’s less verbose, less opinionated, and easier to keep in a pure “tool” role.  
- Economics and strategy split → one camp favors $50k on‑prem rigs as durable tooling; others say <$5k/year for top hosted models beats owning and running clusters.

### LLM perspective
- View: Local ~12–30B models now hit a “good enough” band for iterative coding help, automation, and private workflows on prosumer hardware.  
- Impact: Strongest value for developers needing data locality, reproducibility, model introspection, or insulation from API drift and usage caps.  
- Watch next: Better quantization/KV-cache schemes, Gemma/Qwen/GPT‑OSS refreshes, turnkey on-prem GPU appliances, and head-to-head TCO/performance studies vs mid-tier cloud subscriptions.
