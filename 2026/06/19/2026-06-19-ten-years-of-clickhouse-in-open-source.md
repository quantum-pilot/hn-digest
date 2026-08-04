# Ten years of ClickHouse in open source

- Score: 265 | [HN](https://news.ycombinator.com/item?id=48546890) | Link: https://clickhouse.com/blog/open-source-10

### TL;DR

ClickHouse marks a decade since its June 2016 open-source release, tracing roots from 2009 experiments for real-time web analytics through a production server in 2012, replicated deployments, and today’s 2,000-plus contributors. Built from scratch, it combined columnar aggregation with background merge trees after MySQL and contemporary analytical systems failed its scale. The project argues mature open source requires public roadmaps, reviews, CI, releases, documentation, experiments, and contributor credit. HN users reported dramatic wins replacing Elasticsearch, TimescaleDB, and Loki, tempered by migration inertia and workload-specific search limits.

### Comment pulse

- Replacement economics can be extreme → one evaluation cut query latency from 300–500ms to 75ms and projected multimillion-dollar storage into thousands monthly.
- Organizational inertia often beats benchmarks → teams rejected early deployments over unfamiliarity or remain trapped by Elasticsearch legacy load despite favorable proofs of concept.
- Database choice remains workload-specific → ClickHouse excels at scalable analytics and logs; PostgreSQL extensions promise consolidation, while advanced search may still favor Elasticsearch.

### LLM perspective

- **View:** ClickHouse’s durability came from solving an internal workload before productization, then exposing engineering process as part of the product.
- **Impact:** Teams with append-heavy analytical data can collapse specialized infrastructure, but schema ordering and access-pattern knowledge determine realized gains.
- **Watch next:** Compare ClickHouse against DuckDB and PostgreSQL extensions on scale, search semantics, operations, replication, cost, and migration complexity.
