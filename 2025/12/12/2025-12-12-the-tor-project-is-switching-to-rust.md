# The Tor Project is switching to Rust

- Score: 343 | [HN](https://news.ycombinator.com/item?id=46243543) | Link: https://itsfoss.com/news/tor-rust-rewrite-progress/

### TL;DR

Arti 1.8.0 advances the Tor Project’s Rust implementation, but the supplied article does not establish an immediate wholesale replacement of the C network. Its main change reworks circuit timeouts: separate usage-based timers stop accepting new streams and close idle circuits at randomized times, aiming to reduce predictable patterns. An experimental command migrates restricted-discovery keys for onion-service client authorization from C Tor into Arti’s keystore. The release also reports routing, protocol, directory-cache, and OR-port configuration improvements, with memory safety—not speed—presented as the rewrite’s core benefit.

### Comment pulse

- Readers caution that fingerprint tests must measure both uniqueness and persistence; changing browser security settings can itself narrow anonymity sets.
- Discussion largely agrees Tor latency reflects onion-routing and network tradeoffs, not something a language rewrite automatically fixes.

### LLM perspective

- View: Rust addresses exploitable memory-error classes, while anonymity still depends on protocol behavior and uniform client populations.
- Impact: Incremental migration can improve safety without pretending a language change solves Tor’s network latency.
- Watch next: Arti feature parity, migration reliability, timeout fingerprinting evidence, audits, and production adoption remain decisive.
