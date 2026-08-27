# The state of SIMD in Rust in 2025

- Score: 179 | [HN](https://news.ycombinator.com/item?id=45826348) | Link: https://shnatsel.medium.com/the-state-of-simd-in-rust-in-2025-32c263e5f53d

### TL;DR

Rust developers can pursue SIMD through compiler autovectorization, abandoned iterator-style experiments, portable vector abstractions, or architecture-specific intrinsics. The article recommends nightly-only `std::simd` when acceptable, `wide` without runtime multiversioning, and `pulp` or the less-proven `macerator` when dispatch matters. Raw intrinsics remain verbose and platform-specific, though most became safe to call in Rust 1.86. Commenters challenged the article’s blanket statement about float autovectorization and debated why stable portable SIMD still trails C#, citing API permanence, complexity, and limited contributor capacity.

### Comment pulse

- Float reductions can change results when reordered, but commenters noted independent float loops may still vectorize, narrowing the article’s claim.
- `std::simd` stabilization divides users between demanding a core performance feature and accepting ecosystem crates while its API remains unsettled.

### LLM perspective

- View: Rust has workable SIMD paths, but portability, stable APIs, and runtime dispatch rarely arrive together.
- Impact: Performance-sensitive libraries must choose between nightly dependence, ecosystem risk, target limits, or duplicated low-level implementations.
- Watch next: `std::simd` blockers, SVE support, crate adoption, compiler regressions, and benchmarks across x86, ARM, and WebAssembly.
