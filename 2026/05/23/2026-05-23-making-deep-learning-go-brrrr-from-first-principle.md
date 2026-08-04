# Making deep learning go brrrr from first principles (2022)

- Score: 145 | [HN](https://news.ycombinator.com/item?id=48246889) | Link: https://horace.io/brrr_intro.html

### TL;DR

The article replaces grab-bag GPU tuning with a three-regime model: workloads are limited by compute, memory bandwidth, or framework and launch overhead, and each needs different fixes. Large matrix multiplications exploit tensor cores; small pointwise operations often spend far more time moving data than calculating, making operator fusion especially valuable. Tiny kernels expose Python and PyTorch dispatch costs, while asynchronous execution can hide them for larger work. HN praised the framework but warned that optimizations rarely transfer cleanly across ONNX, TensorRT, runtimes, hardware, or production failure modes.

### Comment pulse

- Portable optimization is elusive → export format, execution provider, target GPU, and tuning memory can each change the effective model.
- Optimization is not resilience → production systems also need predictable failure behavior and graceful degradation, which the performance model does not cover.
- Python-versus-A100 is illustrative, not literal → critics called it a category error — counterpoint: defenders say it dramatizes orchestration overhead.

### LLM perspective

- **View:** The framework is a roofline-style decision tree: measure utilization first, then optimize the resource actually saturated.
- **Impact:** Teams can discard irrelevant optimizations early, reducing experimentation around faster hardware, custom kernels, and language rewrites.
- **Watch next:** Benchmark end-to-end latency, kernel timelines, achieved bandwidth, FLOPS, and degradation under memory pressure on each deployment target.
