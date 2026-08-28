# Qwen3 30B A3B Hits 13 token/s on 4xRaspberry Pi 5

- Score: 347 | [HN](https://news.ycombinator.com/item?id=45148237) | Link: https://github.com/b4rtaz/distributed-llama/discussions/255

### TL;DR

Distributed Llama ran a quantized Qwen3 30B-A3B mixture-of-experts model across four 8GB Raspberry Pi 5 boards connected by a gigabit switch. The posted benchmark reports 14.33 tokens per second for prompt evaluation and 13.04 for generation, with about 5.5GB required per node setup. Commenters found the experiment impressive but questioned its economics: one modern desktop CPU reportedly matched the throughput, while cheaper high-memory ARM boards may perform better. Compatibility and context capacity remain practical constraints.

### Comment pulse

- Enthusiasts see clusters as accessible test beds for distributed inference and eventual offline edge devices.
- Skeptics said four Pis may cost more than a used desktop or unified-memory machine offering similar performance.
- Child-focused talking toys prompted both excitement and strong concern about developmental and social effects.

### LLM perspective

- View: This demonstrates distributed MoE feasibility more than a price-performance victory for Raspberry Pi hardware.
- Impact: Existing idle board fleets can host private inference without purchasing a large-memory GPU.
- Watch next: Scaling efficiency, power use, longer-context benchmarks, model compatibility, and comparisons against single-node x86 or ARM systems.
