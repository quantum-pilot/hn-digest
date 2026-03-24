# iPhone 17 Pro Demonstrated Running a 400B LLM

- Score: 449 | [HN](https://news.ycombinator.com/item?id=47490070) | Link: https://twitter.com/anemll/status/2035901335984611412

## TL;DR
An iPhone 17 Pro demo reportedly runs a “400B”-parameter LLM by combining three tricks: Apple’s “LLM in a Flash” SSD-weight streaming, a Mixture-of-Experts (MoE) architecture where only ~17B parameters are active per token, and heavy quantization. Commenters argue the headline is technically misleading but still see it as a meaningful proof-of-concept for large, mostly-on-device models. Concerns focus on thermal throttling, power use, and the gap between flashy parameter counts and real-world capability.

*Content unavailable; summarizing from title/comments.*

---

## Comment pulse
- Headline inflates model size → Qwen3.5-397B-A17B is MoE with ~17B active parameters plus quantization; “400B” feels like hype — counterpoint: still notable for a phone demo.  
- Technique is known → Based on Apple’s “LLM in a Flash” SSD streaming; similar to Cerebras weight streaming, but iPhone RAM and power constraints remain hard limits.  
- Practical limits and futures → Current Apple devices overheat and throttle on local LLMs; some imagine cooling add-ons, others foresee ubiquitous pocket AIs mostly wasted on doomscrolling.

---

## LLM perspective
- View: This shows MoE + streaming + quantization makes “impossible” parameter counts marketing-accessible on mobile, while true capability tracks active params.  
- Impact: Better on-device assistants, privacy-preserving apps, and offline tools; also pressure on phone SoCs, storage bandwidth, and thermal design.  
- Watch next: Independent latency/quality benchmarks, power-draw measurements, and OS-level APIs for weight streaming vs. vendor push toward cloud AI.
