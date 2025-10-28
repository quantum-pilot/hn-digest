# How I turned Zig into my favorite language to write network programs in

- Score: 308 | [HN](https://news.ycombinator.com/item?id=45716109) | Link: https://lalinsky.com/2025/10/26/zio-async-io-for-zig.html

- TL;DR
  - An engineer built Zio, a Go‑style async I/O and concurrency library for Zig, using stackful coroutines with fixed stacks to make network code feel synchronous while remaining nonblocking. It supports async net/file I/O, channels, and integrates with Zig’s Reader/Writer, claiming single‑threaded performance beating Go and Rust/Tokio. HN debates the “virtually free” context switches, stack sizing and predictability, and Zig’s evolving I/O model (0.16’s std.Io). Some advocate waiting; others argue Zig is usable now. Timeouts/cancellation remain tricky.

- Comment pulse
  - Stackful is fast enough → Fewer allocations and synchronous style; fixed stacks enable simpler state. — counterpoint: mispredicted returns and cache effects dominate; benchmark carefully.
  - Wait for Zig 0.16 I/O → Interfaces are in flux; adopting now means refactors; buffered Reader/Writer softens breakage.
  - Stack size and timeouts are pitfalls → Fixed stacks risk overflow/waste; cancellation and timeouts are unsolved, hardest part of async.

- LLM perspective
  - View: Zio reclaims Go-like ergonomics in Zig without language async, pushing a pragmatic runtime approach.
  - Impact: Could make Zig viable end-to-end for servers, not just hot loops; encourages libs to adopt std.Io compatibility.
  - Watch next: Zig 0.16 std.Io landing, Zio implementing it; credible multi-thread benchmarks; timeout/cancellation API and stack-sizing guidance.
