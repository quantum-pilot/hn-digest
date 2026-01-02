# Show HN: OpenWorkers – Self-hosted Cloudflare workers in Rust

- Score: 351 | [HN](https://news.ycombinator.com/item?id=46454693) | Link: https://openworkers.com/introducing-openworkers

- TL;DR  
OpenWorkers is an open-source, Rust-based V8 runtime that mimics Cloudflare Workers’ API while being fully self-hostable via Docker, Postgres, and built-in bindings (KV, Postgres, S3, scheduling, logs, dashboard). It trades Cloudflare’s massive edge network for control, predictable capacity and no per-request pricing. HN discussion focuses on what “edge” means without 300+ PoPs, the difficulty of building truly secure JS sandboxes, and how this compares to Cloudflare’s workerd and serverless pay-per-invocation economics.

- Comment pulse  
  - Self-hosted “edge” → you gain control and avoid lock-in but can’t match Cloudflare’s global PoPs; maybe regional 5–10 PoPs are enough.  
  - Sandbox security skepticism → V8 isolates plus limits help, but without independent audits and constant patching it’s not suitable for hostile multi-tenant workloads.  
  - Positioning vs workerd/serverless → OpenWorkers adds dashboard, bindings, managed option; critics note you pre-provision hardware instead of paying per-function, which suits infra-rich teams.

- LLM perspective  
  - View: Treat this as a programmable PaaS layer for teams already running regional clusters, not a Cloudflare replacement.  
  - Impact: Simplifies hosting CF-Workers-style apps near existing databases, easing migration away from proprietary edge platforms.  
  - Watch next: Security posture, performance benchmarks vs workerd/Deno, and how deterministic replay/debugging actually works in real incidents.
