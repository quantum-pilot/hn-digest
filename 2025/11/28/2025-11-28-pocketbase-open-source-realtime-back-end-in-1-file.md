# Pocketbase – open-source realtime back end in 1 file

- Score: 601 | [HN](https://news.ycombinator.com/item?id=46075320) | Link: https://pocketbase.io/

### TL;DR
PocketBase is a single Go binary that bundles a realtime SQLite-backed database, auth (email/OAuth), file storage, admin dashboard, and JS/Dart SDKs. You define collections and rules via a web GUI, get REST and realtime APIs out of the box, and can extend behavior with Go/JS hooks. HN commenters like it for side projects, internal tools, and even small production apps, emphasizing SQLite’s simplicity and performance. Concerns center on SQLite limitations (e.g., numeric types) and PocketBase’s solo maintainer and occasional breaking changes.

---

### Comment pulse

- SQLite-first backend scales far enough for most CRUD apps → single-file deployment, minimal ops, WAL on NVMe is fast—counterpoint: lack of native decimal type blocks some financial use cases.  

- PocketBase is “production-solid” for small/medium apps → strong extensibility, migrations, good DX; risk is solo maintainer, rough support tone, and occasional breaking API changes.  

- Best fit is Firebase/Parse-style apps and prototypes → GUI-configured collections + auth + files replaces lots of boilerplate; heavy GIS/Postgres/Supabase-style features still require custom stacks.

---

### LLM perspective

- View: Treat PocketBase as a powerful SQLite BaaS for CRUD-heavy apps, not a universal backend replacement.  

- Impact: Solo devs and small teams can ship full-stack prototypes and internal tools fast, with minimal infra expertise.  

- Watch next: Maturity of ecosystem (plugins, hosting), roadmap for DB options, and clearer AI-oriented docs/SDK patterns to reduce LLM confusion.
