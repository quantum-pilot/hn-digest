# Running Gemma 4 26B at 5 tokens/sec on a 13-year-old Xeon with no GPU

- Score: 219 | [HN](https://news.ycombinator.com/item?id=48922434) | Link: https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/

### TL;DR
An engineer runs Google’s Gemma 4 26B MoE model at ~5 tokens/sec on a 2013 dual‑Xeon (AVX1‑only, no GPU, <$300). They use Claude as a coding partner to adapt ik_llama.cpp for pre‑AVX2 CPUs, diagnosing a subtle MoE dispatch bug that produced deterministic gibberish and adding proper fallbacks. The result is a cheap, private local LLM and a concrete example of human‑in‑the‑loop AI debugging. HN discussion centers on future local‑LLM scale, real‑world speed, and local vs cloud economics.

---

### Comment pulse
- Bigger local MoE soon → Some expect >200B‑class MoE on consumer machines; skeptics cite memory bandwidth, slow speeds, and degraded quality from extreme quantization.  
- Cost per token debate → Some calculate legacy CPUs cost more per token than cloud; others with efficient rigs or cheap/solar power beat cloud pricing.  
- Throughput comparisons → Commenters report 8–12 t/s on similar Xeons and 40+ t/s on newer CPUs by using lower‑bit quantization or small GPUs.

---

### LLM perspective
- View: Demonstrates AI assistants refactor performance‑critical C++ when guided by someone who can test, interpret logs, and constrain scope.  
- Impact: Extends useful life of pre‑AVX2 servers as private LLM appliances and pressures inference libraries to keep robust CPU fallbacks.  
- Watch next: Systematic benchmarks across CPUs, power, and quantization levels; better tools to detect graph bugs and instruction‑set mismatches.
