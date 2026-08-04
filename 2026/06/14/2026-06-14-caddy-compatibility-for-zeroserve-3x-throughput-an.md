# Caddy compatibility for zeroserve: 3x throughput and 70% lower latency

- Score: 201 | [HN](https://news.ycombinator.com/item?id=48527145) | Link: https://su3.io/posts/zeroserve-caddy-compat

### TL;DR

ZeroServe 0.2.11 can now ingest a Caddyfile, compile its configuration into eBPF and then native x86-64 or ARM64 code, and execute it inside an io_uring event loop. In a two-thread HTTPS reverse-proxy benchmark, the Clang build reached 38,948 requests per second with 1.45ms median latency and 30.9MiB RSS, versus Caddy’s 12,529, 4.74ms, and 67.4MiB; nginx nearly matched ZeroServe. Custom middleware can be called from configuration. HN questioned the label because ACME and Caddy plugins are absent, and challenged the userspace-eBPF rationale.

### Comment pulse

- Compatibility is narrower than expected → ACME and Caddy plugins are absent — counterpoint: supporters see a cleaner codebase that may be easier to audit.
- Performance comparison favors nginx too → nginx delivered 37,424 requests per second with lower memory, offering maturity without a new runtime.
- Article hosting raised concern → several browsers received an unexpected client-certificate prompt; one visitor saw a government-use certificate offered for selection.

### LLM perspective

- **View:** The benchmark demonstrates an efficient compiled data path, but configuration syntax compatibility is not operational compatibility.
- **Impact:** Latency-sensitive reverse proxies gain another option; teams needing automated certificates or established extensions still face integration work.
- **Watch next:** Test ACME integration, Caddyfile coverage, plugin boundaries, TLS behavior, failure handling, and workloads beyond a two-thread synthetic proxy.
