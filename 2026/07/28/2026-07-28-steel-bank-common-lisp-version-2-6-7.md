# Steel Bank Common Lisp version 2.6.7

- Score: 184 | [HN](https://news.ycombinator.com/item?id=49086971) | Link: https://sbcl.org/all-news.html?2.6.7

### TL;DR

The monthly release adds an interactive manual embedded in docstrings, declaration documentation support, ARM64 support in SB-SIMD, AVX512 on x86-64, broader SIMD coverage, and faster UTF-8 conversion paths. It also fixes ARM64, type-system, NaN, `CONCATENATE`, and `MULTIPLE-VALUE-CALL` issues while tuning allocation and compiler workloads. HN readers were most interested in SIMD, learning it currently requires explicit use rather than auto-vectorization. Discussion also ranged across Lisp-image deployment, modern Windows support, naming history, and a persistent documentation gap around memory arenas.

### Comment pulse

- SIMD support is explicit today → ARM64 and AVX512 additions expose intrinsics, but the compiler does not yet auto-vectorize ordinary Lisp.
- Interactive development shapes deployment imagination → readers envisioned image-based services, remote s-expression execution, and live production debugging without rebuilds or restarts.
- Documentation still lags capability → memory arenas exist through `NEW-ARENA` and `WITH-ARENA`, yet users found only an old internal note.

### LLM perspective

- **View:** Monthly releases advance mature runtimes through accumulated compiler, platform, documentation, and correctness work rather than headline features.
- **Impact:** Library authors can target newer CPU paths while users gain fewer architecture-specific miscompilations and more discoverable internals.
- **Watch next:** Track auto-vectorization, arena documentation, SIMD benchmarks, Windows regressions, and adoption of SB-MANUAL as the canonical source.
