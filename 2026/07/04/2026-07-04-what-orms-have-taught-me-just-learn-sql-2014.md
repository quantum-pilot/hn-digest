# What ORMs have taught me: just learn SQL (2014)

- Score: 126 | [HN](https://news.ycombinator.com/item?id=48742175) | Link: https://wozniak.ca/blog/2014/08/03/1/index.html

### TL;DR

After using SQLAlchemy, Hibernate, PostgreSQL, and SQLite, the author argues that ORMs obscure rather than eliminate relational complexity. Wide entities cause overfetching, relationships produce excessive joins, advanced queries become awkward, and migrations and transactions still demand database knowledge. Their preferred model treats queries as the database API, using direct or templated SQL with lightweight schema representation. HN largely favored a hybrid: learn SQL, use ORMs for CRUD, hydration, migrations, and change tracking, then switch to query builders or native SQL for complex or performance-sensitive work.

### Comment pulse

- ORM value depends on workload → reporting pipelines need little object machinery, while long-lived clients benefit from identity maps and change tracking.
- Domain modeling remains contentious → some see ORMs as a forcing function — counterpoint: persistence entities can contaminate or duplicate domain models.
- Abstraction must expose cost → seemingly simple ORM calls can hide N+1 queries, overfetching, coercions, and missed indexes.

### LLM perspective

- **View:** The durable skill is reading query plans; syntax choice matters less than understanding generated database work.
- **Impact:** Teams can standardize a tiered data-access policy instead of choosing one universal abstraction.
- **Watch next:** Measure query count, transferred columns, latency, and plan regressions in CI.
