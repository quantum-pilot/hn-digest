# Zero-Copy GPU Inference from WebAssembly on Apple Silicon

- Score: 111 | [HN](https://news.ycombinator.com/item?id=47820195) | Link: https://abacusnoir.com/2026/04/18/zero-copy-gpu-inference-from-webassembly-on-apple-silicon/

### TL;DR

Driftwood demonstrates a zero-copy path from WebAssembly linear memory to Apple Silicon’s GPU: a custom Wasmtime allocator supplies page-aligned mmap memory, while Metal wraps the identical pointer as a buffer. A 128×128 matrix multiplication returned 16,384 correct results, adding only 0.03 MB RSS versus 16.78 MB for copying. Llama 3.2 1B then generated tokens at roughly 9 ms each, and persisted KV-cache state restored 5.45× faster than re-prefilling at 24 tokens. Commenters question novelty and whether native inference already solves the practical problem.

### Comment pulse

- The author clarified that shared CPU/GPU memory is established; the contribution is composing Wasmtime allocation, Metal wrapping, and usable inference performance.
- Native code remains simpler locally — counterpoint: sandboxed actors gain isolation, distribution, and resumable state without copy overhead.
- Skeptics want evidence that transfer costs matter against optimized engines already overlapping computation and communication.

### LLM perspective

- Benchmark larger models, longer contexts, concurrent actors, memory pressure, and snapshot migration across machines.
- Model swaps require compatible cache semantics; a model-agnostic format alone cannot guarantee reuse.
- Security analysis must test whether GPU-visible shared memory weakens Wasm isolation assumptions.
