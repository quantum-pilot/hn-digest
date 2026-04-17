# Qwen3.6-35B-A3B: Agentic coding power, now open to all

- Score: 867 | [HN](https://news.ycombinator.com/item?id=47792764) | Link: https://qwen.ai/blog?id=qwen3.6-35b-a3b

### TL;DR
- Qwen3.6-35B-A3B is a 35B-parameter sparse MoE model with only 3B active params, opened as full weights and accessible via Alibaba’s Qwen Studio/API. Benchmarks show it matching or beating much larger dense models on coding/agent tasks (SWE-bench, Terminal-Bench) and competitive multimodal performance with Claude Sonnet 4.5 and Gemma4-31B. It supports “thinking” traces and plugs into OpenClaw, Qwen Code, and Claude Code. HN readers focus on local GGUF quantizations, image quality anecdotes, quantization pitfalls, and whether small open models meet enterprise needs.

---

### Comment pulse
- Local users run Unsloth GGUF quantizations on laptops/4090s, report higher speed and better agentic behavior than Qwen3.5—counterpoint: launch-day quants can be buggy/misleading.  
- Image tests like “pelican/flamingo on a bicycle” impress some, but others note anatomical errors, reinforcing skepticism about missing world models behind pattern-matching.  
- Commenters welcome open weights after Alibaba turbulence, debate if 3B-active models suffice for regulated sectors versus investing in on‑prem clusters; note exam-heavy embeddings.

---

### LLM perspective
- View: Sparse 35B/3B MoE plus long-context “thinking” mode makes this a strong open candidate for autonomous coding agents.  
- Impact: Low-cost local deployments become more attractive; devs can prototype serious terminal-based assistants without sending codebases to US clouds.  
- Watch next: Independent SWE-bench and project evals, stability of community quantizations, and whether larger Qwen3.6 checkpoints ship as open weights.
