# DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence

- Score: 157 | [HN](https://news.ycombinator.com/item?id=47885014) | Link: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro

### TL;DR
DeepSeek-V4 is an open-source Mixture-of-Experts LLM family with 1M-token context, a 1.6T-parameter Pro model (49B active) and a 284B Flash model (13B active). A hybrid attention scheme plus compression yields roughly an order-of-magnitude KV cache savings for long contexts, while benchmarks put V4-Pro-Max at or near frontier closed models in coding and many reasoning tasks. HN discussion focuses on how (and how slowly) it might run locally, its value versus Claude/GPT, and impressive quality-per-dollar.

---

### Comment pulse
- Can it run locally? → MoE uses 49B active params, quantization and streaming make it possible but painfully slow—counterpoint: Flash + future distillations may be practical.
- Competitiveness → Many see DeepSeek as ~2 months behind top proprietary models, yet already “good enough” to replace Claude Sonnet in some setups.
- Practical value → Users report Flash solving tricky Common Lisp bugs; ultra-low cost enables billions-token evaluations that would be unaffordable on closed APIs.

---

### LLM perspective
- View: Million-token context plus explicit “thinking modes” is a notable step toward practical long-doc reasoning and controllable depth.
- Impact: Strong, cheap open models pressure API pricing, enable on-prem deployments, and broaden access for research and smaller companies.
- Watch next: Community quantizations/distills, real 1M-token use cases, and head-to-head tool-use/latency benchmarks versus latest GPT, Claude, Gemini.
