# How to setup a local coding agent on macOS

- Score: 498 | [HN](https://news.ycombinator.com/item?id=48507020) | Link: https://ikyle.me/blog/2026/how-to-setup-a-local-coding-agent-on-macos

### TL;DR

On a 64GB M1 Max, Kyle Howells builds a fully local coding agent with llama.cpp using Metal, Gemma 4 26B-A4B Q4, a Q8 MTP draft model, a multimodal projector, and Pi through an OpenAI-compatible localhost API. MTP raised measured generation from 58.2 to 72.2 tokens/second; Qwen3.6 35B-A3B appeared stronger for coding but ran at 55. HN welcomed a usable private offline stack but cautioned that 128 generated tokens cannot validate speculative-decoding gains and urged longer-context benchmarks, llama.cpp’s built-in tools, or simpler launchers.

### Comment pulse

- The benchmark is too short → MTP acceptance can be front-loaded, so 128-token outputs may exaggerate gains compared with long coding sessions.
- Context matters as much as decode speed → realistic tests need 3,000-token prompts and performance measurements near 32K–64K context.
- Local tooling spans control versus convenience → llama.cpp exposes tuning and direct downloads — counterpoint: oMLX, Ollama, and GUIs simplify onboarding.

### LLM perspective

- **View:** Local agents are now usable on high-memory Macs, but model quality and tool reliability outweigh raw tokens per second.
- **Impact:** Developers gain privacy, offline resilience, and zero marginal inference fees while accepting hardware limits and configuration work.
- **Watch next:** Compare Gemma and Qwen on repository tasks, tool-call success, long contexts, energy use, and end-to-end completion time.
