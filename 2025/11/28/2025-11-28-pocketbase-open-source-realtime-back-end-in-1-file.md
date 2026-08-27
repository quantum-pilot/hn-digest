# Pocketbase – open-source realtime back end in 1 file

- Score: 601 | [HN](https://news.ycombinator.com/item?id=46075320) | Link: https://pocketbase.io/

### TL;DR

PocketBase 0.34 packages a configurable backend into one executable: an embedded realtime database, authentication, local or S3 file storage, an admin dashboard, REST APIs, subscriptions, migrations, and Go or JavaScript extension hooks. It targets prototypes, internal tools, and small-to-medium applications that do not need a custom distributed stack. Commenters reported solid production and personal use, praising SQLite's operational simplicity, but noted breaking changes, missing specialized capabilities such as decimal handling, difficult edge cases, and dependence on a solo maintainer.

### Comment pulse

- SQLite is sufficient surprisingly often → acquiring users and developer operations usually constrain small applications before write contention.
- Built-in administration accelerates ordinary CRUD → custom domain logic still requires extensions or a conventional backend.
- Solo stewardship creates continuity risk → strong responsiveness and extensibility coexist with maintenance pressure and occasional breaking changes.

### LLM perspective

- View: PocketBase optimizes time-to-working-system, accepting a narrower scaling and ecosystem envelope for lower operational cost.
- Impact: Small teams can postpone infrastructure work and spend earlier effort on product-specific behavior.
- Watch next: Benchmark actual concurrency, rehearse backups and migrations, and identify unsupported data types before production adoption.
