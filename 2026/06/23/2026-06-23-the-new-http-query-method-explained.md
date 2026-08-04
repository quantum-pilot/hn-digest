# The new HTTP QUERY method explained

- Score: 210 | [HN](https://news.ycombinator.com/item?id=48640974) | Link: https://kreya.app/blog/new-http-query-method-explained/

### TL;DR

RFC 10008 defines HTTP QUERY for complex, read-only requests that need a body. It preserves GET-like safety and idempotence without oversized, encoded, routinely logged URLs or the inconsistent handling of GET bodies; unlike POST, intermediaries can understand that retries and caching are permissible. Cache keys must include request content. The author recommends retaining GET for simple or bookmarkable filters and testing QUERY carefully because clients, WAFs, proxies, and servers may reject it for years. HN welcomed clearer semantics but debated whether a new verb improves compatibility over standardizing GET bodies.

### Comment pulse

- GET-with-body fails silently and inconsistently → browsers, frameworks, gateways, and WAFs may reject, strip, or ignore content without a detectable negotiation path.
- QUERY offers cleaner fallback → a 405 response exposes unsupported verbs, allowing clients to retry with POST instead of guessing whether GET worked.
- Protocol evolution burdens old infrastructure → expensive HTTP/1.1-only proxies may block unknown methods — counterpoint: ossification should motivate upgrades, not freeze standards.

### LLM perspective

- **View:** QUERY is primarily a machine-readable promise, not a transport innovation; its value depends on intermediaries honoring safety semantics.
- **Impact:** API designers gain expressive read operations; client and infrastructure teams inherit capability detection, fallback, and body-aware caching work.
- **Watch next:** Track Fetch, framework, proxy, CDN, and WAF support; test cache-key canonicalization and fallback behavior across mixed deployments.
