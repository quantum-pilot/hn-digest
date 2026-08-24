# Pocketbase – open-source realtime back end in 1 file

- Score: 601 | [HN](https://news.ycombinator.com/item?id=46075320) | Link: https://pocketbase.io/

### TL;DR

PocketBase packages a realtime SQLite database, authentication, local or S3 file storage, an admin dashboard, REST APIs, subscriptions, migrations, and Go or JavaScript extension hooks into one portable backend binary. Commenters described it as productive and reliable for prototypes, internal tools, and small-to-medium production applications, especially when operational simplicity matters more than hypothetical scale. Reservations centered on SQLite’s missing decimal type, occasional breaking changes, unsupported edge cases, questions about GIS and PostgreSQL support, and dependence on a single maintainer.

### Comment pulse

- Single-binary operations beat premature distribution → most CRUD applications never reach WAL contention before product or user-growth limits.
- Extensibility covers many gaps → hooks, migrations, and SDKs support custom applications — counterpoint: unusual requirements can become difficult workarounds.
- Sustainability worries users → strong production reports coexist with concern that one developer handles releases and community support.

### LLM perspective

- View: Its sweet spot is bounded applications whose teams value deployment speed over database portability and specialized features.
- Impact: Small teams can replace substantial backend scaffolding, but must own migration and continuity plans.
- Watch next: Stable-version progress, breaking-change frequency, maintainer capacity, Raspberry Pi performance, GIS needs, and decimal handling.
