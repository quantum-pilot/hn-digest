# Right-sizes LLM models to your system's RAM, CPU, and GPU

- Score: 257 | [HN](https://news.ycombinator.com/item?id=47211830) | Link: https://github.com/AlexsJones/llmfit

- TL;DR  
  llmfit is a Rust-based terminal tool that inspects your RAM/CPU/GPU, then ranks hundreds of local LLMs by estimated quality, speed, memory fit, and context. It understands multi‑GPU, MoE models, quantization levels, and integrates with Ollama, llama.cpp, and MLX, outputting an interactive TUI or JSON for agents and scripts. Discussion focuses on offline versus web-based approaches, simple bandwidth-based sizing heuristics, questions around estimate accuracy and model freshness, and comparisons with Hugging Face and other online calculators.

- Comment pulse  
  Website would be nicer UX → some want a pure web form; others note browsers lack low-level hardware access—counterpoint: manual spec entry or uploaded reports.  
  Rules-of-thumb sizing → formulas using params, quantization, memory bandwidth to estimate VRAM and tok/s, plus notes on KV cache, mmap, MoE actives.  
  Skepticism about accuracy → some models flagged unrunnable actually work; database lags new releases and Unsloth variants, limiting reliability beyond rough first-pass guidance.

- LLM perspective  
  View: Offline, hardware-aware recommenders fill a real gap, but must track rapidly changing model ecosystems to stay useful.  
  Impact: Helps local-LLM tinkerers, small teams, and tools like OpenClaw choose right-sized models without hand-tuning benchmarks.  
  Watch next: Automated HF scraping, benchmark ingestion, and plugin architecture so community can add models, providers, and better calibration data.
