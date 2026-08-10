# We replaced Redis with MySQL for inventory reservations and it scaled

- Score: 328 | [HN](https://news.ycombinator.com/item?id=49226536) | Link: https://shopify.engineering/scaling-inventory-reservations

### TL;DR

Shopify moved short-lived inventory reservations from Redis into the same MySQL system as its inventory ledger, restoring ACID transactions across reserve and claim. Rather than contending on one quantity row, it uses a bounded pool of unit rows, `SKIP LOCKED`, composite primary keys, `READ COMMITTED`, consistent lock ordering, and batched queries. Production instrumentation revealed the true ceiling was database connection hold time elsewhere in checkout, not reservation CPU or query speed. After cleanup, tuning, shadow dual writes, and gradual cutover, high-volume flash sales showed substantial database headroom.

### Comment pulse

- Readers questioned whether the 1,000-row pool adds needless complexity or risks latency during replenishment.
- Others argued per-unit rows enable metadata and are a familiar performance denormalization.
- Much discussion criticized the post’s perceived LLM style, separate from the design’s merits.

### LLM perspective

- **View:** The strongest lesson is end-to-end observability, not that MySQL universally replaces Redis.
- **Impact:** Co-locating reservations and inventory removes cross-system atomicity failures while reducing infrastructure.
- **Watch next:** Replenishment-tail latency, hot-SKU contention, and operational results beyond the reported peak.
