# SQL Anti-Patterns

- Score: 210 | [HN](https://news.ycombinator.com/item?id=45626985) | Link: https://datamethods.substack.com/p/sql-anti-patterns-you-should-avoid

### TL;DR

The article identifies SQL shortcuts that become maintenance or performance liabilities: giant duplicated CASE expressions, functions that defeat indexes, SELECT * in views, DISTINCT masking faulty joins, deep view stacks, and heavily nested subqueries. It recommends shared dimensions, index-friendly predicates, explicit columns, corrected relationships, periodic materialization, and clearer CTEs. Commenters agreed SQL deserves production-code discipline but emphasized context: DISTINCT can be legitimate or improve plans, database null and indexing behavior varies, and sargability often matters more than universal rules.

### Comment pulse

- DISTINCT is a diagnostic signal, not automatic proof of error → valid deduplication and optimizer behavior depend on schema and engine.
- Treat SQL as code → consistent formatting, comments, review, versioning, and linters improve comprehension.

### LLM perspective

- View: Most anti-patterns are hidden-model problems; syntax cleanup helps only after cardinality and access paths are understood.
- Impact: Data teams reduce metric drift and debugging time by centralizing semantics and inspecting execution plans.
- Watch next: Benchmark proposed rewrites on the target database, including null handling, indexes, statistics, and materialization costs.
