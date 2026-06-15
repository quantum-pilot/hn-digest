# Caddy compatibility for zeroserve: 3x throughput and 70% lower latency

- Score: 201 | [HN](https://news.ycombinator.com/item?id=48527145) | Link: https://su3.io/posts/zeroserve-caddy-compat

### TL;DR
Zeroserve is a high‑performance HTTPS reverse proxy that runs eBPF programs in userspace and now accepts Caddy’s Caddyfile. It JIT‑compiles configs to eBPF and then native x86_64/ARM64 code, running on an io_uring event loop. In benchmarks it delivers ~3× Caddy’s throughput, ~70% lower median latency, and performance comparable to nginx while using less memory than Caddy. HN likes the speed but criticizes missing ACME and plugins, questions userspace eBPF’s value, and notes a sketchy client‑cert prompt on the demo site.

### Comment pulse
- Zeroserve's “Caddy compatible” omits ACME and plugin ecosystem → many prefer nginx's features and maturity — counterpoint: smaller, cleaner codebase may be easier to audit.  
- Site requests client TLS certificates → browsers prompt to use personal smart‑card/government certs, which feels suspicious and inappropriate for a public marketing page.  
- Original zeroserve pitch emphasized “no separate config files” → adding Caddyfile support raises questions about product direction and what differentiates it beyond performance.  

### LLM perspective
- View: Userspace eBPF plus JITed Caddyfiles shows an emerging pattern: treat configs as code, optimized aggressively at runtime.  
- Impact: If stability and features catch up, such servers could displace traditional proxies in high‑throughput internal APIs and edge gateways.  
- Watch next: Track ACME integration, production incident reports, and real‑world benchmarks under complex configs, not just synthetic reverse‑proxy microbenchmarks.
