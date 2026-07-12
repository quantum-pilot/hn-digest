# Prefer strict tables in SQLite

- Score: 202 | [HN](https://news.ycombinator.com/item?id=48873940) | Link: https://evanhahn.com/prefer-strict-tables-in-sqlite/

### TL;DR
SQLite historically allows almost any value in any column, treating types as hints. STRICT tables, introduced recently, finally enforce declared types, appealing to developers used to Postgres or enterprise SQL. HN commenters mostly favor strict typing for catching bugs and protecting shared databases, but note SQLite’s defaults prioritize backward compatibility, embedded single-app use, and easy schema evolution. They also question SQLite’s own justification for flexible typing, arguing that in practice it can hide schema bugs and allow subtle data corruption.

*Content unavailable; summarizing from title and comments.*

### Comment pulse
- SQLite’s safety features require opt-in: foreign_keys PRAGMA, STRICT per-table; strict-by-default is rejected to avoid breaking existing apps across version upgrades—counterpoint: this preserves buggy behavior indefinitely.  
- Fans of flexible typing highlight in-place schema evolution for embedded, single-app databases, claiming compile-time checks and ownership of all writers make runtime type enforcement redundant.  
- Others report the opposite: loose typing hides bugs, lets wrong-type values silently persist, and can make identifying and repairing corrupted rows costly or impossible.  

### LLM perspective
- View: Treat SQLite as two modes—STRICT for shared or user-facing data, flexible only for private, tool-internal caches.  
- Impact: Wider STRICT adoption would narrow gaps with Postgres/MySQL, making SQLite more suitable for small multi-process services and serious analytics.  
- Watch next: Community pressure for a global STRICT pragma, richer types via CHECK constraints, and tooling that surfaces mixed-type anomalies.
