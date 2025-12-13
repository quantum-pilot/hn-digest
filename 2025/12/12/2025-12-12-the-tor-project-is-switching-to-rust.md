# The Tor Project is switching to Rust

- Score: 343 | [HN](https://news.ycombinator.com/item?id=46243543) | Link: https://itsfoss.com/news/tor-rust-rewrite-progress/

### TL;DR
Tor is progressively replacing its aging C code with Arti, a Rust-based reimplementation focused on memory safety and privacy hardening. The 1.8.0 release overhauls circuit timeouts, using separate, usage-based and randomized timers to make traffic patterns less fingerprintable, and adds tooling to migrate onion-service authorization keys from the C Tor keystore. HN commenters debate fingerprinting tests, argue Rust is an excellent fit for Tor but not a universal remedy, and note Tor’s latency is inherently network-bound.

### Comment pulse
- Fingerprinting discussion → EFF test rewards binning, punishes randomization; Tor Browser defaults already strong, JS-off scores higher but residual leaks via CSS and mouse tracking.  
- Rust seen as apt for Tor → eliminates memory bugs; some resent 'rewrite in Rust' — counterpoint: memory-safe languages beat C for untrusted, security-critical services.  
- Tor slowness blamed on design, not C → onion routing’s multi-hop latency and limited relays dominate; Rust rewrite targets safety, not significantly higher throughput.  

### LLM perspective
- View: Incremental Rust rewrite alongside C Tor limits regressions; Arti’s circuit changes meaningfully strengthen traffic-analysis resistance.  
- Impact: Memory-safe core plus better key handling should cut critical vulnerabilities and operational mistakes for relay and onion-service operators.  
- Watch next: performance benchmarks of Arti vs C Tor, anonymity analyses of new timeouts, and migration tooling for existing relays.
