# The state of SIMD in Rust in 2026

- Score: 207 | [HN](https://news.ycombinator.com/item?id=49844629) | Link: https://shnatsel.github.io/state-of-simd-rust-2026/

### TL;DR

Rust SIMD support has matured through improved autovectorization, stabilized algebraic floating-point operations, safer intrinsics, and several production libraries. The author, now a Fearless SIMD maintainer, compares std::simd, fearless_simd, wide, pulp, and macerator across multiversioning, vector widths, generics, instruction sets, and safety. No option solves everything: std::simd remains nightly, trigonometry is weak, compiler lowering can sabotage intrinsics, and x86 dispatch is complex. HN adds ARM documentation concerns, deployment cases where AVX2 baselines suffice, and requests for stable portable SIMD and better RISC-V coverage.

### Comment pulse

- Portable abstractions remain valuable → they can beat fragile autovectorization while avoiding the difficulty and unsafety of manual intrinsics.
- Deployment determines dispatch strategy → controlled servers, games, and architecture-specific distributions can require AVX2 instead of maintaining broad fallbacks.
- ARM simplifies its baseline but obscures details → optional features and poorly documented execution characteristics complicate reliable tuning.

### LLM perspective

- View: Rust now has credible SIMD paths, but selecting one requires matching portability, dispatch, generics, and numerical needs.
- Impact: Library authors can gain safety without abandoning performance, while accepting benchmarking across compilers and hardware as permanent work.
- Watch next: Track std::simd stabilization, trigonometric implementations, target-feature RFCs, compiler regressions, Cranelift coverage, and representative RISC-V hardware.
