# Qwen3-Coder-Next

- Score: 550 | [HN](https://news.ycombinator.com/item?id=46872706) | Link: https://qwen.ai/blog?id=qwen3-coder-next

### TL;DR
Qwen3-Coder-Next is an open-weight coding model built on a hybrid-attention MoE backbone with only ~3B active parameters, trained as an “agent” on executable programming tasks and RL feedback. Benchmarks like SWE-Bench (including Pro) show it rivaling much larger open models for code agents while being cheap enough for high-end local hardware. Hacker News discussion focuses on how well it really runs locally, quantized GGUF variants and setup recipes, and skepticism that it truly matches models like Claude Sonnet 4.5.

### Comment pulse
- "Local model" debate → some require sub-$10k self-hosted hardware, not cloud-orchestrated; they want standard benchmarks (latency, tps, memory) across typical laptop/desktop classes.  
- Unsloth GGUF quantizations + llama.cpp/docker recipes make setup easy; users report 17–60 tok/s and 28–39GB RAM on mid/high-end consumer GPUs.  
- Some find it impressive but closer to Claude Haiku than Sonnet 4.5, with errors/loops — counterpoint: still remarkable capability for such a tiny active model.  

### LLM perspective
- View: Agent-style training on executable tasks plus sparse MoE looks like a general recipe for efficient specialist models.  
- Impact: High-quality local coding agents could shift many developers from cloud IDE copilots to on-prem setups, especially in regulated environments.  
- Watch next: Independent SWE-Bench Pro runs, open agent scaffolds, and standardized home-hardware benchmarks to clarify competitiveness versus Claude and GPT.
