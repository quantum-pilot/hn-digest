# Rust implementation of Mistral's Voxtral Mini 4B Realtime runs in your browser

- Score: 380 | [HN](https://news.ycombinator.com/item?id=46954136) | Link: https://github.com/TrevorS/voxtral-mini-realtime-rs

### TL;DR

Rust port of Mistral’s Voxtral Mini 4B Realtime ASR runs locally and fully in-browser via WASM + WebGPU, using a 9 GB fp32 path for native and a 2.5 GB Q4_0 GGUF path for native + browser. The author solves tough browser limits (2 GB allocations, 4 GB address space, huge embeddings, no sync GPU readback) with sharded weights, phased loading, compressed embeddings, and custom WGSL. HN discussion focuses on true “realtime” UX, comparisons to Whisper/Parakeet, and enthusiasm for open, on‑prem models and tool integrations.

---

### Comment pulse

- Voxtral ecosystem is growing → Rust, C, and CUDA implementations exist, giving options for different platforms and performance profiles.  
- Realtime UX questioned → current Rust/Q4 path isn’t as snappy as GPU-hosted Voxtral, Whisper ONNX, or Nvidia Parakeet V3 on consumer hardware — counterpoint: UI + buffering could hide latency.  
- Open, on‑prem AI praised → Mistral’s model plus Apache-2.0 code aligns with businesses wanting self-hosted speech systems and may mirror a “Red Hat moment.”

---

### LLM perspective

- View: This is a strong proof that multi‑billion‑parameter ASR can run fully client‑side with careful systems work.  
- Impact: Developers gain a permissive, Rust-based stack for offline speech features in desktop apps, browsers, and tools like Handy.  
- Watch next: Published WER/speed benchmarks, streaming UI, tighter CUDA/WebGPU kernels, and adoption in popular OSS assistants and IDE extensions.
