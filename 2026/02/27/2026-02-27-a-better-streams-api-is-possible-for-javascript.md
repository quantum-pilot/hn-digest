# A better streams API is possible for JavaScript

- Score: 358 | [HN](https://news.ycombinator.com/item?id=47180569) | Link: https://blog.cloudflare.com/a-better-web-streams-api/

### TL;DR

Cloudflare’s James M. Snell argues the WHATWG Web Streams API has structural problems: lock-based readers, BYOB complexity, advisory backpressure, and heavy promise churn that hurt usability and performance, especially on servers and in SSR. He presents a proof‑of‑concept alternative: streams as async iterables of `Uint8Array[]`, pull‑driven transforms, bytes‑only semantics, sync fast paths, and explicit backpressure policies (strict, block, drop‑oldest/newest). Benchmarks show 2–120× speedups. HN discussion explores async iterables, “maybe‑async” iterators, and practical pain with Web Streams in Node.

---

### Comment pulse

- Async+sync “stream iterator” (returns value or Promise) → preserves sync fast paths, avoids unnecessary promises, handles generic types; critics say byte‑chunk primitives are better for I/O.

- Async iterables still costly → small-chunk SSR thrashes promises; some use sync iterables with thunks to selectively go async, gaining 12–18× speedups.

- Practitioners dislike Web Streams on Node → feel browser‑centric and over‑abstract; prefer async iterables or classic Node `.pipe()` for simpler backpressure and composition.

---

### LLM perspective

- View: The proposal resets streaming around JS primitives, trading spec cleverness for predictable, optimizable patterns.

- Impact: Runtime implementers, SSR frameworks, and high-throughput services gain simpler code and more consistent performance envelopes.

- Watch next: Concrete polyfills, cross‑runtime benchmarks, and an incubation effort (WHATWG/TC39) to reconcile with existing Web Streams and fetch.
