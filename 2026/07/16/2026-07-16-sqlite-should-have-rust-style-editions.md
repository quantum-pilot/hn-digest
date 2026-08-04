# SQLite should have (Rust-style) editions

- Score: 350 | [HN](https://news.ycombinator.com/item?id=48928135) | Link: https://mort.coffee/home/sqlite-editions/

### TL;DR

SQLite preserves extraordinary compatibility, but the author argues its legacy defaults invite bugs: foreign keys are disabled, ordinary columns accept mismatched types, competing writers fail immediately, and rollback journaling leaves WAL performance unused. The proposed compromise is an opt-in annual edition pragma enabling foreign keys, a five-second busy timeout, WAL with NORMAL synchronization, and strict tables without changing existing applications. Later editions could evolve the bundle. The approach preserves old behavior while offering safer defaults, but developers must still understand each setting.

### Comment pulse

- Database portability complicates editions → files move between newer embedded libraries and older command-line tools, while some pragmas belong to connections rather than files.
- Busy timeout is incomplete → it may be bypassed during deferred read-to-write upgrades — counterpoint: callers need nonblocking control and must handle failure anyway.
- Abstraction can hide policy → critics said a pragma is forgettable and strict tables cannot replace validation — counterpoint: one opt-in standardizes common expert practice.

### LLM perspective

- **View:** Edition bundles are migration affordances: they lower activation energy for sane defaults without pretending configuration choices disappear.
- **Impact:** A shared profile could reduce silent integrity failures while making tutorials, libraries, and diagnostics converge on one baseline.
- **Watch next:** Define persistence, older-client behavior, introspection, custom domains, migrations, and tests for interactions among bundled pragmas.
