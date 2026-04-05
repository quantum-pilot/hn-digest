# Show HN: TurboQuant-WASM – Google's vector quantization in the browser

- Score: 126 | [HN](https://news.ycombinator.com/item?id=47639567) | Link: https://github.com/teamchong/turboquant-wasm

## TL;DR

TurboQuant‑WASM brings Google Research’s TurboQuant vector quantization algorithm to browsers and Node via WebAssembly with relaxed SIMD. It compresses high‑dimensional float vectors to ~3–4.5 bits per dimension while preserving dot products closely enough for similarity search. A small TypeScript API exposes encode/decode and fast dot products, including an 83× faster batched search path. Demos show text, image, and 3D Gaussian Splatting applications, and golden tests ensure bit‑identical results with the original Zig implementation.

## LLM perspective

- View: Client-side vector compression enables private, offline semantic search and embeddings-heavy apps without roundtrips to backend vector databases.  
- Impact: Most useful where bandwidth or storage is tight: web apps shipping many embeddings, 3D assets, or on-device RAG indexes.  
- Watch next: Benchmark against libraries like FAISS, ScaNN, and PQ implementations; profile real-world browser workloads and measure recall–latency–size tradeoffs.
