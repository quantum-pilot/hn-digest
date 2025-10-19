# SQL Anti-Patterns

- Score: 210 | [HN](https://news.ycombinator.com/item?id=45626985) | Link: https://datamethods.substack.com/p/sql-anti-patterns-you-should-avoid

- TL;DR
  - Practical SQL anti-patterns and fixes: centralize CASE WHENs via dimension tables; avoid functions on indexed columns (use computed/indexed or normalized columns); don’t SELECT * in views; fix joins instead of masking duplicates with DISTINCT; limit view stacking; favor CTEs over deep subqueries; treat SQL like production code. HN adds: DISTINCT is often a smell but sometimes correct or even faster; make predicates sargable; beware NOT IN/!= and NULL/index semantics; enforce style with linters and comments.

- Comment pulse
  - DISTINCT is a smell → usually hides bad joins or modeling; use correct keys. — counterpoint: valid for unique lists, Cypher, or planner optimizations.
  - Make predicates sargable → avoid functions on indexed columns; precompute/normalize, index computed columns, or store case-folded values.
  - Negations/NULLs hurt indexing → NOT IN, !=, IS NULL skip indexes; know NULL semantics; index is_null flag. — counterpoint: NOT IN on constants often efficient.

- LLM perspective
  - View: Treat SQL transformations as shared code; centralize semantics, avoid magic logic in isolated views.
  - Impact: Data teams gain consistency, faster queries, easier debugging; fewer downstream breakages from schema drift or hidden deduping.
  - Watch next: Adopt linting/formatters, sargability checks, and query plans in CI; measure improvements via latency, scan volume, and cache hit rates.
