# What is a database transaction?

- Score: 194 | [HN](https://news.ycombinator.com/item?id=47110473) | Link: https://planetscale.com/blog/database-transactions

### TL;DR

A database transaction groups reads and writes into one atomic unit that either commits or rolls back, while isolation controls how concurrent work becomes visible. The article contrasts PostgreSQL’s row-versioning with MySQL’s undo log, then explains serializable, repeatable-read, read-committed, and read-uncommitted modes through phantom, non-repeatable, and dirty reads. At serializable isolation, MySQL uses blocking row locks, whereas PostgreSQL detects conflicts through serializable snapshot isolation and aborts transactions. Commenters wanted serializability introduced first, clearer default-level distinctions, and stronger emphasis on application retry logic.

### Comment pulse

- One camp favors teaching strict serializability as the goal, treating weaker isolation as explicit relaxations rather than a catalog of anomalies.
- Serializable execution improves guarantees — counterpoint: coordination costs, aborts, and mandatory retries often make weaker levels more practical.
- Readers corrected that modern MySQL and MariaDB InnoDB default to repeatable read, while PostgreSQL defaults to read committed.

### LLM perspective

- **View:** Isolation names are insufficient specifications; applications must state which cross-row invariants concurrent transactions must preserve.
- **Impact:** Developers choosing weaker defaults inherit responsibility for locks, constraints, conflict handling, and tests that exercise races.
- **Watch next:** Retry guidance, default-level documentation, workload benchmarks, anomaly tests, and comparisons of MySQL locking with PostgreSQL SSI.
