# Workers Cache

- Score: 188 | [HN](https://news.ycombinator.com/item?id=48804014) | Link: https://blog.cloudflare.com/workers-cache/

### TL;DR
Cloudflare has introduced a new Workers Cache that finally lets Worker-generated responses participate in normal HTTP caching using `Cache-Control`, including `stale-while-revalidate`, plus tag-based invalidation and custom cache keys. Internally, this replaces the old browser-style Cache API with an architecture better suited to distributed caching and multiple worker entrypoints. HN commenters welcome the spec-compliant design, but question request-based billing for cache hits and note the marketing article’s LLM-ish writing style and lack of explicit technical backstory.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- New cache vs old API → Old Workers Cache API mimicked browser standards; new design finally matches distributed, multi-entrypoint Worker architecture.
- Spec-compliant caching → Proper `Cache-Control` and `stale-while-revalidate` support, plus cache tags, make Workers behave like a first-class HTTP origin.
- Pricing and DX concerns → Cache hits now billed per request, even static/worker calls; feels like metering quirk or upsell—counterpoint: CPU time remains free.

---

### LLM perspective
- View: This closes a long-standing gap: serverless-rendered apps on Cloudflare can now use standard HTTP caching semantics directly.
- Impact: Beneficial for high-traffic CMS, SSR, and APIs that can cut origin/compute usage, but pricing may deter aggressive adoption.
- Watch next: Real-world latency/cost benchmarks, clearer docs on cache-key control, and potential revisions to billing for static and internal requests.
