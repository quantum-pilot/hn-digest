# Databases in 2025: A Year in Review

- Score: 591 | [HN](https://news.ycombinator.com/item?id=46496103) | Link: https://www.cs.cmu.edu/~pavlo/blog/2026/01/2025-databases-retrospective.html

### TL;DR

Andy Pavlo’s 2025 database review finds PostgreSQL’s ecosystem still dominant, driven by version 18, major cloud offerings, acquisitions of Neon and CrunchyData, and new sharding projects. MCP servers became nearly universal, but often remain thin database proxies without adequate agent guardrails. New columnar formats challenged Parquet while acquisitions, private-equity deals, mergers, renamings, and shutdowns reshaped vendors. Commenters highlighted omitted temporal databases, growing SQLite and DuckDB use, and a core MCP tension: broad context access conflicts with least privilege.

### Comment pulse

- Temporal-database advocates argued immutability enables auditability, concurrency, cloning, and undo, though PostgreSQL ranges and extensions cover many needs.
- Developers reported continued migration toward SQLite or DuckDB for simple deployment, flexible ingestion, analytics, and single-file operation.
- MCP criticism centered on privileged credentials and hallucinated actions—counterpoint: database roles and views already provide enforceable boundaries.

### LLM perspective

- View: PostgreSQL’s gravitational pull now extends beyond features into acquisitions, compatibility layers, hosting, tooling, and distributed architecture.
- Impact: Database teams must evaluate ecosystem durability and operational safeguards alongside benchmark performance or fashionable interfaces.
- Watch next: Sharded PostgreSQL maturity, MCP guardrail failures, GPU-oriented formats, and consolidation outcomes will define 2026.
