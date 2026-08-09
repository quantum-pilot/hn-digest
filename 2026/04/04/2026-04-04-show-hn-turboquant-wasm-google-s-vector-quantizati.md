# Show HN: TurboQuant-WASM – Google's vector quantization in the browser

- Score: 126 | [HN](https://news.ycombinator.com/item?id=47639567) | Link: https://github.com/teamchong/turboquant-wasm

### TL;DR

TurboQuant-WASM packages a Zig implementation of Google Research’s TurboQuant algorithm as a roughly 12KB-gzipped WebAssembly module for browser and Node.js vector compression. It exposes TypeScript methods to encode, decode, and compute individual or batched dot products without decompression, using relaxed SIMD and claiming roughly sixfold compression at about 4.5 payload bits per dimension. Golden-value tests match the reference implementation, while demos cover text/image search and Gaussian splats. It requires modern runtimes; the README reports an 83× batch speedup over repeated WASM calls, not over uncompressed float search.

### Comment pulse

- One implementer found comparable retrieval quality and major storage savings, but raw float32 searches remained faster without GPU acceleration.
- A critic reported drastic demo latency and suggested simpler compression — counterpoint: the author revised performance and requested a retest.
- Other commenters welcomed the release, particularly its browser use cases and Gaussian-splat demonstration.

### LLM perspective

- **View:** This is primarily a bandwidth and storage optimization, not an automatic search-speed improvement.
- **Impact:** Smaller embeddings could make richer client-side retrieval practical where download size matters more than peak CPU latency.
- **Watch next:** Independent comparisons against float32, 8-bit quantization, and trained OPQ across browsers, dimensions, datasets, and batch sizes.
