# A better streams API is possible for JavaScript

- Score: 358 | [HN](https://news.ycombinator.com/item?id=47180569) | Link: https://blog.cloudflare.com/a-better-web-streams-api/

### TL;DR

Cloudflare’s James Snell argues that WHATWG Web Streams, designed before async iteration, burden users and runtimes with manual locks, specialized BYOB readers, advisory backpressure, eager transforms, and promise-heavy hot paths. His proof of concept instead uses async iterables of byte-chunk batches, pull-driven transforms, explicit overflow policies, and optional synchronous fast paths, benchmarking 2–120× faster across major runtimes. It is a discussion prototype, not a production proposal. HN largely welcomed simpler composition but debated whether mixed sync/async iteration, per-item promises, and interoperability recreate other hazards.

### Comment pulse

- Web Streams hide costly machinery → locks, tee buffering, and unconsumed bodies create failures disproportionate to ordinary read-and-pipe tasks.
- Async iterables fit modern JavaScript → pull semantics compose naturally with `for await` — counterpoint: microtask overhead still punishes tiny chunks.
- Mixed synchronous and asynchronous results could recover speed → critics warn variable timing revives Zalgo semantics and complicates consumers.

### LLM perspective

- **View:** Stream design should make bounded-memory behavior observable and unavoidable.
- **Impact:** Runtime and framework authors could replace divergent fast paths with a shared primitive.
- **Watch next:** Reproducible benchmarks, cancellation semantics, and experiments in Node.js, browsers, Deno, and Bun.
