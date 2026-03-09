# How to run Qwen 3.5 locally

- Score: 442 | [HN](https://news.ycombinator.com/item?id=47292522) | Link: https://unsloth.ai/docs/models/qwen3.5

### TL;DR
Unsloth’s guide explains how to run Alibaba’s Qwen3.5 models (0.8B–397B) locally via llama.cpp, LM Studio, and an OpenAI-compatible llama-server. It ships Dynamic 2.0 GGUF quantizations (2–8 bit), with a memory table, tuned sampling configs, and switches for the hybrid “thinking” reasoning mode. Benchmarks show 3–4‑bit quants stay close to full precision, enabling even the 397B MoE on 192–256GB Macs. HN users report 9B–27B variants are fast and useful on consumer GPUs but still below top cloud models for complex agents.

### Comment pulse
- Consumer HW viability → 9B on 16GB GPUs hits ~100 tok/s; 27B 4‑bit fits 16GB with Sonnet‑4‑like quality—counterpoint: still weaker than Sonnet/Opus for hard tasks.  
- Quant choice confusion → Many GGUF types (Q4_0, Q4_K_M, UD‑Q4_K_XL); docs say older Q4_0/Q4_1 hurt accuracy, XL merely larger than M.  
- Latency vs quality → Thinking mode boosts coding accuracy (35B >27B) but adds big latency; Qwen3.5 sliding‑window attention halves token/s vs older Qwen3 in llama.cpp.  

### LLM perspective
- View: Turnkey GGUFs plus tooling make high‑end Qwen3.5 a realistic local option instead of a research-only curiosity.  
- Impact: Stronger on‑device coding/chat agents, especially for developers with 16–64GB Macs/GPUs who previously topped out at weaker 7B–13B models.  
- Watch next: Improved llama.cpp kernels for Qwen3.5, standardized quant naming, and community repositories of tested configs per model/OS/hardware.
