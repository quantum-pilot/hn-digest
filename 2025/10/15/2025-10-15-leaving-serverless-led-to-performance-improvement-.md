# Leaving serverless led to performance improvement and a simplified architecture

- Score: 289 | [HN](https://news.ycombinator.com/item?id=45590756) | Link: https://www.unkey.com/blog/serverless-exit

- TL;DR
  - Unkey rebuilt its API from Cloudflare Workers to stateful Go services and cut latency ~6x. Stateless serverless blocked in-process caching/batching, forcing networked caches (~30ms p99), queues, and log pipelines that added cost, complexity, and vendor lock‑in. Stateful servers enabled hot in‑memory caches, buffered analytics, a faster/more accurate rate limiter, local dev, and self‑hosting/portability; v1 remains for a low‑cost migration. HN largely agrees: serverless fits bursts and simple jobs, but containers/locality win for low‑latency paths; others note workarounds and Lambda’s strengths.

- Comment pulse
  - Serverless imposes limits; e.g., 100MB gateway uploads → brittle workarounds with queues/objects/log drains → complexity tax — counterpoint: presigned S3/tus help, but add components.
  - Containers as the unit are easier to test and port; Cloud Run/Knative accept them—counterpoint: some report Lambda is cheaper and simpler when designed properly.
  - Edge isn’t automatically faster: put compute near data dependencies; otherwise networked caches and hops dominate p99 latency.

- LLM perspective
  - View: Ultra-low-latency auth favors stateful services with hot in-memory caches over stateless functions plus networked caches.
  - Impact: Expect more teams to standardize on containerized Go/Rust services with regional clusters for sub-10ms authentication and rate limiting.
  - Watch next: Independent benchmarks of p99 latency/cost, release of Unkey Deploy, and improvements to edge-state primitives like Durable Objects.
