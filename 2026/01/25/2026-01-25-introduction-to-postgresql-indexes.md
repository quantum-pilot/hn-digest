# Introduction to PostgreSQL Indexes

- Score: 279 | [HN](https://news.ycombinator.com/item?id=46751826) | Link: https://dlt.github.io/blog/posts/introduction-to-postgresql-indexes/

### TL;DR

This guide explains PostgreSQL indexes as separate structures mapping keys to tuple locations in unordered heap pages. A million-row example cuts one lookup from roughly 265 milliseconds and thousands of page reads to under a tenth of a millisecond and four cached pages. The speed costs disk, write work, planner complexity, and memory. It surveys B-tree variants, hash equality indexes, compact BRIN summaries, GIN for composite values, and GiST frameworks, while showing partial, covering, expression, multi-column, and combined bitmap strategies.

### Comment pulse

- Official documentation deserves equal billing → PostgreSQL’s own index chapters are unusually clear and authoritative.
- Leftmost-prefix advice has changed → PostgreSQL 18 adds skip scans — counterpoint: older full-index scans may still be inefficient.

### LLM perspective

- View: Index choice is a workload decision, not a reflexive answer to every slow query.
- Impact: Carefully shaped indexes trade extra storage and writes for dramatically less read I/O.
- Watch next: Explain plans, selectivity, write amplification, index size, and version-specific planner behavior.
