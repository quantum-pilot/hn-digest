# A sharded DuckDB on 63 nodes runs 1T row aggregation challenge in 5 sec

- Score: 197 | [HN](https://news.ycombinator.com/item?id=45694122) | Link: https://gizmodata.com/blog/gizmoedge-one-trillion-row-challenge

- TL;DR
  GizmoData’s pre‑prod GizmoEdge sharded DuckDB across ~1,000 pods on 63 Azure E64pds v6 nodes to run Coiled’s 1‑trillion‑row challenge: COUNT(*) <0.5s; station group‑by min/max/avg <5s (412 rows). The server splits queries; workers process local shards and stream Arrow IPC intermediates; integrity verified via SHA‑256/MD5. HN applauds speed but notes it assumes hot, locally staged data; cold‑start/S3 adds minutes and big cost (~4000 vCPUs/30TB). Debates compare Snowflake/BigQuery and cite Ballista/Smallpond. Single‑node GizmoSQL did ~2 minutes.

- Comment pulse
  - 5-second result excludes S3 reads; needs hot, locally staged data and ~4000 vCPUs/30TB—expensive for 24/7. — counterpoint: author says NVMe-local shards; cold-start is minutes.
  - Why WebSockets over raw TCP? → minimal overhead, built-in TLS/auth, framing and multiplexing, easy library support, single-port routing; author chose it for familiarity.
  - Cloud DWs may match with lower ops burden: Snowflake 4XL claimed ~30s; BigQuery pay-per-query; note 4000 vCPUs often means 2000 cores.

- LLM perspective
  - View: Sharded DuckDB with Arrow IPC delivers blistering aggregates when data locality is engineered; limited by IO and coordination overheads.
  - Impact: Makes edge+cloud mixed deployments plausible for sub-10s analytics; less compelling for ad-hoc cold data or cost-sensitive workloads.
  - Watch next: Publish price-performance including ingest; compare to Snowflake/BigQuery; fault tolerance under node loss; try GPU and raw TCP vs WebSockets benchmarks.
