# Show HN: Open-source engine running Gemma 4 26B in 2 GB RAM on any M-series Mac

- Score: 594 | [HN](https://news.ycombinator.com/item?id=49098510) | Link: https://github.com/drumih/turbo-fieldfare

- TL;DR  
  TurboFieldfare is an Apache-licensed Swift+Metal engine that runs Google’s Gemma 4 26B‑A4B on any 8 GB M‑series Mac using ~2 GB RAM. It keeps a 1.35 GB shared core and FP16 KV cache in memory while streaming mixture‑of‑experts weights from SSD via scheduled pread, plus 4‑bit quantization and an expert LFU cache. A Mac app, CLI, and OpenAI‑style server are included. HN discusses why selective loading is hard, compares mmap vs tuned I/O, and notes language‑model fingerprints in the README.

- Comment pulse  
  - Selective loading sounds obvious → but deciding which parameters to skip per token is unsolved; weights lack semantic meaning and routing is computationally hard.  
  - OS‑driven mmap offload works → hand‑tuned pread overlapped with GPU cuts expert load from 10 ms to 2.8 ms and boosts 0.5→4 tok/s.  
  - Language‑model phrases in the README triggered complaints about “Claudespeak”, but others pushed back, noting the author is a non‑native using LLMs for proofreading.

- LLM perspective  
  - View: Demonstrates that IO-aware runtimes plus MoE can shrink RAM needs for frontier-scale models without unacceptable throughput loss.  
  - Impact: Broadens who can experiment with MoE models locally, including students and indie devs without high‑VRAM GPUs or cloud budgets.  
  - Watch next: Rigorous comparisons with mmap-based engines, mobile ports, and techniques to push model knowledge into tools, not parameters.
