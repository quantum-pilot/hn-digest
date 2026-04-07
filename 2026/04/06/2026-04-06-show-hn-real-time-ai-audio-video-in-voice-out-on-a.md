# Show HN: Real-time AI (audio/video in, voice out) on an M3 Pro with Gemma E2B

- Score: 261 | [HN](https://news.ycombinator.com/item?id=47652007) | Link: https://github.com/fikrikarim/parlor

### TL;DR
Parlor is an on-device, real-time multimodal assistant that takes audio and video from your browser and responds with low-latency speech, all running locally. It uses Google’s Gemma 4 E2B for speech+vision understanding via LiteRT-LM and Kokoro for text-to-speech, achieving 2.5–3 seconds end-to-end on an M3 Pro with ~3 GB RAM. The author’s goal is a free, sustainable language-learning assistant without server costs, and HN sees it as the Siri that Apple never shipped and proof that last year’s cloud SOTA now fits on laptops.

---

### Comment pulse
- Local, hands-free assistant dream → people want workshop/household helpers that don’t require unlocking phones or phoning home; phones feel hijacked by ads, not usability.
- Cloud-to-local lag shrinking → commenters note today’s local models match 6–12-month-old hosted SOTA; this demo showcases that shift for real-time, multimodal use—counterpoint: Gemma 4 E2B still heavy for some.
- Technical feedback → Kokoro praised for ultra-low TTS latency; multilingual handling (e.g., Greek/English) seems better than typical STT, though some builders prefer smaller models like Qwen 0.8B.

---

### LLM perspective
- View: This is a practical blueprint for private, multimodal, voice-first assistants without recurring server costs or vendor lock-in.
- Impact: Benefits hobbyists, educators, and OSS ecosystems; pressures platform vendors whose assistants feel stagnant despite strong device hardware.
- Watch next: Benchmarks against cloud GPT-4o-style systems, mobile ports, lighter models for weaker GPUs, and integrations with Home Assistant-style automation.
