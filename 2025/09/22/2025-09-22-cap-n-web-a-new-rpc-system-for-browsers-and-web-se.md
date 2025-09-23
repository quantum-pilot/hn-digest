# Cap'n Web: a new RPC system for browsers and web servers

- Score: 357 | [HN](https://news.ycombinator.com/item?id=45332883) | Link: https://blog.cloudflare.com/capnweb-javascript-rpc-library/

- TL;DR
  - Cloudflare’s Cap’n Web is a tiny, MIT-licensed TypeScript RPC bringing object-capability semantics to browsers, Workers, and Node via JSON, no schemas, and HTTP/WebSocket/postMessage. It supports bidirectional calls, passing functions/objects by reference, and promise pipelining; batch mode and a special array.map trace/pipeline fuse dependent calls into one round-trip. TypeScript interfaces add static checks; auth can return session capabilities. HN praises the record–replay idea (akin to expression trees/JAX), debates hidden round-trips, and questions portability and missing ocap features (sturdyrefs, third-party handoffs).

- Comment pulse
  - map() tracing is powerful yet scary → record–replay builds a constrained IR, like C# expression trees/TanStack DB; questions remain about conditionals and operator support.
  - Hiding round-trips is risky → users want clear network boundaries — counterpoint: the await is the round-trip; pipelined calls without await don’t add latency.
  - Scope and ports → tiny codebase; easier in dynamic languages; lacks sturdyrefs/third-party handoffs; author: 3PH later, sturdyrefs are platform-specific (OAuth-like approach possible).

- LLM perspective
  - View: A JS-first ocap RPC that fuses calls via tracing/pipelining reduces chattiness without new schemas.
  - Impact: Frontend teams model real-time workflows naturally; security shifts to capability objects instead of global auth state.
  - Watch next: Benchmarks under loss; semantics docs for tracing/map DSL; interop/ports; third-party handoff and persistence story (OAuth, Durable Objects).
