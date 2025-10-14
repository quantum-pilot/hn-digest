# HTTP3 Explained

- Score: 173 | [HN](https://news.ycombinator.com/item?id=45565646) | Link: https://http3-explained.haxx.se

- TL;DR
  - Community explainer of HTTP/3/QUIC: why QUIC exists (TCP head‑of‑line, latency), how it works (UDP, TLS 1.3, streams), and deployment. HN readers found the site fast yet JS-heavy (GitBook SPA), noted the content feels dated and the repo quiet, and shared a clear history of HTTP→HTTP/2→QUIC plus adoption trade-offs: UDP syscall costs, trickier load‑balancing, and blocking in some regions. Practical notes: h2 avoids multiple sockets to skip TLS handshakes; PDF link is hidden.

- Comment pulse
  - Fast static site → links open instantly, perceived static UX — counterpoint: GitBook SPA loads many JS files; heavy first load despite server rendering fallback.
  - Needs update → text reads pre-adoption (“upcoming years”); repo appears quiet; QUIC acronym note disputed.
  - HTTP/3 over QUIC → fixes TCP HOL and mobility; hampered by UDP syscall cost, load-balancing, blocking — counterpoint: io_uring plus in-kernel QUIC may improve throughput.

- LLM perspective
  - View: Solid primer but dated; pair with RFC 9000/9114 and real-world benchmarks before architectural decisions.
  - Impact: Best for high-latency, lossy, mobile paths; ops must rethink load-balancing, observability, and firewall policies.
  - Watch next: Kernel/user-space QUIC performance, io_uring adoption, QUIC v2 rollout, and default HTTP/3 enablement across CDNs and major stacks.
