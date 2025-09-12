# Qwen3 30B A3B Hits 13 token/s on 4xRaspberry Pi 5

- Score: 347 | [HN](https://news.ycombinator.com/item?id=45148237) | Link: https://github.com/b4rtaz/distributed-llama/discussions/255

- TL;DR
  - A 4× Raspberry Pi 5 (8GB) cluster using Distributed Llama v0.16.0 runs Qwen3‑30B‑A3B (MoE, quantized) at 13.0 tokens/s generation (14.3 eval) over gigabit Ethernet, needing ~5.5 GB RAM per board. It showcases shard‑friendly MoE enabling interactive, fully local inference on low‑power hardware. HN compares with alternatives—used Apple Silicon (Asahi), x86 mini PCs, RK3588 SBCs—and cites similar single‑CPU results. Discussion weighs ROI (dev tools, context window) and the promise/risks of LLM‑powered toys for kids.

- Comment pulse
  - Pi cluster is neat → x86 minis, used MacBooks, or RK3588 boards can match speed, simpler setup — counterpoint: MoE sharding benefits small-node clusters.
  - Value uncertain → Devs want larger context windows; $500 for 4 Pis is hard to justify versus Claude; many Pi clusters sit mostly idle.
  - Edge toys excite people → Local, talking toys with memory seem near; others warn about children’s cognition, privacy, and unintended behaviors.

- LLM perspective
  - View: Open-source sharding (Distributed Llama v0.16) achieves low overhead on gigabit Ethernet, making 30B MoE quantized models responsive on SBC clusters.
  - Impact: Edge and lab users get air-gapped assistants, copilots, and chatbots without GPUs; lower cost, power, and noise.
  - Watch next: Head-to-head vs x86 minis/RK3588; NPU offload support; shrink to 1–2 Pis; standardized model/tokenizer compatibility.
