# Python has had async for 10 years – why isn't it more popular?

- Score: 324 | [HN](https://news.ycombinator.com/item?id=45106189) | Link: https://tonybaloney.github.io/posts/why-isnt-python-async-more-popular.html

- TL;DR
  - Python added async/await in 3.5, but adoption lags because its sweet spot is narrow (mostly socket I/O), file I/O isn’t truly async, the GIL limits CPU parallelism, and the model adds “colored” APIs, event loops, and maintenance/testing burden. Ecosystem support remains uneven (FastAPI yes; Django ORM and Flask lag; ORMs only recently). Python 3.14’s free-threaded build and stdlib subinterpreters may make thread‑based parallelism practical, reducing pressure to go async everywhere.

- Comment pulse
  - Async arrived late; teams had forks/multiprocessing; green threads give blocking ergonomics without coloring — counterpoint: structured concurrency (Trio) improves Python’s ergonomics.
  - API gotchas: many primitives, event-loop coupling; some sync APIs require an event loop; tasks may be garbage-collected if not awaited; threads break 'fearless' guarantees.
  - Ops pain: file-descriptor leaks and CPU-bound tasks can stall event loops; many fallback to Flask/Gunicorn+nginx; Twisted praised for high-throughput networking.

- LLM perspective
  - View: Async shines for socket I/O; free-threaded Python plus subinterpreters could shift recommendation toward threads and structured concurrency for general workloads.
  - Impact: Web frameworks and ORMs may drop dual APIs; stdlib could add a task-parallel API; maintainers spend less on async-specific testing.
  - Watch next: Benchmarks: free-threaded vs asyncio under I/O and CPU load; Windows/Linux wheels for aiohttp/uvloop; governance on io_uring adoption.
