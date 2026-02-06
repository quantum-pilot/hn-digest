# It's 2026, Just Use Postgres

- Score: 218 | [HN](https://news.ycombinator.com/item?id=46905555) | Link: https://www.tigerdata.com/blog/its-2026-just-use-postgres

## TL;DR
Postgres is argued as the sensible default database in 2026: mature, extensible, and “good enough” for most transactional and analytic workloads, even vectors. Hacker News largely agrees on using it as the primary store and deferring other databases until there’s a clear need. But commenters stress exceptions: SQLite for simplicity and local apps, and purpose‑built systems (ClickHouse, Pinecone, Redis, etc.) for high‑scale analytics or AI. Operational pain points remain: clustering/HA, permissions, and maintaining extensions like vector search.

*Content unavailable; summarizing from title/comments.*

## Comment pulse
- Developers report SQLite feeling great initially but becoming painful with indexing, performance, and tooling; others lean on it for ephemeral data processing and local save-files.  
- Some build on Postgres first, then benchmark specialized stores with traffic to justify switching — counterpoint: AI-heavy startups adopt ClickHouse or Pinecone from day one.  
- Self-hosted ops remain rough: people juggle Patroni, Spilo, CloudNativePG, yet still lack easy, Jepsen-robust HA comparable to Mongo’s replica sets.  

## LLM perspective
- View: Treat Postgres as the backbone store, but design clear boundaries so specialized databases can be plugged in without major rewrites.  
- Impact: Smaller teams gain focus by standardizing on Postgres, while high-growth AI or analytics products should budget early for multi-database expertise.  
- Watch next: Watch for native vector support, simpler HA tooling, and managed Postgres narrowing gaps with today’s specialized search and analytics engines.
