# Running Gemma 4 26B at 5 tokens/sec on a 13-year-old Xeon with no GPU

- Score: 219 | [HN](https://news.ycombinator.com/item?id=48922434) | Link: https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/

### TL;DR

A dual 2013 Xeon E5-2690 v2 server with DDR3 and no GPU ran quantized Gemma 4 26B-A4B at 5.2 output tokens/s and 16 prompt tokens/s. Because Ivy Bridge lacks AVX2, Claude helped patch ik_llama.cpp’s build fallbacks and replace unsupported fused MoE operations; otherwise uncomputed tensors produced deterministic gibberish. The author frames this as agent-assisted debugging guided by human experiments, not one-shot automation. HN admired the retrofit but disputed whether reading-speed inference is useful or economical, emphasizing quantization, prompt speed, electricity, privacy, and local control.

### Comment pulse

- Economics depended on assumptions → one estimate matched local generation at $0.30 per million tokens, but cloud inference was eight times faster.
- Local proponents prioritized sovereignty → privacy, offline availability, and competitive pressure on cloud pricing outweighed electricity costs.
- Performance predictions polarized → optimists expect 200B MoEs on consumer hardware by 2027 — counterpoint: memory bandwidth, quality loss, and latency remain barriers.

### LLM perspective

- **View:** The impressive result is correctness on unsupported silicon, not throughput leadership.
- **Impact:** Old enterprise servers become viable private batch workers when latency is secondary and hardware is sunk cost.
- **Watch next:** Maintainer review, AVX1 regression tests, watt-meter measurements, first-token latency, and Q8 quality benchmarks.
