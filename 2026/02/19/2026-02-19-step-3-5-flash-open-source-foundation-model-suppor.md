# Step 3.5 Flash – Open-source foundation model, supports deep reasoning at speed

- Score: 209 | [HN](https://news.ycombinator.com/item?id=47069179) | Link: https://static.stepfun.com/blog/step-3.5-flash/

### TL;DR
Step 3.5 Flash is a 196B-parameter open‑source MoE model that only activates 11B parameters per token, targeting “frontier-level” reasoning and agents at lower inference cost. It combines sliding‑window + full attention, 3‑token‑ahead decoding, and 256K context to reach 100–350 tok/s while matching or nearing GPT‑5.2, Claude Opus, Gemini 3.0 Pro, and Kimi K2.5 on math, coding, and agent benchmarks. A custom RL algorithm (MIS‑PO) stabilizes long‑horizon training, and INT4 GGUF releases make serious agentic coding feasible on high‑end local machines.

---

### Comment pulse
- Local-first enthusiasts → 4‑bit quant runs fast and stable on 128 GB Macs; best agentic local model some have used, especially with CLI harnesses—counterpoint: current build can get stuck in infinite reasoning loops.  
- Benchmark skeptics → 51% on Terminal‑Bench sounds low for “unwavering stability”; context shows this is ~⅔ of SOTA and benchmark design is odd and tool-heavy.  
- Reliability worriers → Some report heavy hallucinations on niche knowledge (e.g., Pokémon decks); others treat it mainly as an execution/agent engine, delegating facts to search tools.

---

### LLM perspective
- View: This is one of the first open models explicitly optimized for “fast reasoning + tools + agents,” not just chat/coding quality.  
- Impact: Strong, cheap local agent brains plus cloud orchestration will pressure proprietary stacks, especially for dev tools and internal automation.  
- Watch next: Better loop‑prevention, token‑efficiency improvements, and community harnesses/benchmarks for tool-use and edge–cloud workflows will determine real‑world adoption.
