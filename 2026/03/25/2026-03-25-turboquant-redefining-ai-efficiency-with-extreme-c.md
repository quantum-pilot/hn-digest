# TurboQuant: Redefining AI efficiency with extreme compression

- Score: 479 | [HN](https://news.ycombinator.com/item?id=47513475) | Link: https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/

### TL;DR

Google Research presents TurboQuant, a theoretically grounded vector quantizer combining PolarQuant’s random rotation and compact scalar codes with QJL’s one-bit residual estimator. It targets LLM KV caches and vector search without per-block full-precision constants. Google reports 3-bit caches with no benchmark accuracy loss, at least 6× memory reduction, and up to 8× faster 4-bit attention-logit computation versus 32-bit keys on H100s. Commenters welcomed rapid llama.cpp experimentation but raised prior-art attribution and explanatory-accuracy concerns.

### Comment pulse

- A DRIVE author requested citation for similar 2021 rotation and bias correction — counterpoint: others called the mechanism older, recurring classical technique.
- Explanations emphasized that common rotation preserves pairwise geometry while spreading outlier energy across coordinates, making low-bit bins more efficient.
- An early llama.cpp experiment replaces quadratic rotation with a faster randomized Hadamard transform, pending equivalent theoretical and empirical behavior.

### LLM perspective

- **View:** The claims are consequential, but production value depends on end-to-end kernels and representative workloads.
- **Impact:** Longer contexts and larger retrieval indexes could fit existing accelerators with lower latency and cost.
- **Watch next:** Independent reproductions, merged inference support, model breadth, quality tails, attribution updates, and total-system benchmarks.
