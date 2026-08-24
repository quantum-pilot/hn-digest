# The Tor Project is switching to Rust

- Score: 343 | [HN](https://news.ycombinator.com/item?id=46243543) | Link: https://itsfoss.com/news/tor-rust-rewrite-progress/

### TL;DR

Arti 1.8.0 advances Tor’s Rust reimplementation; this release does not mean the C implementation has been replaced. The central change splits circuit lifetime behavior into separate acceptance and idle-close timers, randomizing closure to reduce fingerprintable timing patterns. An experimental migration command transfers restricted-discovery keys for onion-service client authorization from C Tor into Arti’s keystore. The release also improves routing architecture, protocol handling, directory-cache support, and relay-port configuration, while Rust’s memory safety targets buffer, lifetime, and corruption bugs.

### Comment pulse

- Fingerprint tests sparked disagreement because anonymity depends on both uniqueness and persistence; one-dimensional benchmarks can reward or punish the wrong defense.
- Rust fit this security-sensitive, untrusted-input workload for many commenters — counterpoint: language choice alone does not make every rewrite appropriate.
- Users hoping for speed were reminded that onion routing’s multiple relays and geographic latency dominate performance; the release promises safety, not acceleration.

### LLM perspective

- View: Arti’s significance is reducing vulnerability classes while incrementally matching operational features, not winning a language contest.
- Impact: Onion-service operators gain a migration path, and clients receive less predictable circuit aging plus memory-safe implementation progress.
- Watch next: Feature parity, audits, default deployment, onion-service migration, performance regressions, fingerprint studies, and retirement plans for C Tor.
