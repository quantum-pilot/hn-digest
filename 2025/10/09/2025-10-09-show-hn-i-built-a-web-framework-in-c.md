# Show HN: I built a web framework in C

- Score: 272 | [HN](https://news.ycombinator.com/item?id=45526890) | Link: https://github.com/ashtonjamesd/lavandula

### TL;DR

Lavandula is an MIT-licensed web framework written in C that aims to package routing, HTTP methods, middleware, scaffolding, tests, logging, environment variables, SQLite, and JSON behind a small API. Sessions, CORS configuration, templating, rate limiting, static files, additional databases, and richer code generation remain planned or in progress. Commenters praised the project's readable code and educational value, while identifying production gaps including blocking I/O, partial-read handling, fixed request buffers, limited error checking, IPv6, and request parallelism.

### Comment pulse

- Readers treated Lavandula primarily as an appealing learning project rather than demanding immediate parity with mature frameworks.
- Technical feedback focused on slow-client blocking, unchecked allocations, request buffering, and concurrency.

### LLM perspective

- View: Lavandula's clearest present value is making low-level web mechanics approachable through clean C.
- Impact: Its simplicity aids learning, but missing I/O safeguards sharply limits production readiness.
- Watch next: Nonblocking networking, bounded parsing, error propagation, and concurrency should precede broader feature growth.
