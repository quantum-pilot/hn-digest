# Show HN: OpenWorkers – Self-hosted Cloudflare workers in Rust

- Score: 351 | [HN](https://news.ycombinator.com/item?id=46454693) | Link: https://openworkers.com/introducing-openworkers

### TL;DR

OpenWorkers packages a Rust and V8-isolate runtime with a dashboard, API, scheduler, logs, and bindings for KV, PostgreSQL, S3-compatible storage, services, and secrets. It targets Cloudflare Workers compatibility while keeping data and costs on self-hosted infrastructure, deployable through Docker Compose and PostgreSQL; workers receive 100 ms CPU and 128 MB memory limits. HN welcomed the complete platform but challenged its “edge” framing and, more importantly, whether AI-assisted rusty_v8 code can safely isolate hostile tenants without Cloudflare-scale security maintenance.

### Comment pulse

- Self-hosting trades global reach for control → a few regional locations may suffice without 300 points of presence.
- Isolates alone are not a security proof → untrusted multi-tenancy needs testing, documentation, patching, and layered containment.
- Compared with workerd, completeness is the differentiator → OpenWorkers includes operations, bindings, scheduling, and a managed option.

### LLM perspective

- View: The strongest proposition is a portable workers platform; “edge” and security claims should remain deliberately narrower.
- Impact: Teams can avoid per-request pricing and lock-in when workloads are trusted and geographic needs are modest.
- Watch next: Review threat models, V8 update latency, escape testing, Cloudflare compatibility coverage, and deterministic replay.
