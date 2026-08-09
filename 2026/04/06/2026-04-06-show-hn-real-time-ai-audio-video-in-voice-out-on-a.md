# Show HN: Real-time AI (audio/video in, voice out) on an M3 Pro with Gemma E2B

- Score: 261 | [HN](https://news.ycombinator.com/item?id=47652007) | Link: https://github.com/fikrikarim/parlor

### TL;DR

Parlor is an Apache-licensed research preview for private, real-time voice-and-vision conversations entirely on local hardware. A browser captures PCM audio and camera frames, performs Silero voice-activity detection, and streams them to FastAPI; Gemma 4 E2B handles speech and images through LiteRT-LM, while Kokoro returns sentence-streamed speech through MLX or ONNX. On an M3 Pro, the author reports roughly 2.5–3 seconds end-to-end and 83 generated tokens per second. It supports interruption, needs about 3 GB RAM, and automatically downloads roughly 2.6 GB of model files plus TTS assets.

### Comment pulse

- A hands-free workshop assistant for timers, calculations, and notes resonated with users frustrated by locked phones and advertising-oriented assistants.
- Commenters saw the demo as evidence that local models increasingly reproduce capabilities recently confined to hosted systems on ordinary hardware.
- Limited testing found multilingual switching better than expected; another builder preferred Qwen 0.8B because Gemma E2B remained comparatively heavy.

### LLM perspective

- **View:** The compelling achievement is a complete conversational loop, not any isolated model benchmark.
- **Impact:** Local multimodality could make language tutoring and situational assistance sustainable without per-session server costs or cloud dependence.
- **Watch next:** Longer-session stability, language evaluations, Linux performance, phone-class deployment, tool integrations, privacy hardening, and latency under noisy conditions.
