# Accelerating Gemma 4: faster inference with multi-token prediction drafters

- Score: 414 | [HN](https://news.ycombinator.com/item?id=48024540) | Link: https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/

### TL;DR
Google adds Multi-Token Prediction (MTP) “drafter” models to Gemma 4, using speculative decoding: a small model drafts several future tokens while the large model verifies them in parallel. This turns a single-token step into a multi-token jump, yielding up to roughly 3× higher throughput without hurting reasoning quality. Architectural tricks like KV‑cache sharing and embedder clustering keep overhead low, making big Gemma 4 variants usable on consumer GPUs and edge devices, with open Apache‑2.0 weights and broad tooling support.

---

### Comment pulse
- Gemma/Gemini feel faster and more token‑efficient than peers, often finishing tasks in a fraction of the time—counterpoint: errors can require extra correction turns, offsetting savings.  
- Local‑model users report major speedups from MTP in llama.cpp and prefer Gemma 4 26B over Qwen 27B in practice, despite benchmarks sometimes favoring Qwen.  
- Some see Google “carrying” Western open models and optimizing for efficiency and mass deployment, not just peak capability, in a still‑“dialup era” of LLM latency.

---

### LLM perspective
- View: Speculative decoding is becoming a standard inference feature, not a research curiosity, especially for mid‑to‑large local models.  
- Impact: Low‑latency coding agents, on‑device assistants, and small‑GPU enthusiasts gain most; cloud providers can stretch existing hardware further.  
- Watch next: Head‑to‑head benchmarks of MTP vs alternatives (e.g., flash‑attention variants, DFlash), plus broader support across runtimes and model families.
