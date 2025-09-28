# GPT-OSS Reinforcement Learning

- Score: 148 | [HN](https://news.ycombinator.com/item?id=45392744) | Link: https://docs.unsloth.ai/new/gpt-oss-reinforcement-learning

TL;DR
Unsloth adds GRPO-based RL training for gpt-oss, with a custom inference stack delivering 3x speed, ~50% less VRAM, 8x longer context, and 4‑bit RL. It replaces FA3 with Flex Attention to keep O(N) memory and correct gradients for attention sinks, adds embedding offload, and ships a free Colab to train 20B on 15GB GPUs; 120B fits 80GB. They detail masking quirks and practical defenses against reward hacking. HN split: some hail democratized RL (sleep mode, toolchains); others prefer RAG and doubt gpt‑oss, while practitioners report strong results.

Comment pulse
- RL training is now accessible → vLLM sleep mode decouples inference memory from training, enabling larger runs on modest GPUs.
- Fine-tuning hurts generality; prefer RAG → limited data causes forgetting; gpt‑oss lags peers — counterpoint: users see strong instruction-following and RL wins on real tasks.
- Context engineering isn’t enough for computer-use/multimodal tasks → RL markedly improved success where prompt/RAG approaches stalled.

LLM perspective
- View: The real advance is an RL-ready attention/masking stack plus reward-hacking defenses, not just raw speed.
- Impact: Makes gpt‑oss RL reproducible on commodity GPUs; standardizes attention‑sink training semantics across T4–H100 hardware.
- Watch next: Independent evals on reasoning/code; FA3 sink‑backward fixes; vLLM RL support and 50% weight sharing integration.
