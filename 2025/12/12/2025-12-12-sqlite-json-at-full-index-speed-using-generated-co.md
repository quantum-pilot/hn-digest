# SQLite JSON at full index speed using generated columns

- Score: 359 | [HN](https://news.ycombinator.com/item?id=46243904) | Link: https://www.dbpro.app/blog/sqlite-json-virtual-columns-indexing

### TL;DR

SQLite can keep each incoming JSON document intact while exposing selected paths as virtual generated columns. Indexing those columns lets ordinary predicates use B-tree lookups, and additional paths can be surfaced later without rewriting every document into a relational schema. The examples extract event type, user role, timestamp, and user ID, then query them as typed columns while retaining the raw payload. Virtual columns avoid storing duplicate extracted values; the index supplies lookup performance. The pattern trades up-front normalization for incremental, query-driven schema decisions.

### Comment pulse

- Some saw this as standard generated-column practice and warned that frequently constrained or updated attributes may belong in normalized rows.
- DuckDB was favored for large analytical scans — counterpoint: commenters still preferred SQLite for embedded application deployment.
- Alternatives included PostgreSQL JSONB expression indexes and a serialized B-tree document format supporting direct traversal and in-place updates.

### LLM perspective

- View: This is pragmatic schema evolution, provided indexed paths remain a curated interface rather than an accidental data model.
- Impact: Applications can ingest flexible payloads first, then accelerate proven access patterns with familiar SQL columns and indexes.
- Watch next: Index-build cost, write amplification, type coercion, missing paths, JSON validation, composite indexes, and when normalization becomes simpler.
