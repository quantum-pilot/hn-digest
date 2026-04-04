# April 2026 TLDR Setup for Ollama and Gemma 4 26B on a Mac mini

- Score: 290 | [HN](https://news.ycombinator.com/item?id=47624731) | Link: https://gist.github.com/greenstevester/fc49b4e60a4fef9effc79066c1033ae5

- TL;DR  
    - Guide shows how to run Google’s Gemma 4 locally on an Apple‑silicon Mac mini using Ollama: install via Homebrew, auto‑start the server, preload the gemma4:latest (8B) model with a LaunchAgent, and keep it resident using OLLAMA_KEEP_ALIVE, leveraging Ollama’s MLX backend and improved caching. Author notes 26B overwhelms a 24GB machine. HN discussion warns that brand‑new open‑weight releases often have broken tool‑calling and quantizations, and that even good local models still trail Claude‑class cloud models for complex coding.

- Comment pulse  
    - Cutting-edge open models are often broken at launch → tokenizer, tool-calling, and quantization bugs mean results reflect your inference stack, not the weights.  
    - On Macs, LM Studio currently struggles with Gemma 4 and tool calls → some report freezes, while llama.cpp runs 26B quantizations smoothly.  
    - Open models help for smaller tasks but lag Claude Sonnet for coding → many stick with paid APIs — counterpoint: some rate GLM5/KimiK2.5 as close.

- LLM perspective  
    - View: This setup is a solid template for “LLM appliance” Macs: background-loaded model, warm cache, simple local API.  
    - Impact: Developers can prototype private agents and coding helpers without cloud costs, while accepting weaker reasoning versus top closed models.  
    - Watch next: Track Gemma 4 inference fixes, Ollama MLX improvements, and benchmarks comparing 8B vs 26B quality under realistic coding/tool-use workloads.
