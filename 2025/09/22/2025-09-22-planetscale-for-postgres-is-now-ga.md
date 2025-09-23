# PlanetScale for Postgres is now GA

- Score: 248 | [HN](https://news.ycombinator.com/item?id=45334545) | Link: https://planetscale.com/blog/planetscale-for-postgres-is-generally-available

TL;DR
PlanetScale’s managed Postgres is now GA, bringing its Metal performance controls and developer tooling to PostgreSQL, plus migration guides and early customer wins. The roadmap includes Neki, an open‑source sharding layer for Postgres from the Vitess team. HN feedback highlights real performance gains and standout support, but asks for clearer positioning, pricing, and trial options; PlanetScale phased out its free tier and targets production workloads. Migration from Heroku can be tricky due to blocked logical replication, though control over IOPS is praised.

Comment pulse
- Performance and support shine → users report faster queries, quick weekend support, and Insights surfacing missing indexes; Metal lets you buy IOPS and storage.
- Onboarding unclear → weak product/pricing context; no obvious trial; free Hobby tier was removed. — counterpoint: it’s a blog post, not a landing page.
- Migration mixed → some smooth; Heroku blocks logical replication, complicating moves; questions about public-internet connectivity and latency for external consumers remain.

LLM perspective
- View: PS brings Postgres with Metal performance focus and promises Neki sharding; differentiator is operational excellence and IOPS controls over convenience.
- Impact: Targets teams outgrowing Heroku/Neon/Supabase and MySQL/Vitess shops moving to Postgres; expect consolidation toward premium managed Postgres.
- Watch next: Neki release timeline and benchmarks; private networking/peering and latency guidance; clearer pricing/trial, migration tooling for Heroku without logical replication.
