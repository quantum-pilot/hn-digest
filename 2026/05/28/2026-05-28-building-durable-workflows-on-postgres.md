# Building durable workflows on Postgres

- Score: 244 | [HN](https://news.ycombinator.com/item?id=48313530) | Link: https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution

### TL;DR

DBOS argues durable execution needs no separate orchestrator: application workers can dequeue workflows from Postgres, checkpoint every completed step, recover crashed work, and reject duplicate execution through locks and integrity constraints. This reuses Postgres replication, scaling, SQL observability, access controls, and an application’s existing failure boundary instead of adding orchestration infrastructure. HN recognized the database-first pattern and lightweight alternatives, but questioned whether the simplicity survives production scale, feature parity, and commercial dependencies.

### Comment pulse

- Postgres is sufficient at modest scale → absurd, durable, and homegrown multi-backend queues show the pattern can remain lightweight and migration-friendly.
- Temporal buys structure and lifecycle features → users praised its SDK and discipline — counterpoint: others reported complexity, cost, payload friction, and poor throughput.
- Open-core boundaries affect adoption → one commenter rejected DBOS because scaling and recovery reportedly require paid Conductor.

### LLM perspective

- **View:** Postgres can replace orchestration storage and dispatch, but durable semantics still require disciplined runtime and idempotent application design.
- **Impact:** Teams may eliminate an orchestrator service, but workflow load now shares Postgres capacity, incident response, and scaling decisions.
- **Watch next:** Compare recovery correctness, retry semantics, backpressure, history growth, multi-region failover, observability, and cost under equivalent workloads.
