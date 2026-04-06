# Running Gemma 4 locally with LM Studio's new headless CLI and Claude Code

- Score: 158 | [HN](https://news.ycombinator.com/item?id=47651540) | Link: https://ai.georgeliu.com/p/running-google-gemma-4-locally-with

### TL;DR
- Guide shows how to run Google’s Gemma 4 26B-A4B MoE model locally via LM Studio 0.4.0’s new `llmster` daemon and `lms` CLI, plus how to wire it into Claude Code through LM Studio’s Anthropic-compatible `/v1/messages` endpoint.  
- On a 48 GB M4 Pro MacBook, the Q4_K_M quantized model uses ~21 GiB at 48k context and generates ≈51 tok/s, with tunable context length, GPU offload, parallelism, and TTL.  
- Author argues MoE is ideal for local use (4B active params with ~10B “dense-equivalent” quality), but warns speculative decoding is a poor fit for MoE and that Claude Code + LM Studio can be flaky and slower than cloud or ollama-based setups.

---

### Comment pulse
- Local Claude via ollama → `ollama launch claude --model gemma4:26b` is trivial for some, but others see Gemma hang while other models work.  
- LM Studio Anthropic endpoint → lets Claude Code use Gemma locally; several users report it often “loses its place” and stalls—counterpoint: ollama’s API feels more reliable.  
- Performance concerns → 48 GB Framework-type desktops can chat, but agentic coding over real codebases is painfully slow even with decent GPUs.

---

### LLM perspective
- View: MoE + headless LM Studio makes serious, private assistants viable on single high-RAM machines, not just GPU servers.  
- Impact: Most useful for developers, small teams, and privacy-sensitive orgs wanting Claude-like workflows without sending code off-box.  
- Watch next: Better MoE-aware speculative decoding, stability of Claude Code against local Anthropic endpoints, and standardized config recipes for common hardware tiers.
