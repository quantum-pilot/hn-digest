# Turbovec – Google's TurboQuant for vector search in Rust

- Score: 293 | [HN](https://news.ycombinator.com/item?id=49349898) | Link: https://github.com/RyanCodrai/turbovec

### TL;DR

turbovec is a Rust/Python vector index implementing Google Research’s TurboQuant: random rotation, 2- or 4-bit scalar quantization, optional per-coordinate calibration, and SIMD scoring. It claims to shrink 10 million 1,536-dimensional vectors from 31GB to about 4GB, accept online inserts without retraining, persist changes incrementally, delete stable IDs in constant time, and apply allowlists inside search kernels. On 100,000-vector tests it beat FAISS IndexPQFastScan speed while roughly matching or improving recall in most cells. Commenters liked compression and removal performance but questioned FAISS as a state-of-the-art baseline and cited RaBitQ alternatives.

### Comment pulse

- The value proposition is memory, speed, and online operations, not universal nearest-neighbor leadership; other indexes optimize different tradeoffs.
- Published scripts and results aid reproduction—counterpoint: independent comparisons across modern libraries and datasets remain missing.
- README prose felt machine-generated to some commenters, potentially hurting adoption despite extensive implementation detail.

### LLM perspective

- View: This is a strong engineering package around a quantizer, but comparator choice narrows its performance conclusion.
- Impact: Local retrieval workloads can hold larger corpora in RAM while updating and filtering indexes cheaply.
- Watch next: Broader benchmarks, billion-scale recall and latency, SQLite bindings, concurrency, crash tests, calibration drift, and independent reproduction.
