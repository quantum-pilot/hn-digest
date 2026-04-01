# Ollama is now powered by MLX on Apple Silicon in preview

- Score: 602 | [HN](https://news.ycombinator.com/item?id=47582482) | Link: https://ollama.com/blog/mlx

### TL;DR
- Ollama 0.19 preview switches its Apple Silicon backend to Apple’s MLX framework, nearly doubling prefill and decode speeds on M5 chips while adding better KV caching and NVFP4 quantization for higher‑fidelity, production‑parity models like Qwen3.5‑35B‑A3B (requires >32 GB RAM). HN discussion focuses on the push toward on‑device AI (Apple’s Foundation Model, MLX tools, SSD‑backed caches) and debates whether local models can truly rival cloud AI on cost, privacy, efficiency, and ergonomics.

### Comment pulse
- Embedded Apple models: AFM via apfel CLI is fast and scriptable but limited by 4k context, heavy guardrails, and English‑centric behavior — counterpoint: offline, free.
- On‑device vs cloud: proponents cite privacy, offline reliability, and ‘good‑enough’ small models; skeptics stress user apathy, B2B economics, and datacenters’ superior speed and continual improvement.
- Tooling split: some favor MLX stacks like omlx.ai or llama.cpp/Lemonade for flexibility; others stay with Ollama for Docker‑like CLI, simple API, and stable defaults.

### LLM perspective
- View: MLX integration plus NVFP4 support turns high‑RAM Macs into credible local inference nodes for serious coding and agent workflows.
- Impact: Raises the bar for Apple‑centric dev tools; alternative runtimes must match Ollama’s new speed, caching, and dev‑experience advantages.
- Watch next: Expect benchmarks on non‑M5 chips, broader NVFP4 model catalog, easier custom‑model import, and potentially SSD‑backed KV caching built into Ollama.
