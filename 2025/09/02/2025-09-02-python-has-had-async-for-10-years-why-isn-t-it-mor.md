# Python has had async for 10 years – why isn't it more popular?

- Score: 324 | [HN](https://news.ycombinator.com/item?id=45106189) | Link: https://tonybaloney.github.io/posts/why-isnt-python-async-more-popular.html

### TL;DR

Python’s `async` and `await` arrived in 3.5, yet the author argues their practical sweet spot remains concurrent network I/O. Filesystem work generally falls back to thread pools, CPU-bound work remains constrained by the GIL in standard builds, and one blocking call can stall an event loop. Library maintainers also face duplicated synchronous and asynchronous implementations, incompatible backends, awkward properties and constructors, and separate testing patterns. FastAPI’s growth shows real success in web workloads, while Python 3.14 free-threading and subinterpreters may expand concurrency without requiring parallel async APIs.

### Comment pulse

- Many commenters prefer green threads because blocking-looking code avoids function coloring and cooperative-scheduling surprises.
- Others emphasize structured concurrency, which makes task lifetime, cancellation, and cleanup easier to reason about.

### LLM perspective

- View: Asyncio is specialized infrastructure whose ecosystem costs become visible when applied beyond network-heavy workloads.
- Impact: Teams pay not only syntax complexity but duplicated APIs, testing paths, resource ownership, and debugging ambiguity.
- Watch next: Whether free-threading gains task-level abstractions that preserve structured cancellation without spreading async interfaces.
