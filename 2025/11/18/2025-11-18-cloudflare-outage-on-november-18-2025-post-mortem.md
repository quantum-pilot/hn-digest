# Cloudflare outage on November 18, 2025 post mortem

- Score: 253 | [HN](https://news.ycombinator.com/item?id=45973709) | Link: https://blog.cloudflare.com/18-november-2025-outage/

## TL;DR

Cloudflare’s Nov 18, 2025 outage was caused by an internal configuration error, not an attack. A ClickHouse permission change made a metadata query return duplicate columns, doubling a Bot Management “feature file.” The proxy’s Bot module had a hard limit of 200 features with a Rust `unwrap()` that panicked when the larger file arrived, crashing core proxies worldwide. Rollback was slowed by initial misdiagnosis as DDoS and lack of tooling to inject a known-good file and restart the fleet quickly.

---

## Comment pulse

- Rust `unwrap()` in critical paths is reckless → it converts recoverable errors into panics; production code should treat each `unwrap` like a deliberate `panic`.  
- Global config push without canaries increased blast radius → rapid bot-config rollout traded safety for speed; better staged rollouts and dependency mapping could have contained failure.  
- Strong praise for fast, candid postmortem → but questions why global revert tools weren’t first-class and why customers couldn’t easily bypass Cloudflare via DNS when control plane was impaired.

---

## LLM perspective

- View: This was a classic “config as code” failure; internal data must be validated and rate-limited like untrusted user input.  
- Impact: Any service centralizing Internet traffic needs stronger blast-radius isolation for both code and configuration, not just better incident playbooks.  
- Watch next: Whether Cloudflare adds mandatory canarying, automated rollback for bad configs, and stricter review of crash-on-error patterns in critical Rust components.
