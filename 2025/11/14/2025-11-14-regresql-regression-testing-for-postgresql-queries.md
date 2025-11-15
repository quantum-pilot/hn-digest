# RegreSQL: Regression Testing for PostgreSQL Queries

- Score: 143 | [HN](https://news.ycombinator.com/item?id=45924619) | Link: https://boringsql.com/posts/regresql-testing-queries/

TL;DR
- RegreSQL brings PostgreSQL-style regression testing to app queries: runs .sql with plans, validates results, and keeps EXPLAIN-based performance baselines that flag plan anti-patterns. A YAML fixture system declaratively seeds reproducible data (generators, SQL hooks) and outputs CI-friendly reports. HN likes the direction but doubts CI can validate performance without prod-like distributions and concurrency; requests hooks for app-driven fixtures, broader ORM support beyond SQLAlchemy, and compatibility with tools like pgTAP, ephemeralpg, and PGlite.

Comment pulse
- Perf in CI is dubious → plans depend on stats, data size, and concurrency; caches mask issues. — counterpoint: EXPLAIN baselines catch obvious regressions early.
- Prefer app-code fixtures → avoids drift, reuse in end-to-end tests; request hooks so RegreSQL can call into app seeders.
- ORM and environment support matter → capture SQLAlchemy is promising; questions on interactive transactions, PGlite; some use pgTAP + ephemeralpg today.

LLM perspective
- View: Treat SQL like code: regression-test semantics, track plan smells; reserve load testing for prod-like environments.
- Impact: CI pipelines gain early warnings on query drift; DB teams formalize fixtures as versioned assets shared across services.
- Watch next: Add EXPLAIN ANALYZE sampling, stats seeding, concurrency harnesses; expand ORM/sqlc parsers; pre/post hooks and ephemeral DB backends (PGlite, ephemeralpg).
