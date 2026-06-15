# How to setup a local coding agent on macOS

- Score: 498 | [HN](https://news.ycombinator.com/item?id=48507020) | Link: https://ikyle.me/blog/2026/how-to-setup-a-local-coding-agent-on-macos

### TL;DR
Author walks through building a fast, offline coding agent on an M1 Max Mac using llama.cpp with Metal, Unsloth’s Gemma 4 26B Q4 GGUF, and Multi-Token Prediction (MTP). Tuning the speculative draft parameter (`--spec-draft-n-max`) yields ~72 tokens/s vs 58/s baseline, beating equivalent MLX setups on the same hardware. The stack is exposed via an OpenAI-compatible `/v1` endpoint and wired into the Pi terminal agent, including image support; Qwen3.6 35B is tried as a slower but stronger coding alternative.

---

### Comment pulse
- Benchmarks are too short → 128 generated tokens overstate MTP gains; real tests need long prompts, long contexts, and llama.cpp’s dedicated benchmarking tools.  
- Setup choices → llama.cpp can fetch Hugging Face models directly with `-hf`/`-hfd`, simplifying the guide’s download steps.  
- Alternatives and tradeoffs → Others report good results with oMLX, ds4/DeepSeek, or Ollama+opencode—counterpoint: many still find llama.cpp GGUF consistently faster on Mac.

---

### LLM perspective
- View: This shows practical, reproducible steps to get near–GPT-4-like coding help fully offline on modern Macs.  
- Impact: Beneficial for developers sensitive to privacy, latency, or unreliable internet, especially those already using OpenAI-compatible tools.  
- Watch next: Better MTP tuning tools, richer Mac-focused launchers (LM Studio, oMLX, ds4), and more optimized MLX checkpoints for Gemma/Qwen.
