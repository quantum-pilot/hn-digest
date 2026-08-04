# RFC 10008: The new HTTP Query Method

- Score: 310 | [HN](https://news.ycombinator.com/item?id=48568502) | Link: https://www.rfc-editor.org/info/rfc10008/

### TL;DR

RFC 10008 defines HTTP QUERY: a safe, idempotent method that carries query instructions in a request body, filling the gap between URI-bound GET and potentially state-changing POST. It enables automatic retries, conditional requests, cacheable responses keyed by body and metadata, and optional URIs for repeating queries or retrieving results; Accept-Query advertises supported formats. HN welcomed clearer semantics for complex filters and dry runs, but debated body-based cache keys, uncertain browser support, and whether headers or existing POST-redirect-GET patterns would suffice.

### Comment pulse

- Body caching divides opinion → exact bytes seem application-blind and attacker-controlled — counterpoint: hashed keys face the same abuse as unique query parameters.
- Browser usefulness remains unsettled → HTML forms could avoid POST resubmission warnings, but forms expose only GET/POST and redirect-after-POST already works.
- A distinct verb beats GET bodies → Fetch forbids them and some load balancers discard them, making interoperability failures practical rather than theoretical.

### LLM perspective

- **View:** QUERY separates read-like intent from transport shape, giving infrastructure a semantic signal without forcing inputs into URLs.
- **Impact:** API clients, gateways, caches, and observability tools must recognize a new method before benefits become dependable.
- **Watch next:** Track framework support, CDN cache-key behavior, CORS ergonomics, HTML form adoption, and retry correctness under failures.
