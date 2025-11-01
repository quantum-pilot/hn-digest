# Zig's New Async I/O

- Score: 300 | [HN](https://news.ycombinator.com/item?id=45746020) | Link: https://andrewkelley.me/post/zig-new-async-io-text-version.html

- TL;DR
    - Andrew Kelley previews Zig 0.16’s std.Io: a pluggable I/O interface with async/await futures, explicit cancel, queues, and a distinction between asynchrony (io.async) and true concurrency (io.concurrent). Await/cancel are idempotent, enabling safe error handling and resource cleanup; cancellation accelerates failure paths. A default Threaded backend oversubscribes; single-threaded builds surface ConcurrencyUnavailable. Future backends (io_uring, kqueue; coroutines) are prototyped. HN debates function coloring and predictability across libraries vs. the benefits of capability-style Io parameters akin to Haskell IO or Java virtual threads.

- Comment pulse
    - Design hides function coloring; shared Io hurts local reasoning, risks LSP violations → behavior shifts across libraries. — counterpoint: interface semantics + testing across backends.
    - Pluggable Io unifies evented and threaded runtimes → same APIs; feels like Haskell IO or Java virtual threads without monkey-patching.
    - Async i/o ergonomics vs multithreading: some prefer BEAM, Java/.NET, or JS promises; others cite throughput/memory trade-offs and inevitable “colored” call graphs.

- LLM perspective
    - View: Treat Io as an explicit capability; cancellation + idempotent await simplify cleanup patterns and eliminate common leak/timeout footguns.
    - Impact: Libraries will accept Io and expose cancellable futures; runtime swapping encourages benchmarks and clearer performance contracts.
    - Watch next: Measure Threaded vs io_uring/kqueue; stress-test single-threaded ConcurrencyUnavailable; track stackless/stackful coroutine features and maximum-stack tooling.
