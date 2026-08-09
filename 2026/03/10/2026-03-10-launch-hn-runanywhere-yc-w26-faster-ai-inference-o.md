# Launch HN: RunAnywhere (YC W26) – Faster AI Inference on Apple Silicon

- Score: 173 | [HN](https://news.ycombinator.com/item?id=47326101) | Link: https://github.com/RunanywhereAI/rcli

### TL;DR

RunAnywhere presents RCLI, an MIT-licensed macOS voice assistant and demo for its proprietary MetalRT inference engine. The local pipeline combines speech recognition, small language models, speech synthesis, 38 system actions, and hybrid document retrieval, claiming up to 550 tokens per second and sub-200-millisecond voice latency on M3-or-newer Macs; M1 and M2 fall back to llama.cpp. The broader pitch is on-device AI infrastructure, not merely an assistant. Early commenters liked the speed and privacy but reported installation and action-grounding failures and found the product positioning confusing.

### Comment pulse

- Local execution improves privacy and latency → RCLI keeps speech, documents, and actions on the Mac.
- A demo exposed false success reporting → opening Safari worked, while navigation failed despite a spoken confirmation.
- Product identity remains blurry → the team frames RCLI as a showcase for MetalRT’s broader runtime ambitions.

### LLM perspective

- **View:** Verified action outcomes matter more than raw token throughput for a trustworthy assistant.
- **Impact:** Mac developers gain a local stack, while MetalRT’s proprietary license limits full openness.
- **Watch next:** Reproducible benchmarks, M1/M2 acceleration, larger-model tests, diarization, and reliable tool-result grounding.
