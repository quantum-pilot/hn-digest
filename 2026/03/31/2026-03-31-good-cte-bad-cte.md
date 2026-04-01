# Good CTE, Bad CTE

- Score: 167 | [HN](https://news.ycombinator.com/item?id=47571330) | Link: https://boringsql.com/posts/good-cte-bad-cte/

### TL;DR
The article dissects how PostgreSQL handles Common Table Expressions (CTEs), emphasizing that since PG 12 most single-use, side-effect-free CTEs are inlined and no longer act as “optimization fences.” It catalogs when CTEs are forced to materialize (multiple references, VOLATILE functions, DML, recursion, row locks), how this creates a statistics blind spot, and when materialization is actually beneficial. It also shows how pipeline-style CTEs with `GROUP BY` can block optimizations, recommends `EXISTS` patterns, and explains writable and recursive CTE traps, plus PG 17–18 improvements.

---

### Comment pulse
- Author forgot to define CTE; readers debate expectations for prior knowledge and call out unhelpful snark—counterpoint: on a SQL-focused site, some jargon is reasonable.
- Some see CTEs mainly as a readability tool; treating them as optimization fences is viewed as an implementation quirk, not a design goal.
- Recursive CTE discussion sparked comparisons with Oracle’s CONNECT BY and DuckDB’s USING KEY, highlighting differing recursion models and SQL-standard features like SEARCH/CYCLE.

---

### LLM perspective
- View: Treat CTE patterns (multi-use, GROUP BY booleans) as query-smell signals that tools or linters can automatically flag.
- Impact: DBAs and backend teams can codify these rules into query-review checklists, catching performance issues before production.
- Watch next: Benchmark auto-rewrites (CTE → EXISTS / temp tables) and surface EXPLAIN-based hints directly in application logs or migration pipelines.
