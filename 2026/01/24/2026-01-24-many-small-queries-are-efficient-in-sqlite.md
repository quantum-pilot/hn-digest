# Many Small Queries Are Efficient in SQLite

- Score: 151 | [HN](https://news.ycombinator.com/item?id=46742635) | Link: https://www.sqlite.org/np1queryprob.html

### TL;DR

SQLite runs inside the application process, removing the IPC that makes repeated queries costly in remote databases. Fossil generates a 50-entry timeline with one complex selection followed by object-specific lookups, often issuing more than 200 statements while finishing in under 25 milliseconds; profiling attributes little time to the database. This separates timeline selection from rendering and keeps check-in, ticket, and wiki logic near each object type. Because SQLite also handles complex relational queries, applications can choose the clearer approach instead of minimizing statement count reflexively.

### Comment pulse

- Read-heavy success has a boundary → concurrent background workers can hit SQLite write contention despite light user traffic.
- Local-query design creates migration coupling → hundreds of calls become costly after adding network latency — counterpoint: many systems never outgrow one host.
- Transaction scope dominates inserts → batching writes avoids paying the durability flush cost for every statement.

### LLM perspective

- View: Query count is a proxy; process boundaries and synchronized durable writes are the actual costs.
- Impact: Developers can favor simple, modular reads without prematurely compressing them into fragile mega-queries.
- Watch next: Concurrent writers, transaction boundaries, storage latency, and any future move to a remote server.
