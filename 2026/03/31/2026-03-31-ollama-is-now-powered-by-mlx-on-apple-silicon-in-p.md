# Ollama is now powered by MLX on Apple Silicon in preview

- Score: 602 | [HN](https://news.ycombinator.com/item?id=47582482) | Link: https://ollama.com/blog/mlx

### TL;DR

Ollama 0.19 previews an MLX backend for Apple Silicon, using unified memory and M5 GPU Neural Accelerators. With Qwen3.5-35B-A3B, Ollama reports prefill rising from 1,154 to 1,810 tokens per second and decoding from 58 to 112, though the comparison uses different quantizations. The release adds NVFP4 support plus cross-conversation cache reuse, prompt checkpoints, and smarter eviction; the showcased model requires over 32GB of unified memory. HN welcomed the speedup but disputed whether local inference beats cloud systems on privacy, energy, utilization, quality, and cost.

### Comment pulse

- Ollama users value two-command setup, stable API, and model library; critics say llama.cpp or Lemonade offers stronger optimization.
- Long-context agent users highlighted SSD-backed cold KV caching in other MLX runtimes as the remaining workflow advantage.
- Personal local-model projects ranged from private journals to scripting — counterpoint: limited memory, guardrails, and language handling still constrain usefulness.

### LLM perspective

- **View:** The largest practical gain may be cache persistence, because agents repeatedly share long prefixes across branches.
- **Impact:** High-memory Mac owners get a more credible offline coding stack without changing Ollama’s familiar interface.
- **Watch next:** Like-for-like quantization benchmarks, older-chip results, model coverage, cache correctness, import tooling, and peak memory.
