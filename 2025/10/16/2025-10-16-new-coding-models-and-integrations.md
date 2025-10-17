# New coding models and integrations

- Score: 205 | [HN](https://news.ycombinator.com/item?id=45601834) | Link: https://ollama.com/blog/coding-models

- TL;DR
  - Ollama adds two top-tier coding models—GLM-4.6 and Qwen3‑Coder‑480B—to its cloud, updates Qwen3‑Coder‑30B for better tool use, and ships turnkey integrations for VS Code, Zed, Droid, plus a simple cloud API. You can run 480B locally only with ~300GB VRAM; otherwise use cloud endpoints. HN reports strong GLM‑4.6 reasoning and easy, cheap access via z.ai/Claude Code; a fresh Vulkan backend promises broader GPU support. Some doubt laptop‑local coding performance, suggesting cheap hosted options like DeepSeek; others seek speed/limits vs Anthropic/OpenAI.

- Comment pulse
  - GLM-4.6 is strong and cheap → Users report excellent reasoning (Lean lemmas) and easy use via Claude Code with z.ai; $3/month via env var swap.
  - Vulkan compute broadens hardware support → Experimental merge enables AMD GPUs without ROCm, Intel GPUs, and iGPUs; potentially accelerates many previously unsupported devices.
  - Local laptop models disappoint for short coding → Slow, low-quality outputs reported; deepseek via openrouter is cheap alternative — counterpoint: Others rate GLM-4.6 when hosted.

- LLM perspective
  - View: Ollama shifts coding assistants toward cloud-hosted, tool-integrated big models while retaining local endpoints for flexibility.
  - Impact: Developers on AMD/Intel GPUs gain access via Vulkan; teams can swap providers in editors without rewiring workflows.
  - Watch next: Independent benchmarks vs Claude 3.5/DeepSeek, latency/limits of Ollama Cloud, and stability of Vulkan path across consumer GPUs.
