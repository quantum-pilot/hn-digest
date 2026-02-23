# What is a database transaction?

- Score: 194 | [HN](https://news.ycombinator.com/item?id=47110473) | Link: https://planetscale.com/blog/database-transactions

- TL;DR  
  - The article explains SQL transactions as atomic units of work, then contrasts how Postgres (MVCC row-versioning) and MySQL (undo log) provide consistent reads. It walks through four isolation levels and how they relate to anomalies like phantom, non-repeatable, and dirty reads, plus how each database handles concurrent writes (MySQL row locks vs Postgres predicate locks/SSI). HN discussion focuses on better teaching via serializability/thread-safety, practical defaults (read committed/repeatable read), and the real-world tradeoffs of strict isolation.

- Comment pulse  
  - Start from serializability/thread safety → developers already reason about interleavings; weaker isolation is a deliberate relaxation. — counterpoint: serializable often unnecessary, hurts throughput.  
  - Most major RDBMSs default to read committed or repeatable read, not serializable; strict isolation brings retries, deadlocks, and sometimes large performance penalties.  
  - Clarifying phantom reads: repeatable read keeps previously seen row values stable, but may show additional rows in later SELECTs, not changed/deleted ones.

- LLM perspective  
  - View: Teach isolation by mapping to concurrency bugs developers already know, then layer SQL anomalies on top as diagnostics.  
  - Impact: Backend engineers, SaaS tool designers, and DBaaS vendors must consciously pick defaults and document their anomaly guarantees.  
  - Watch next: Robust client libraries with built‑in retry for serializable, plus benchmarks quantifying isolation-level costs on modern Postgres/MySQL.
