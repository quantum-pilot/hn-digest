# Cap'n Web: a new RPC system for browsers and web servers

- Score: 357 | [HN](https://news.ycombinator.com/item?id=45332883) | Link: https://blog.cloudflare.com/capnweb-javascript-rpc-library/

### TL;DR

Cloudflare’s experimental Cap’n Web is a dependency-free, sub-10kB TypeScript RPC system for browsers, Workers, Node.js, WebSockets, HTTP batches, and postMessage. Its object-capability model passes functions and objects by reference, supports bidirectional calls, and pipelines dependent promises into one round trip. A special synchronous array map records operations into a restricted server-side instruction graph. TypeScript supplies compile-time interfaces, not runtime validation. Commenters admired the compact design and tracing trick, but debated whether RPC abstractions clarify latency or dangerously hide network boundaries.

### Comment pulse

- Round-trip debate → critics fear invisible network costs; defenders say each await marks the boundary and unawaited calls are deliberately fused.
- Scope caution → commenters noted missing distributed-capability features; the author said browser-to-server communication drove the initial release.

### LLM perspective

- View: Cap’n Web treats JavaScript as both API language and traceable query planner, reducing schemas while increasing semantic subtlety.
- Impact: Interactive TypeScript systems gain expressive batching, but teams must document failure, lifetime, authorization, and latency behavior.
- Watch next: Cross-language servers, runtime validation, third-party handoffs, security audits, and production experience beyond remote bindings.
