# Oban, the job processing framework from Elixir, has come to Python

- Score: 164 | [HN](https://news.ycombinator.com/item?id=46797594) | Link: https://www.dimamik.com/posts/oban_py/

### TL;DR

Oban’s Python port implements a PostgreSQL-backed job queue whose inserts can share application transactions, avoiding a separate broker. Nodes wake through LISTEN/NOTIFY, claim work with FOR UPDATE SKIP LOCKED, execute asyncio tasks, then acknowledge results; database leases also coordinate leader-only pruning and orphan rescue. The open-source version supports concurrent I/O work but not multicore execution, bulk operations, or liveness-aware rescue. Those features, plus workflows, uniqueness, and richer concurrency controls, sit in Pro, so long-running open-source jobs should be idempotent and carefully configured.

### Comment pulse

- Transactional enqueueing was the standout benefit; commenters identified the outbox pattern and valued commit-or-rollback consistency.
- The pricing split drew criticism because multiprocessing and workflows are free elsewhere — counterpoint: maintainers may migrate features as usage develops.
- Skeptics questioned PostgreSQL throughput; one operator reported 20 million daily jobs on a modest VM, while another had benefited from Redis.

### LLM perspective

- View: The design makes PostgreSQL both durable store and coordinator, trading another dependency for tighter transactional semantics.
- Impact: Python teams gain an approachable brokerless queue, but open-source limits narrow its fit for CPU-heavy or high-volume workloads.
- Watch next: Benchmark evidence, edition changes, rescue correctness, process-pool economics, and adoption against mature Python competitors.
