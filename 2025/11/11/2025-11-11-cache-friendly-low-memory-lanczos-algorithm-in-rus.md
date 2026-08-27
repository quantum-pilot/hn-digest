# Cache-friendly, low-memory Lanczos algorithm in Rust

- Score: 100 | [HN](https://news.ycombinator.com/item?id=45889891) | Link: https://lukefleed.xyz/posts/cache-friendly-low-memory-lanczos/

### TL;DR

The article implements a two-pass Lanczos method in Rust for approximating matrix-function actions on large sparse Hermitian systems. Instead of retaining an O(nk) basis, pass one stores tridiagonal coefficients; pass two regenerates vectors and accumulates the result, reducing memory to O(n) while doubling matrix-vector products. The author's benchmarks show flat memory and, for sparse problems, less than a twofold slowdown because cache-friendly reconstruction offsets work. Dense cases approach the expected 2:1 penalty. The code is exploratory, not production-ready.

### Comment pulse

- Readers asked whether loss of orthogonality limits long or ill-conditioned runs; the author reported degradation there.
- Discussion welcomed modern-language numerical work while noting Rust's ecosystem still trails decades of C and Fortran infrastructure.

### LLM perspective

- View: The design succeeds when memory traffic costs more than recomputing Krylov vectors.
- Impact: Large sparse workloads can trade predictable extra arithmetic for dramatically lower peak memory.
- Watch next: Reorthogonalization strategies, broader matrices, reproducible benchmarks, and production-grade numerical validation.
