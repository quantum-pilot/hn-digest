# Making deep learning go brrrr from first principles (2022)

- Score: 145 | [HN](https://news.ycombinator.com/item?id=48246889) | Link: https://horace.io/brrr_intro.html

### TL;DR
Horace He explains deep-learning performance from first principles: GPU time decomposes into compute (FLOPs), memory bandwidth (moving tensors), and overhead (Python/framework/kernel launches). Modern accelerators are optimized for dense matmuls; most other ops are bandwidth-bound and slow because of DRAM traffic, not math. The key optimization is operator fusion, which reduces memory accesses and can make `cos(cos(x))` cost ~`cos(x)`. A roofline-style example shows when workloads shift from memory- to compute-bound. Finally, Python/framework overhead is huge for small ops, but mostly hidden for large, asynchronous kernels.

---

*Comment pulse*
- Nvidia’s dominance → TFLOPs, bandwidth, and interconnects have scaled aggressively for years; a 30-year incumbent still out-iterating newer rivals.
- Performance portability is chaotic → the “same” model in PyTorch, ONNX, ONNX Runtime, TensorRT behaves differently across runtimes/hardware; tuning is deeply platform-specific.
- Python vs A100 FLOPs comparison → some call it a category error; others say the apples-to-oranges contrast usefully illustrates overhead vs specialized throughput — counterpoint: core-count differences blur the ratio.

---

### LLM perspective
- View: Treating performance as compute vs bandwidth vs overhead is a reusable mental model for diagnosing slow training/inference.
- Impact: Helps practitioners prioritize: fusion and layout for memory-bound parts, batching and async execution for overhead-bound ones.
- Watch next: Better profilers exposing achieved FLOPs/bandwidth per op, and compilers that fuse more patterns automatically across frameworks and backends.
