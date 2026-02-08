# It's 2026, Just Use Postgres

- Score: 519 | [HN](https://news.ycombinator.com/item?id=46905555) | Link: https://www.tigerdata.com/blog/its-2026-just-use-postgres

### TL;DR
The article argues that in 2026 most teams should default to “one big Postgres” instead of a zoo of specialized databases. Modern Postgres plus extensions (pg_textsearch, pgvector/pgvectorscale, TimescaleDB, PostGIS, pgmq, pg_cron, JSONB, etc.) can handle search, vectors, time‑series, queues, caching, documents, and geospatial in one system—often using the same algorithms as Elasticsearch, Pinecone, InfluxDB, Redis, and MongoDB. This greatly cuts operational complexity, especially for AI-era workflows where agents need to fork, test, and tear down environments quickly.

---

### Comment pulse
- Postgres-as-default → Reasonable for early stages; once scale/requirements are clear, specialized systems like ClickHouse, Redis, Pinecone can be more cost-effective—counterpoint: you’ll know when you’re truly in that 1%.  
- Complexity tradeoffs → Postgres is powerful but admin-heavy; SQLite remains simpler for single-user or tiny shared apps, yet many find “low-maintenance Postgres” easier than stretching SQLite.  
- Meta reaction → Some see the post as LLM-flavored marketing slop; others note votes mainly reflect agreement with the “use Postgres” sentiment, not article craftsmanship.

---

### LLM perspective
- View: Treat Postgres as the default “data platform,” then introduce specialized systems only when measured pain justifies operational overhead.  
- Impact: Simplifies AI/RAG stacks, small-team ops, and prototyping by unifying storage, search, vectors, and jobs under one SQL interface.  
- Watch next: Independent benchmarks of pgvector/pgvectorscale vs dedicated vector DBs, and tooling that auto-manages Postgres extensions as composable “services.”
