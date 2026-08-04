# How Our Rust-to-Zig Rewrite Is Going

- Score: 386 | [HN](https://news.ycombinator.com/item?id=48933149) | Link: https://rtfeldman.com/rust-to-zig

### TL;DR

After 487 days, Roc’s compiler rewrite from Rust to Zig has reached feature parity, though it is not yet a release. The redesign adds hot loading, deterministic cross-compilation, allocation-free routing, arena layouts, direct disk caches, and LLVM bitcode emission. A Zig nightly rebuilds today’s 464,000-line tree in 35 ms, versus 3.4 seconds for the smaller Rust tree, but stable Zig currently breaks that mode. The team reports two compiler use-after-free bugs while missing Rust’s borrow checker, automatic cleanup, private fields, dead-code detection, and release compatibility.

### Comment pulse

- Memory-safety claims drew scrutiny → commenters said ReleaseSafe lacks reliable temporal checks and challenged whether compilation itself requires unsafe operations.
- Language selection looked underexplored → critics proposed OCaml or self-hosting experiments and argued algorithms dominate compiler speed — counterpoint: layout control can change constants dramatically.
- Build speed is compelling but deferred → 35-ms incrementals require a prerelease and x86-64, while Rust’s supported builds improved substantially during the rewrite.

### LLM perspective

- **View:** Project fit drove the choice: Roc prioritized arena memory, compiler reuse, layout control, cross-compilation, and iteration latency.
- **Impact:** Feature parity validates feasibility, but unfinished docs, stable-toolchain gaps, safety disputes, and migration costs still separate milestone from release.
- **Watch next:** Verify stable incremental builds, independent memory-safety testing, cold-build performance, real project migrations, cache correctness, and the 0.1 release.
