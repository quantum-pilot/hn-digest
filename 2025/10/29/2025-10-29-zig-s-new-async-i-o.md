# Zig's New Async I/O

- Score: 300 | [HN](https://news.ycombinator.com/item?id=45746020) | Link: https://andrewkelley.me/post/zig-new-async-io-text-version.html

### TL;DR

Zig’s newly landed `std.Io` introduces preview async primitives for the planned 0.16.0 release. Programs receive an I/O implementation much like an allocator, then use futures, idempotent `await` and `cancel`, queues, and a distinct `concurrent` operation when execution truly requires parallel progress. Examples show why awaiting every task prevents leaks, how deferred cancellation restores ordinary `try` and resource-management patterns, and how confusing asynchrony with concurrency can deadlock. Threaded support exists now; evented coroutine implementations remain experimental, and the APIs are explicitly unsettled.

### Comment pulse

- Skeptics worry injected I/O behavior weakens local reasoning and merely hides function coloring.
- Supporters see a testable interface that can select threaded, evented or domain-specific implementations without rewriting libraries.

### LLM perspective

- View: Separating expressed asynchrony from required concurrency is unusually honest, but shifts complexity into interface contracts.
- Impact: Libraries may become runtime-agnostic while demanding careful cancellation, capability and blocking-operation discipline.
- Watch next: Real applications must expose semantic surprises before the interface and coroutine strategy stabilize.
