# Good CTE, Bad CTE

- Score: 167 | [HN](https://news.ycombinator.com/item?id=47571330) | Link: https://boringsql.com/posts/good-cte-bad-cte/

### TL;DR

PostgreSQL CTEs stopped being automatic optimization fences in version 12: a pure, singly referenced query is normally inlined, while multiple references, recursion, writes, volatile functions, row locks, or an explicit hint trigger materialization. Inlining permits predicate pushdown, indexes, join reordering, and partition pruning; materialization computes once but can lose planning detail and spill beyond work_mem. PostgreSQL 17 propagates more statistics and sort information, while 18 exposes memory and disk usage. The article recommends EXISTS for boolean relationship tests and temporary tables when large intermediates need indexes or statistics.

### Comment pulse

- The article initially omitted that CTE means Common Table Expression; the author accepted and corrected the oversight.
- Readers primarily value CTEs for organization, praising the recursive hierarchy example and warning against treating syntax as an optimization tool.
- Oracle CONNECT BY may suit depth-first traversal — counterpoint: standard CTE SEARCH and CYCLE clauses offer broader traversal and cycle controls.

### LLM perspective

- **View:** Since PostgreSQL 12, CTE syntax alone says little about execution; semantics and reference count determine the boundary.
- **Impact:** Developers can retain readable decomposition if they inspect actual plans instead of applying pre-12 folklore.
- **Watch next:** Version-specific plans, row-estimate quality, temporary-file spills, prepared-plan changes, and accidental repeated work under NOT MATERIALIZED.
