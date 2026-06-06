# Async Rust never left the MVP state

- Score: 421 | [HN](https://news.ycombinator.com/item?id=48019163) | Link: https://tweedegolf.nl/en/blog/237/async-rust-never-left-the-mvp-state

## TL;DR

The post dissects how Rust’s async/await transformation into state machines has barely been optimized since stabilization, causing MIR bloat, larger binaries, and missed performance, especially on embedded targets. The author shows that trivial futures still carry `Unresumed/Returned/Panicked` states and panicking branches that LLVM often cannot remove, and proposes compiler changes: optional non-panicking completed futures, skipping state machines for futures without `await`, inlining single-`await` async functions, and collapsing equivalent states. HN discussion focuses on Tokio’s dominance, async vs threads, and Rust’s reliance on panics.

---

## Comment pulse

- Tokio monoculture concern → many server/web crates assume Tokio; executor-agnostic design takes discipline. — counterpoint: embedded and other domains use Embassy, smol, etc. successfully.  

- Async vs threads → async seen by some as overcomplicated; others argue OS threads are too heavyweight and poorly scheduled for massive I/O concurrency.  

- Panics debate → some want a provable “no-panic” Rust subset to shrink binaries; others stress panics are memory-safe and crucial for ergonomics and invariants.

---

## LLM perspective

- View: Targeting MIR-level async optimizations is pragmatic; LLVM can’t reliably undo structural inefficiencies introduced upstream.  

- Impact: Biggest wins for embedded, WASM, and high-concurrency servers where binary size and per-future overhead directly limit capacity.  

- Watch next: rustc experiments behind flags, benchmarks on real services/firmware, and Rust Project Goal progress through RFCs and funding commitments.
