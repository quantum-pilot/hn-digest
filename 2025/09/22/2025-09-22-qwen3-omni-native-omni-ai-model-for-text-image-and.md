# Qwen3-Omni: Native Omni AI model for text, image and video

- Score: 270 | [HN](https://news.ycombinator.com/item?id=45336989) | Link: https://github.com/QwenLM/Qwen3-Omni

- TL;DR
  - Alibaba’s Qwen3‑Omni is an end‑to‑end, open‑weight multimodal model (Apache‑2.0) that natively handles text, images, audio, and video and streams speech replies in real time. A MoE Thinker–Talker design underpins SOTA claims on many audio/video benchmarks, with 119 text languages plus multilingual speech I/O. Weights are ~70GB; vLLM and quantization make local runs feasible on 24–48GB GPUs. HN praises live translation/voice, debates reliance on Chinese open models and potential US bans, and asks about macOS/NVIDIA support.

- Comment pulse
  - Open Chinese models could win home AI → open weights, privacy; dual‑3090 + ESP32 setups work — counterpoint: few will pay; bans could block downloads.
  - Local runs look doable → ~70GB weights; Q4 quantization targets 24GB GPUs; multi‑GPU and 5090 questions; macOS inference engine/port remains unclear.
  - Voice features are fun and capable → real‑time video‑in to speech‑out translation impresses; character voices entertain; accents vary when switching languages.

- LLM perspective
  - View: End‑to‑end speech I/O plus native AV is the differentiator over stitched ASR+LLM+TTS stacks.
  - Impact: Open Apache‑2.0 weights shift developer energy to efficient inference, quantization, and on‑device assistants.
  - Watch next: vLLM audio output release, 24GB quantized benchmarks, M‑series/macOS path, and any US export or download restrictions.
