# Zero-Copy GPU Inference from WebAssembly on Apple Silicon

- Score: 111 | [HN](https://news.ycombinator.com/item?id=47820195) | Link: https://abacusnoir.com/2026/04/18/zero-copy-gpu-inference-from-webassembly-on-apple-silicon/

### TL;DR
A Rust + Wasmtime experiment on Apple Silicon shows that a WebAssembly module’s linear memory can be directly shared with the GPU via Metal’s `makeBuffer(bytesNoCopy:)`, thanks to unified memory. Using `mmap` for page‑aligned buffers and Wasmtime’s custom allocator, the same physical bytes back both Wasm and GPU, eliminating copies and extra VRAM. Benchmarks show identical compute latency but halved memory use, and this enables stateful AI “actors” whose KV caches can be snapshotted, moved, and restored efficiently.

---

### Comment pulse
- UMA isn’t new → x86 iGPUs and old Macs already shared RAM; the novelty is the full Wasm→Metal zero‑copy chain — counterpoint: Apple’s unified memory still central here.  
- Why not just go native? → This mainly matters for sandboxed, mobile actors with GPU access, web distribution, and security/privacy guarantees.  
- AI-written style gripe → Phrases like “no copies, no serialization” trigger suspicion of LLM authorship; others argue tools assisting writing are no worse than calculators for math.

---

### LLM perspective
- View: This validates a practical pattern for GPU-accelerated, sandboxed runtimes where Wasm orchestrates and GPU computes without data marshaling.  
- Impact: Most useful for multi-tenant local agents, plugin systems, and browsers on UMA machines where isolation and performance both matter.  
- Watch next: Benchmarks on larger models, non-Apple UMA hardware, and alignment with emerging WebAssembly memory-control proposals.
