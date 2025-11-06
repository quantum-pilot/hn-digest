# The state of SIMD in Rust in 2025

- Score: 179 | [HN](https://news.ycombinator.com/item?id=45826348) | Link: https://shnatsel.medium.com/the-state-of-simd-in-rust-in-2025-32c263e5f53d

- TL;DR
  - Rust SIMD in 2025: choose autovectorization for zero-deps, portable SIMD crates for most workloads, and raw intrinsics for hardware-specific ports. x86 needs function multiversioning; ARM64 NEON is universal; WASM requires dual builds. std::simd remains nightly; wide is stable but lacks multiversioning; pulp and macerator are the pragmatic stable choices. Float-heavy loops block autovectorization unless you accept relaxed math; Rust 1.86 made many intrinsics safe. HN debate centers on fast‑math trade-offs, C#’s stronger stable SIMD, and why std::simd still isn’t stabilized.

- Comment pulse
  - Autovectorization limits with floats → IEEE‑754 reordering changes results; use relaxed math for reductions — counterpoint: dependency‑free loops still autovectorize fine.
  - C# has better stable SIMD → corporate backing, mature ecosystem; portable SIMD exists but often requires unsafe; LLVM auto‑vec can suffice.
  - Why std::simd isn’t stable → huge API surface, performance/usability balance, Rust’s strict stability guarantees, few maintainers, dependencies on other unstable pieces.

- LLM perspective
  - View: Use portable SIMD + multiversioning for x86; autovec for simple loops; intrinsics only for niche hotspots.
  - Impact: Libraries will converge on pulp/macerator until std::simd stabilizes; x86 feature dispatch remains boilerplate.
  - Watch next: std::simd stabilization plan, SVE/SVE2 support, faster feature detection and stable relaxed‑math flags.
