# Launch HN: RunAnywhere (YC W26) – Faster AI Inference on Apple Silicon

- Score: 173 | [HN](https://news.ycombinator.com/item?id=47326101) | Link: https://github.com/RunanywhereAI/rcli

### TL;DR
RunAnywhere’s RCLI is an open‑source, on‑device voice assistant for macOS Apple Silicon that chains STT → LLM → TTS, can control 38 Mac actions, and query local documents via RAG, all without cloud or API keys. Underneath, their proprietary MetalRT engine accelerates LLM, speech recognition, and TTS on M3+ chips, claiming very high token throughput and sub‑200ms voice latency; on M1/M2 it falls back to llama.cpp. HN feedback praises the concept and speed but notes early bugs and confusing positioning.

---

### Comment pulse
- What is this? → A proprietary MetalRT inference runtime plus RCLI, an open‑source Mac voice assistant showing fast, fully local AI workflows — counterpoint: several readers still found this unclear.  
- Early usage → Fun and fast, with memory and “personality”; but some voice actions report success without executing, and Homebrew installs can be flaky.  
- Feature requests → Better model selection (e.g., Unsloth quants, HuggingFace options), diarization, and data on big‑model latency on high‑end Macs; diarization support is planned.

---

### LLM perspective
- View: Strong proof-of-concept for local, multimodal “Mac copilot,” though proprietary GPU engine and Apple‑only focus limit openness and reach.  
- Impact: Most useful for Mac power‑users and devs who value privacy, offline operation, and system automation over frontier‑model capability.  
- Watch next: Independent benchmarks vs MLX/CoreML, stable M1/M2 GPU support, richer action reliability, and expansion beyond macOS/Apple Silicon.
