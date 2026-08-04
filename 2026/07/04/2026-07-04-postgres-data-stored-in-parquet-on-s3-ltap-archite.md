# Postgres data stored in Parquet on S3: LTAP architecture explained

- Score: 161 | [HN](https://news.ycombinator.com/item?id=48745855) | Link: https://www.databricks.com/blog/lakebase-ltap-rethinking-database-storage

### TL;DR

Databricks’ Lakebase separates Postgres compute from durability: SafeKeeper replicates WAL, while PageServer materializes state into object storage and reconstructs row pages in memory/NVMe caches. LTAP changes the durable representation to Parquet inside Delta/Iceberg, letting Lakehouse engines read the same governed tables. Analytics pins a Postgres LSN, scans materialized columns from S3, then merges recent PageServer changes, avoiding CDC and transaction-server contention. HN saw pipeline simplification but challenged the “single copy” framing because row caches still exist, and questioned proprietary interfaces, S3/NVMe failure modes, conversion catch-up under heavy writes, and latency.

### Comment pulse

- One durable copy is not one physical representation → Parquet is authoritative, while row pages and indexes persist as performance caches.
- Fresh analytics depends on a merge boundary → queries pin an LSN, scan S3, then overlay unmaterialized WAL-derived changes without loading Postgres.
- Openness remains contested → Parquet, Iceberg, and Postgres are standard — counterpoint: the combined transactional/analytical read-write protocol and service layers remain proprietary.

### LLM perspective

- **View:** LTAP preserves specialized compute engines and unifies durability beneath them; its value is operational simplification, not a universal engine.
- **Impact:** Teams could eliminate selected-table CDC, freshness lag, duplicate governance, and OLAP interference, while accepting deeper dependence on Lakebase infrastructure.
- **Watch next:** Publish 50K-TPS materialization lag, cache-miss latency, failover behavior, object-store throttling results, format specifications, and third-party engine interoperability.
