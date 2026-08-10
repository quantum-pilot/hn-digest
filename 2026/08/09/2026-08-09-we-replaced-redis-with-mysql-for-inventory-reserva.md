# We replaced Redis with MySQL for inventory reservations and it scaled

- Score: 328 | [HN](https://news.ycombinator.com/item?id=49226536) | Link: https://shopify.engineering/scaling-inventory-reservations

## TL;DR

Shopify migrated oversell protection from Redis to MySQL so reservations and the inventory ledger live in one ACID system. They model each sellable unit as a row in a bounded “available units” pool (capped at 1,000 per item/location), use `SELECT … FOR UPDATE SKIP LOCKED` to avoid hot-row contention, composite primary keys to reduce locks, and `READ COMMITTED` to dodge gap-lock deadlocks. The real scalability limit turned out to be database connections held by other checkout code, fixed via better connection attribution and tuning.

---

## Comment pulse

- Article feels AI-written → listicle tone, over-polish, and repetition erode trust in “engineer-authored” posts—counterpoint: likely human plus AI editing, which is now normal.

- Bounded per-unit row pool seems over-engineered → worries about complexity, potential undersell during spikes, and lack of hard numbers vs. simpler batched-decrement designs.

- Meta concern: 2026 and we still can’t cheaply decrement a shared counter → teams build elaborate DB patterns or external systems to preserve atomicity at scale.

---

## LLM perspective

- View: Pattern shows relational DBs can handle high-contention coordination, but at the cost of schema complexity and deep engine knowledge.

- Impact: Encourages teams to reconsider “throw Redis/Kafka at it” instincts and instead exploit modern DB features like `SKIP LOCKED`.

- Watch next: Benchmarks comparing this to batched counters, per-SKU sharding, and alternative primitives (e.g., Durable Objects, transactional message queues).
