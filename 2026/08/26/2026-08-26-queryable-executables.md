# Queryable Executables

- Score: 307 | [HN](https://news.ycombinator.com/item?id=49442589) | Link: https://fzakaria.com/2026/08/24/actually-queryable-executables

### TL;DR

SELF represents an executable as a SQLite database, letting a custom Linux interpreter map code segments and jump to its entry point. The new self-httpd demonstration also stores routes, assets, logs, and button presses transactionally in that same runnable file. Consequently, SQL can inspect symbols, update a live site, add full-text search, audit deployments with sqldiff, and migrate state between builds. HN loved the hacker audacity and connections to Smalltalk, Lisp, and program images, while warning that mutable internet-facing binaries complicate security, immutability, concurrent instances, and upgrades.

### Comment pulse

- Database-as-container collapses tooling into relational operations → code, assets, logs, schema, search, diffs, and migrations become ordinary tables and transactions.
- Self-contained mutable programs offer delightful portability → one file can remember state across machines — counterpoint: multiple instances and security boundaries become awkward.
- Historical systems anticipated the concept → Smalltalk images, Lisp, APL, Tcl, and redbean show old ideas resurfacing through accessible SQLite machinery.

### LLM perspective

- View: SELF is most valuable as a design probe showing which deployment mechanisms disappear when executable structure becomes queryable data.
- Impact: Small tools could become inspectable, migratable single-file systems; production operators would trade immutable artifacts for new coupling risks.
- Watch next: Explore read-only code separation, signed updates, multi-architecture rows, zero-downtime migrations, mmap alignment, and SQL-injection containment.
