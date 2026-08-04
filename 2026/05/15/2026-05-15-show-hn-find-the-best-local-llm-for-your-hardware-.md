# Show HN: Find the best local LLM for your hardware, ranked by benchmarks

- Score: 277 | [HN](https://news.ycombinator.com/item?id=48146369) | Link: https://github.com/Andyyyy64/whichllm

### TL;DR

WhichLLM is a Python CLI that detects NVIDIA, AMD, Apple Silicon, or CPU hardware, filters Hugging Face models that should fit, then ranks them using benchmark quality, recency, evidence confidence, quantization, estimated VRAM, and speed. It can simulate GPUs, plan hardware, emit JSON or snippets, and launch models. HN readers liked quantization-aware recommendations but reported outdated or implausible picks, a broken Homebrew install, and missing context-length, batching, KV-cache, backend, and verbosity effects. Several also distrusted the project’s apparent AI-generated presentation and deleted marketing plan.

### Comment pulse

- Model selection looked stale → users saw Qwen 2.5 recommendations while newer Qwen 3.5/3.6 models ran well on the same hardware.
- One speed number is inadequate → long contexts, batching, KV-cache quantization, verbosity, and MLX/backend choices materially alter throughput and memory.
- A browser tool felt safer → critics resisted installing an unknown CLI — counterpoint: shipping a CLI avoids hosting and supports automation.

### LLM perspective

- View: Ranking local models is multidimensional; confidence labels help, but inaccurate freshness or runtime assumptions can overwhelm the score.
- Impact: Buyers and self-hosters could make costly hardware or model choices from estimates lacking workload-specific validation.
- Watch next: Reproducible recommendation fixtures, hardware-measured benchmarks, dependency audit, fixed installation, and transparent data freshness.
