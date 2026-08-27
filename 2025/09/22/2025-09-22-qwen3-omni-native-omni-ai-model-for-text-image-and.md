# Qwen3-Omni: Native Omni AI model for text, image and video

- Score: 270 | [HN](https://news.ycombinator.com/item?id=45336989) | Link: https://github.com/QwenLM/Qwen3-Omni

### TL;DR

Alibaba’s Qwen team released Apache-2.0-licensed Qwen3-Omni models that accept text, images, audio, and video and can stream text or speech responses. The repository claims leading results on many audio-video benchmarks, support for 119 text languages, 19 speech-input languages, and 10 speech-output languages, using a 30B-A3B mixture-of-experts Thinker–Talker design. HN reactions highlight impressive translation demonstrations and roughly 70GB weights, while noting uneven voice accents, slow English pacing, and current NVIDIA-oriented deployment friction.

### Comment pulse

- Local use looks plausible → commenters expect quantization could fit 24GB GPUs, though macOS inference support remains uncertain.
- Speech quality varies by language → Spanish seemed faster, while several Russian voices reportedly carried conspicuous accents.
- Open weights create strategic leverage → discussion links accessibility to privacy, efficiency pressure, and geopolitical restrictions.

### LLM perspective

- View: Native multimodality becomes meaningful when latency, speech quality, and deployment accessibility converge.
- Impact: Developers can prototype private voice-and-video agents without depending entirely on closed services.
- Watch next: Independent multilingual benchmarks, macOS ports, quantized quality, and complete vLLM audio-output support.
