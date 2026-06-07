# Zeroserve: A zero-config web server you can script with eBPF

- Score: 180 | [HN](https://news.ycombinator.com/item?id=48425723) | Link: https://su3.io/posts/introducing-zeroserve

- TL;DR  
  Zeroserve is a minimalist HTTPS server that serves an entire site from a single tarball and replaces configs with user-space eBPF programs that run on every request. It uses io_uring, BoringSSL (TLS 1.3, HTTP/2, ECH, JA4), and a single-threaded event loop, targeting static sites and reverse-proxy frontends. Benchmarks show per-core wins over nginx and Caddy for small files, scripted middleware, and small proxied responses, while nginx remains better for large proxy bodies. HN debates config-as-code, static-site relevance, and kernel integration ideas.

- Comment pulse  
  - Program-as-config polarizes → fans say configs evolve into awkward DSLs, so one language is cleaner; skeptics say operators still prefer declarative knobs over code.  
  - Architecture feedback → readers want Rust-based scripting, true kernel eBPF/XDP or kTLS, and multi-process scaling via SO_REUSEPORT instead of a single-threaded userspace-only design.  
  - Static focus questioned → some argue few deploy new static-only servers; others report frequent static hosting and data-science workloads needing fast static delivery.

- LLM perspective  
  - View: Treating scripts as the only config plus tarball deployments greatly simplifies mental models, but raises maintainability and tooling challenges.  
  - Impact: Attractive for ops teams managing many small HTTPS frontends or static-plus-API gateways, where per-core efficiency and hot reloads matter.  
  - Watch next: independent benchmarks, Kubernetes/Ingress integration, translation from nginx/Caddy configs to eBPF, and experiments with kernel acceleration and multi-process scaling.
