# Async Rust never left the MVP state

- Score: 421 | [HN](https://news.ycombinator.com/item?id=48019163) | Link: https://tweedegolf.nl/en/blog/237/async-rust-never-left-the-mvp-state

### TL;DR

The author argues Rust’s async lowering still emits unnecessarily bulky state machines, especially painful on embedded targets. Even futures with no `await` keep Unresumed, Returned, and Panicked states; nested single-await futures are not inlined before LLVM; equivalent branch states remain duplicated; and post-completion panic paths inhibit optimization. Compiler experiments replacing the release-mode panic with `Pending` cut firmware size 2–5%, removing needless state machines saved 0.2%, and together improved a synthetic x86 benchmark about 3%. He seeks €30,000 to implement and benchmark four MIR-level optimizations. Discussion welcomed specifics despite the title.

### Comment pulse

- Readers praised the compiler deep dive — counterpoint: several called “never left MVP” dramatic because measured trivial-case overhead is modest.
- Executor agnosticism works from servers to Embassy microcontrollers, though Tokio’s de facto dominance worries some.
- The model debate split by workload: compute-bound work favors threads; bandwidth-bound systems benefit from explicit scheduling.

### LLM perspective

- MIR is the right layer because late LLVM passes lose async structure and cannot reliably collapse nested futures.
- Embedded and WebAssembly users gain most; servers need realistic workload evidence before prioritizing compiler complexity.
- Watch funding, semantic review of post-completion behavior, compile-time cost, and representative binary benchmarks.
