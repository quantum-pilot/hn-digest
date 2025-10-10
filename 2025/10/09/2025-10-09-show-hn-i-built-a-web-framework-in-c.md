# Show HN: I built a web framework in C

- Score: 272 | [HN](https://news.ycombinator.com/item?id=45526890) | Link: https://github.com/ashtonjamesd/lavandula

- TL;DR
  - Lavandula is a lightweight C web framework with routing, middleware, CLI scaffolding, built-in tests, JSON, and SQLite. The roadmap includes JSON body parsing, sessions, CORS, an ORM, and templating. HN praised its clean, teachable C, while offering practical feedback: adopt non-blocking I/O with an event loop, handle partial I/O and large bodies, add IPv6, rigorous error checking, and parallel request handling (threads/libuv). Many see it as ideal for learning and embedded/CGI use rather than a PHP replacement.

- Comment pulse
  - Educational and embedded value over mainstream replacement → clean C and tests aid learning; small footprint suits embedded/CGI; Jetzig comparisons — counterpoint: risk of abandonment.
  - Networking correctness → use non-blocking I/O with an event loop; handle partial reads/writes; avoid fixed buffers; bind AF_INET6 for IPv6.
  - Robustness and performance → check malloc/snprintf errors; remove dead code; add request parallelism (threads or libuv).

- LLM perspective
  - View: A C web framework for teaching/embedded use needs solid networking and safety to be credible.
  - Impact: Encourages C learners; could power tiny HTTP services if non-blocking, IPv6, and tests mature.
  - Watch next: Benchmarks versus Go/Rust; epoll/libuv integration; HTTP compliance tests; security audits for memory leaks and parsing edge cases.
