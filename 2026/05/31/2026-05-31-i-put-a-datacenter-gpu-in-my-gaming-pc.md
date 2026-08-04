# I put a datacenter GPU in my gaming PC

- Score: 271 | [HN](https://news.ycombinator.com/item?id=48345694) | Link: https://blog.tymscar.com/posts/v100localllm/

### TL;DR

For about £200, the author paired a secondhand 16GB Tesla V100 SXM2 and PCIe adapter with an RTX 4080, giving llama.cpp 32GB split VRAM. A 19GB Qwen3.6-27B quantized model delivered roughly 32 tokens/s generation, 133–160 tokens/s prompt processing, a 128k context window, and local vision support. Making it usable required rewiring an 82dB fan for motherboard PWM, pinning NixOS to legacy NVIDIA drivers, CUDA 12.2, and kernel 6.6, plus occasional cold boots. HN admired the economics but emphasized cooling, aging feature support, and long-context prefill latency.

### Comment pulse

- Cheap VRAM shifts costs into integration → old V100s lack bfloat16 and current driver support, while alternative MI-series cards still require ecosystem work.
- Generation speed hides agentic latency → 100k-token prefill at 150 tokens/s takes about 11 minutes — counterpoint: prefix caching can reduce repeated work.
- Server hardware assumes server airflow → community shrouds and 120mm fans can tame thermals, but quiet desktop operation requires deliberate engineering.

### LLM perspective

- **View:** The £200 result is a systems-hacking achievement, not a direct substitute for a supported 32GB consumer GPU.
- **Impact:** Hobbyists gain private inference and strong FP64 compute; maintainers inherit compatibility and safety burdens vendors no longer carry.
- **Watch next:** Benchmark prefill with cache reuse, sustained thermals, idle power, warm-reboot recovery, model compatibility, and total platform cost.
