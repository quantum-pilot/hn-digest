# Workers Cache

- Score: 188 | [HN](https://news.ycombinator.com/item?id=48804014) | Link: https://blog.cloudflare.com/workers-cache/

### TL;DR

Cloudflare’s Workers Cache places a tiered cache before a Worker, so hits return without executing or billing Worker CPU. One flag enables it; responses use standard Cache-Control, stale-while-revalidate, and Vary headers, with tag or prefix purges. Unlike zone caching, it follows the Worker across domains, previews, service bindings, and per-entrypoint compositions; ctx.props partitions multi-tenant cache keys. HN praised the standards-first design and server-rendering path. The major objection was billing: every hit still incurs a request charge, and enabling caching makes free static assets and worker-to-worker calls billable, potentially raising costs.

### Comment pulse

- The old Cache API fit browsers, not distributed infrastructure → partial adequacy delayed replacement until parameterized entrypoints and channel tokens simplified insertion.
- HTTP semantics won praise → Cache-Control, Vary, stale-while-revalidate, and tags avoid framework-specific caching while supporting negotiation, background refresh, and targeted invalidation.
- Billing can invert savings → hits eliminate CPU charges but retain request fees — counterpoint: static and internal calls newly becoming billable may outweigh gains.

### LLM perspective

- **View:** This is function memoization expressed through HTTP: cache stages can sit before public, service-bound, or internal entrypoints without infrastructure.
- **Impact:** Moving cache ownership from zones to deployable code improves composability, testing isolation, tenant safety, and framework portability.
- **Watch next:** Request-cost break-even, static-asset metering, hit ratios, variant explosion, purge propagation, tenant isolation, Smart Placement co-location, and framework integrations.
