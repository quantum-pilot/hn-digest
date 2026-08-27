# RegreSQL: Regression Testing for PostgreSQL Queries

- Score: 143 | [HN](https://news.ycombinator.com/item?id=45924619) | Link: https://boringsql.com/posts/regresql-testing-queries/

### TL;DR

RegreSQL is an early-stage tool that applies PostgreSQL-style regression testing to application queries. It scans named SQL, substitutes inputs, compares expected JSON results, and tracks estimated EXPLAIN costs with configurable tolerances and plan warnings. YAML fixtures support static or generated data, dependencies, setup, and rollback cleanup; experimental SQLAlchemy capture targets ORM queries. The author positions performance checks as inexpensive baselines, not production benchmarks: reliable conclusions still require representative data distributions, statistics, concurrency, cache state, and hardware.

### Comment pulse

- Readers debated YAML fixtures versus application-native setup and broader API-level integration tests.
- The author agreed EXPLAIN baselines catch regressions but cannot model full production performance.

### LLM perspective

- View: RegreSQL productizes a useful narrow guardrail rather than promising comprehensive database performance testing.
- Impact: Teams can detect result or plan drift early if fixtures resemble the queries they protect.
- Watch next: Better documentation, ORM capture maturity, and evidence from larger real-world test suites.
