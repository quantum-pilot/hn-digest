# Cache-friendly, low-memory Lanczos algorithm in Rust

- Score: 100 | [HN](https://news.ycombinator.com/item?id=45889891) | Link: https://lukefleed.xyz/posts/cache-friendly-low-memory-lanczos/

- TL;DR
  - The post implements a two-pass Lanczos in Rust that stores only O(n) memory: pass 1 records the tridiagonal scalars; pass 2 regenerates the basis to accumulate the solution, doubling matvecs. On large sparse problems, cache-local accumulation often offsets the extra work by avoiding the dense V_k*y bandwidth bottleneck; dense cases revert to ~2× slower. Benchmarks and faer-based engineering (MemStack, LinOp, SIMD) support this. HN discussion probes orthogonality/accuracy trade-offs, communication-avoiding alternatives, and Rust vs Julia/BLAS ecosystems.

- Comment pulse
  - Two-pass wins when basis gemv is bandwidth-bound → Cache-local axpy accumulation beats streaming V_k; matches comm-avoiding. — counterpoint: dense cases are compute-bound, yielding ~2× slowdown.
  - Accuracy concern → Without reorthogonalization, orthogonality degrades; acceptable for matrix-function actions at moderate k, not for eigenvectors or very long runs.
  - Rust in numerics → Promising ergonomics and safety; faer shows progress, but C/Fortran BLAS/LAPACK maturity and Julia packages still dominate ecosystems.

- LLM perspective
  - View: Compute-for-bandwidth trade pays when sparse matvecs are efficient and V_k*y is memory-bound; engineering details matter.
  - Impact: Enables larger n or k under tight memory; benefits PDE solvers, KKT systems, and matrix exponential or sign applications.
  - Watch next: Benchmark against communication-avoiding/block Lanczos; add optional reorthogonalization, mixed precision, GPU operators; publish reproducible kernels and roofline analyses.
