# Training an LLM in Swift, Part 1: Taking matrix mult from Gflop/s to Tflop/s

- Score: 209 | [HN](https://news.ycombinator.com/item?id=48085685) | Link: https://www.cocoawithlove.com/blog/matrix-multiplications-swift.html

### TL;DR

Matt Gallagher optimizes GPT-2 training matrix multiplication in Swift on an M3 Max without production libraries. Basic Swift ran at 2.8 Gflop/s, 15–20× slower than C, mainly from array copy-on-write checks and conservative floating point. MutableSpan, relaxed FMA, InlineArray unrolling, and `concurrentPerform` pushed CPU Swift past C; AMX and tiled Metal reached 1.1 Tflop/s, a 382× speedup. The result still produces under 12 tokens/s, so the author recommends Apple frameworks. HN praised the tutorial but cautioned that `-ffast-math` is broader than needed and noted how difficult GPU peak utilization is.

### Comment pulse

- Readers valued a rare, reproducible Swift optimization path spanning compiler output, memory semantics, threading, matrix accelerators, and GPU kernels.
- For FMA, `-ffp-contract=fast` is safer than blanket `-ffast-math`, which permits other transformations that can damage numerical accuracy.
- M3 Max’s theoretical 15 Tflop/s misleads — counterpoint: workload ceilings, memory locality, and tuned kernels matter more than headline GPU throughput.

### LLM perspective

- View: The 382× gain came from matching computation to memory layout and hardware hierarchy, not from changing the mathematical algorithm.
- Impact: Swift can match C for numeric loops, but safety and readability erode once manual parallelism and undocumented hardware enter.
- Watch next: Production-library comparisons across BLAS, BNNS, CoreML, and MPSGraph; M4 SME results; power efficiency; larger models; numerical-error analysis.
