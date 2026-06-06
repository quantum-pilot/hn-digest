# Idempotency is easy until the second request is different

- Score: 272 | [HN](https://news.ycombinator.com/item?id=48047930) | Link: https://blog.dochia.dev/blog/idempotency/

### TL;DR

The article argues that real idempotency is not “store response by Idempotency-Key and replay,” but correctly handling every later request with that key. The server must remember a canonical command, execution state, and outcome, reject same-key/different-command requests, and coordinate with downstream systems, queues, expiry, and schema changes. It recommends durable idempotency tables, atomic ownership, and explicit policies for failures. Hacker News debates whether this is over-engineered versus simply returning 409 on duplicate keys and pushing responsibility to clients.

---

### Comment pulse

- Simpler contract: duplicate key -> 409; client decides; works for ecommerce APIs; unique constraint or Redis enough — counterpoint: doesn't reveal if first attempt succeeded.  
- One camp: never fix client bugs; if contract is 'idempotent on key', trust key or body-hash. Others prefer checks to avoid client bugs impacting behavior.  
- Many praise the article’s real-world coverage; some reference Antithesis’s definite/indefinite error model and argue careful failure classification is crucial to designing replay policies.

---

### LLM perspective

- View: The right idempotency design depends on business impact; heavy machinery should be reserved for money, inventory, or irreversible effects.  
- Impact: Teams often overgeneralize Stripe-style patterns; documenting a few clear contracts (409-only, replay-with-body, etc.) per endpoint reduces confusion.  
- Watch next: Worth building tooling: operation IDs, status dashboards, and chaos tests that inject downstream timeouts to verify recovery and deduplication logic.
