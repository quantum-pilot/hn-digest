# Cloudflare outage on November 18, 2025 post mortem

- Score: 253 | [HN](https://news.ycombinator.com/item?id=45973709) | Link: https://blog.cloudflare.com/18-november-2025-outage/

### TL;DR

Cloudflare says an 11:05 UTC ClickHouse permission change exposed duplicate column metadata to a Bot Management query, more than doubling a feature file beyond the proxy's 200-feature limit. Rapid global propagation caused FL2 workers to panic on an unhandled Rust `unwrap`; an older proxy instead assigned zero bot scores. Alternating good and bad files initially resembled an attack. Cloudflare stopped generation, inserted a known-good file, and restarted proxies, restoring core traffic by 14:30 and all systems by 17:06.

### Comment pulse

- Critics treated `unwrap` as an explicit production panic requiring the same scrutiny as unsafe code.
- Others focused on missing canaries and fault-contained rollouts, although rapid bot updates impose operational pressure.

### LLM perspective

- View: The deeper failure joined unsafe configuration assumptions, global propagation, and crash-oriented error handling.
- Impact: A peripheral bot feature became a shared failure path for core traffic, KV, Access, and dashboard login.
- Watch next: Configuration canaries, schema-qualified queries, graceful module isolation, kill-switch safety, and rollback drills.
