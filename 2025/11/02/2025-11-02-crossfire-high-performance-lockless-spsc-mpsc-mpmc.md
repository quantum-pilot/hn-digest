# Crossfire: High-performance lockless spsc/mpsc/mpmc channels for Rust

- Score: 94 | [HN](https://news.ycombinator.com/item?id=45787571) | Link: https://github.com/frostyplanet/crossfire-rs

- TL;DR
  - Crossfire is a Rust crate offering lockless SPSC/MPSC/MPMC channels that work in both async and blocking contexts. v2.1 swaps crossbeam-channel for a modified crossbeam-queue and reports sizable throughput gains (async and some blocking). APIs are cancellation-safe with timeout helpers for tokio/async-std; a backoff auto-detect improves behavior on VPS. CI spans x86/ARM and multiple runtimes, with tokio 1.48 recommended on ARM. HN readers welcome the ambition but question atomic-memory correctness and robustness, and debate cancellation safety, “futurelock,” and Go-style channel-centric Rust.

- Comment pulse
  - Memory-ordering in atomics seems risky → redundant acquires, missing release chains, double-close behavior, no Loom tests; could heisenbug on ARM — counterpoint: works fine for.
  - Cancellation-safety is distinct from futurelock → futurelock concerns deadlocks via blocked futures; cancellation can help, while cancellation-safety defines atomicity and cleanup guarantees.
  - Go-style channels in Rust can work → prefer threads for compute-bound parallelism, async for I/O; channels vs mutexes is an orthogonal design choice.

- LLM perspective
  - View: Ambitious lockless design plus runtime-agnostic async/blocking bridge; performance hinges on spinning and careful waker management.
  - Impact: Could displace crossbeam-channel/Tokio mpsc where latency matters; better bounded/unbounded options across mixed async/blocking systems.
  - Watch next: Loom-model tests, ARM weak-order benchmarks, power/CPU impact of spinning, comparisons vs flume/tokio mpsc under varied loads.
