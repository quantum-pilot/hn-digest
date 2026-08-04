# Prefer strict tables in SQLite

- Score: 202 | [HN](https://news.ycombinator.com/item?id=48873940) | Link: https://evanhahn.com/prefer-strict-tables-in-sqlite/

### TL;DR

Appending STRICT to a SQLite table makes declared types enforceable: invalid text-to-integer writes fail, bogus type names are rejected, and columns require one of six supported types, while lossless conversions and ANY preserve flexibility. The author recommends it for catching data-integrity bugs, but notes existing tables require copy-and-clean migrations, pre-3.37 clients cannot read strict schemas, and flexible tables still suit messy imports or key-value data. HN wanted stricter defaults, yet emphasized SQLite’s backward compatibility and embedded, single-application niche, where compile-time checks and easy schema evolution may outweigh redundant runtime validation.

### Comment pulse

- Strictness makes the schema a contract → multiple writers can trust declared types — counterpoint: one embedded application may already guarantee them statically.
- Changing the default would break compatibility → SQLite preserves old behavior, but the lack of a database-wide strict pragma creates repetitive, mixed enforcement.
- Flexible typing eases ingestion and evolution → heterogeneous values can preserve messy source data or defer migrations, at the cost of downstream validation.

### LLM perspective

- **View:** STRICT is a boundary choice: runtime validation matters where independent components exchange data and assumptions can diverge.
- **Impact:** Failing on write localizes corruption early; accepting anything shifts discovery to readers, where original intent may already be unrecoverable.
- **Watch next:** Global strict-mode proposals, migration tooling, mixed-schema linting, compatibility floors, ORM support, and measurable overhead under real write workloads.
