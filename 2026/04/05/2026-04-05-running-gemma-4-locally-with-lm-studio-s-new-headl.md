# Running Gemma 4 locally with LM Studio's new headless CLI and Claude Code

- Score: 158 | [HN](https://news.ycombinator.com/item?id=47651540) | Link: https://ai.georgeliu.com/p/running-google-gemma-4-locally-with

### TL;DR

LM Studio 0.4.0 turns its inference engine into the headless llmster daemon plus `lms` CLI, enabling downloads, model loading, chat, APIs, continuous batching, and MCP without the desktop app. The author runs quantized Gemma 4 26B-A4B—26B total, 3.8B active—at about 51 tokens/second on a 48 GB M4 Pro. Its 17.99 GB model needs roughly 21 GiB at 48K context; LM Studio exposes an Anthropic-compatible endpoint so Claude Code can use it locally. Privacy and zero API cost improve, but complex agent work is slower, memory-heavy, and less reliable.

### Comment pulse

- Ollama offers a dramatically shorter launch command — counterpoint: one user reported Gemma looping indefinitely while Nemotron, GLM, and Qwen worked.
- An LM Studio user saw Claude Code lose its place and halt mid-plan repeatedly, whereas the Ollama API remained stable.
- Speculative decoding drew interest, but diverse token routes can activate many experts during verification and make MoE inference slower rather than faster.

### LLM perspective

- **View:** Protocol compatibility separates the coding harness from its model, but behavioral compatibility remains the harder constraint.
- **Impact:** Developers gain offline review and experimentation; sustained multi-file automation still favors faster, better-aligned hosted or alternative local backends.
- **Watch next:** Compare LM Studio and Ollama task completion, stalls, context retention, thermals, swap, parallel load, and model-specific tool compliance.
