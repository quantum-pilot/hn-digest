# Oban, the job processing framework from Elixir, has come to Python

- Score: 164 | [HN](https://news.ycombinator.com/item?id=46797594) | Link: https://www.dimamik.com/posts/oban_py/

## TL;DR

Oban.py is a Python port of the Elixir Oban job framework that uses PostgreSQL as both storage and coordination layer: jobs live in a table and are moved through states with `LISTEN/NOTIFY`, `FOR UPDATE SKIP LOCKED` for safe concurrent fetching, and `INSERT … ON CONFLICT` for leader election. The open-source version is asyncio-only and single-process; Oban Pro adds a process pool, bulk operations, smarter job rescue, workflows, and advanced concurrency, which sparked pricing and competitiveness debate on HN against existing Python job/worker tools.

---

## Comment pulse

- DB-backed queueing is praised for transactional guarantees → enqueue and domain writes in one commit; framed as the transactional outbox pattern — counterpoint: some warn about overloading Postgres.

- Revenue model questioned → putting multiprocessing, workflows, and unique jobs behind Pro feels steep in Python’s crowded ecosystem; maintainers note features may shift OSS over time.

- Scalability and architecture debated → some doubt Postgres vs Redis/Sidekiq at very high volumes; others report tens of millions of daily jobs on modest Postgres, plus easy horizontal worker scaling.

---

## LLM perspective

- View: Oban.py fits teams already on Postgres wanting strong consistency and minimal extra infra, especially for I/O-bound, app-adjacent jobs.

- Impact: Competes with Celery, RQ, Temporal-style systems; most attractive where DB-centered operations and Elixir–Python interoperability matter.

- Watch next: Benchmarks vs Redis/Temporal, clearer guidance on volume limits, and whether Pro-only features (process pool, workflows) migrate into OSS.
