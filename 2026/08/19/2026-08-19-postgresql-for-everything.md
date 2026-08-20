# PostgreSQL for Everything

- Score: 353 | [HN](https://news.ycombinator.com/item?id=49361279) | Link: https://www.raphaelbauer.com:443/posts/postgresql-everything/

### TL;DR

The author recommends PostgreSQL as the default way to reduce operational complexity, using built-ins or extensions for full-text search, JSON documents, queues, time-series data, vectors, unlogged caches, binary blobs, hierarchies, and JSON-serving APIs. The pitch rests on maturity, broad hosting support, and avoiding synchronization across specialized systems: start with Postgres, then switch only when it stops meeting requirements. The examples demonstrate breadth, not equivalent capability; the article gives little scale, cost, reliability, or migration guidance, and several functions depend on extensions.

### Comment pulse

- “Use Postgres until you discover why you cannot” captured the supportive simplicity-first view.
- Critics called it hammer-and-nail thinking, arguing Elastic and Kafka offer capabilities Postgres cannot match at demanding scale.
- Others said teams talked past each other: small applications benefit, while centralized bottlenecks, tooling gaps, and failover complicate larger systems.

### LLM perspective

- View: This is a sound defaulting heuristic but an overstatement when read as literal equivalence.
- Impact: Small teams can ship with fewer services, synchronization paths, and operational skills.
- Watch next: Measured workloads, extension operations, high availability, framework support, and explicit migration thresholds.
