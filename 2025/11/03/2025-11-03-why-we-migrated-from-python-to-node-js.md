# Why we migrated from Python to Node.js

- Score: 205 | [HN](https://news.ycombinator.com/item?id=45800955) | Link: https://blog.yakkomajuri.com/blog/python-to-node

### TL;DR

One week after launch, Skald rewrote its Django backend in Node.js because its workload makes many concurrent LLM and embedding API calls. The team found Django’s partial async support, sync/async adapters, worker choices, and non-native file I/O difficult to reason about. A three-day migration to Express and MikroORM reportedly produced about three times the initial throughput, unified an existing Node worker with the server, and prompted more tests. The tradeoffs include rebuilding Django conveniences and losing Python’s stronger machine-learning ecosystem; the benchmark remains early and self-reported.

### Comment pulse

- Critics questioned premature scaling and whether Celery, Channels, FastAPI, or horizontal scaling received enough consideration.
- Supporters argued that a tiny codebase made this the cheapest moment to remove a concurrency model the team distrusted.

### LLM perspective

- View: The rewrite is best understood as reducing team-specific complexity, not proving Node universally scales better.
- Impact: A unified event-loop stack may accelerate I/O-heavy work while creating framework and ML-ecosystem costs.
- Watch next: Production latency, failure handling, resource use, feature velocity, and whether Python returns as a separate service.
