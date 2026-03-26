# TurboQuant: Redefining AI efficiency with extreme compression

- Score: 479 | [HN](https://news.ycombinator.com/item?id=47513475) | Link: https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/

### TL;DR

TurboQuant is a Google Research compression scheme for LLM key‑value caches and vector search that preserves dot‑product similarity while using as little as ~3 bits per value. It first rotates vectors to make coordinates well‑behaved, then applies PolarQuant-style scalar quantization for most bits and a 1‑bit Johnson‑Lindenstrauss residual to debias the remaining error. Benchmarks show no accuracy loss, up to 8× faster attention on H100, and better recall than standard PQ methods, sparking debate over prior art and rapid open‑source ports.

### Comment pulse

- Claim: TurboQuant omits key prior work on rotation-based compression (e.g., DRIVE) → debate over citation ethics vs inevitability of rediscovery — counterpoint: rotations are classical.  
- Claim: random rotation makes activations more uniform and Gaussian, so scalar quantization bins waste less capacity; 1‑bit JL keeps per-dimension signs, preserving similarities.  
- Claim: early TurboQuant support in llama.cpp shows algorithmic complexity is modest; optimizations like Hadamard-based rotations may reduce compute from O(d²) to O(d log d).  

### LLM perspective

- View: If TurboQuant’s 3‑bit, zero‑loss KV cache generalizes, long‑context LLMs become cheaper than current inference-optimized architectures.  
- Impact: Memory-bound workloads—chatbots, RAG, embedding search—gain most, especially on GPUs where KV cache dominates cost and latency.  
- Watch next: independent reproductions, open-source kernels, and comparisons against architectural tricks like multi-head latent attention or recurrent long-context alternatives.
