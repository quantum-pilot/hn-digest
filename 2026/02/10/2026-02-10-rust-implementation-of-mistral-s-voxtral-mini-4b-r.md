# Rust implementation of Mistral's Voxtral Mini 4B Realtime runs in your browser

- Score: 380 | [HN](https://news.ycombinator.com/item?id=46954136) | Link: https://github.com/TrevorS/voxtral-mini-realtime-rs

### TL;DR

A Rust/Burn implementation brings Mistral’s 4B speech recognizer to native GPUs and browser tabs. Its Q4 GGUF path shrinks weights from roughly 9GB to 2.5GB and uses WASM, WebGPU, custom WGSL kernels, sharded loading, phased memory management, and quantized embeddings to fit browser limits; a full-precision native path and Apache-2.0 license round out the project. However, speed and accuracy benchmarks remain forthcoming. Demo users found transcription batch-oriented and slower than real time, especially versus Whisper or Parakeet, tempering enthusiasm for its nominal streaming design.

### Comment pulse

- The browser UI records then transcribes; a ring buffer could stream results, but respondents said current inference remains too slow for real time.
- Commenters preferred Parakeet V3 or ONNX Whisper on consumer hardware, judging small accuracy gains insufficient to offset latency.
- Open, on-premise operation drew business interest, while others asked for integration into Handy and transcribe-rs.

### LLM perspective

- View: The browser engineering is substantial, but the project’s real-time label currently describes architecture more than user-perceived latency.
- Impact: Client-side transcription improves privacy and deployment control, provided users can tolerate multi-gigabyte downloads and delayed output.
- Watch next: Published WER and speed results, incremental UI, model-load latency, sustained memory use, hardware coverage, and Handy integration.
