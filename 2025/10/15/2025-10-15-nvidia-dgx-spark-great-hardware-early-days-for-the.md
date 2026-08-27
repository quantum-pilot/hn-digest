# Nvidia DGX Spark: great hardware, early days for the ecosystem

- Score: 171 | [HN](https://news.ycombinator.com/item?id=45586776) | Link: https://simonwillison.net/2025/Oct/14/nvidia-dgx-spark/

### TL;DR

Simon Willison's NVIDIA-provided DGX Spark preview finds compelling compact hardware—20 ARM64 CPU cores, 128GB unified memory, a Blackwell GPU, and 4TB storage—but an immature software experience around ARM CUDA. Official containers and newly released guides improved setup, while Ollama, llama.cpp, LM Studio, vLLM, and Unsloth added early support. Commenters welcomed easier post-embargo installation yet questioned its $4,000 value, inference speed, architecture compatibility, and longevity versus Macs, discrete NVIDIA GPUs, and AMD APUs.

### Comment pulse

- Support improved rapidly after launch → shared containers and integrations turned some vLLM setup into a short recipe.
- Unified memory is the differentiator → commenters disputed performance value against faster GPUs, Macs, and cheaper AMD systems.
- ARM remains frictionful → software often assumes x86, repeating ecosystem problems familiar from earlier ARM accelerators.

### LLM perspective

- View: Spark offers unusual local model capacity, but ecosystem readiness matters as much as its memory specification.
- Impact: Researchers gain a compact CUDA development target while accepting early-adopter tooling and compatibility costs.
- Watch next: Independent inference, training, power, support-lifetime, and price-performance comparisons across realistic model sizes.
