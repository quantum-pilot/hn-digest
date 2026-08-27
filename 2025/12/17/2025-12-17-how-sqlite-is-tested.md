# How SQLite is tested

- Score: 219 | [HN](https://news.ycombinator.com/item?id=46303277) | Link: https://sqlite.org/testing.html

### TL;DR

SQLite maintains reliability through four independently developed harnesses, millions of parameterized cases and far more test code than production C. Its default core reaches 100% branch and MC/DC coverage, while anomaly tests inject allocation, I/O, crash and compound failures through replaceable interfaces. Continuous fuzzing mutates SQL and databases; regressions preserve every discovered bug. Releases also undergo leak detection, Valgrind, undefined-behavior builds, optimization-disabled comparisons and a roughly 200-item human-run checklist. The project says this expense is justified for ubiquitous, state-preserving infrastructure, not typical applications.

### Comment pulse

- Readers admired checklists but warned that copying the form without careful design can create red tape rather than communication and discovery.
- SQLite keeps TH3 and dbsqlfuzz proprietary despite public-domain code, suggesting paid test infrastructure can fund freely reusable software.

### LLM perspective

- View: SQLite’s strength comes from overlapping failure models, not any single coverage number.
- Impact: Database changes can proceed rapidly because regressions, compiler differences and malformed inputs are systematically challenged.
- Watch next: Extension coverage, JSON regressions, fuzzer discoveries, and how release checklists evolve after incidents.
