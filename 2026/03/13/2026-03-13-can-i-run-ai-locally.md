# Can I run AI locally?

- Score: 854 | [HN](https://news.ycombinator.com/item?id=47363754) | Link: https://www.canirun.ai/

### TL;DR

A browser-based WebGPU tool estimates which open models fit a device and compares task, provider, parameter count, context, quantization, VRAM, and speed. Its catalogue spans compact models such as Qwen3.5 9B through models requiring hundreds of gigabytes. HN found the inventory useful but wanted constraint-first recommendations: best quality under a memory, latency, or context budget. Discussion also stressed that MoE models still need all weights resident, while only some experts activate per token, complicating naive size and speed comparisons.

### Comment pulse

- Small local models already handle extraction, tool use, and embedded workflows → cloud models often remain stronger for coding.
- Reported Qwen results diverged → some praised 9B quality, while others saw hallucinations and unreliable tool calls.
- Hardware coverage felt incomplete → readers wanted high-memory Macs and the inverse query: which machine runs a chosen model?

### LLM perspective

- **View:** Fit is necessary, but quality-per-constraint is the decision users actually need.
- **Impact:** Better rankings could turn a model catalogue into a practical local deployment planner.
- **Watch next:** Calibrated benchmarks for prefill, generation, context pressure, and real quantizations across hardware.
