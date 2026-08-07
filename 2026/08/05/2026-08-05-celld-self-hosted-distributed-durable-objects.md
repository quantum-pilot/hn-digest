# Celld: Self-hosted, distributed Durable Objects

- Score: 272 | [HN](https://news.ycombinator.com/item?id=49185430) | Link: https://github.com/denoland/celld

### TL;DR

Celld is an open-source daemon for running Cloudflare Workers and Durable Objects on self-hosted machines. Each named object owns a SQLite database, while an S3-compatible bucket stores deployments, replicated state, leases, and fleet authentication. Object-storage compare-and-swap assigns a cell to one node without a separate control plane or consensus service; nodes restore cells after movement or hibernation. The project includes signed peer probes, replay protection, optional pressure shedding, and guarded networking defaults, but describes its compatibility and distributed protocol as still evolving.

### Comment pulse

- Supporters welcomed provider-independent Durable Objects and the per-object SQLite model for multiplayer, collaborative, and WebSocket applications.
- One commenter questioned whether unconditional segment writes uphold single-owner safety at persistence time.
- Disabling pull requests sparked debate: AI lowers contribution cost but shifts scarce effort to review and coherence.

### LLM perspective

- View: The design trades control-plane complexity for dependence on object-store semantics.
- Impact: Self-hosting could broaden actor-style applications while keeping cells isolated and portable.
- Watch next: Fault-injection evidence, Workers conformance, and proof that write fencing preserves zero data loss.
