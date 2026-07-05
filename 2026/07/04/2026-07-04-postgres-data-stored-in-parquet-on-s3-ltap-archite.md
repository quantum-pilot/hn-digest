# Postgres data stored in Parquet on S3: LTAP architecture explained

- Score: 161 | [HN](https://news.ycombinator.com/item?id=48745855) | Link: https://www.databricks.com/blog/lakebase-ltap-rethinking-database-storage

- TL;DR  
  LTAP here means running Postgres on top of Parquet files stored in S3, with an NVMe “pageserver” cache so most reads avoid S3. OLTP uses Postgres over this cache; OLAP can scan Parquet directly, giving one logical storage copy instead of separate OLTP and warehouse systems plus CDC/ETL. HN discussion highlights: it’s conceptually similar to Lambda/lakehouse and “bottomless” filesystems; performance hinges on the caching tier and network; skeptics question tradeoffs versus specialized OLTP/OLAP engines at high throughput.

  *Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - Architecture = Parquet on S3 + pageserver cache; reads rarely touch S3; format change avoids extra copies vs existing “bottomless” designs.  
  - Object-storage-backed filesystems are trending for databases; cheap capacity but need 5–10 Gbps uplinks and hit latency, throttling, NVMe write and CPU bottlenecks in production.  
  - Skeptics: one engine can’t match best-in-class OLTP+OLAP, especially 50k+ TPS; CDC pipelines are fine when done well—counterpoint: CDC slots burden Postgres and are error-prone.

- LLM perspective  
  - View: LTAP reuses Postgres semantics while shifting durability to Parquet+S3, but caching tier becomes the true performance-critical database.  
  - Impact: could simplify stacks for SaaS vendors needing fresh analytics, but increases dependence on specific LTAP vendors and their infra.  
  - Watch next: benchmarks under mixed OLTP/OLAP loads, any open LTAP protocols, and safe multi-engine access to shared Parquet.
