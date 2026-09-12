# I've operated petabyte-scale ClickHouse clusters for 5 years

- Score: 207 | [HN](https://news.ycombinator.com/item?id=49601138) | Link: https://www.tinybird.co/blog/what-i-learned-operating-clickhouse

### TL;DR

A Tinybird cofounder distills years operating petabyte-scale ClickHouse clusters: initial setup is easy, but cost, ingestion, upgrades, and reliability demand specialized systems and repeated practice. He favors separate write replicas, workload-aware routing, careful batching and partitioning, backpressure, mixed-version CI, and testing real query workloads before upgrades. He argues compute-storage separation usually helps, yet warns open-source zero-copy replication can lose data and leak storage objects. These are practitioner recommendations shaped by Tinybird’s modified fork and architecture.

### Comment pulse

- Database gatekeepers can help → Review and rate-limiting improve reliability when schemas, query volume, and datasets become large.
- Operational patterns remain bespoke → Teams often build distinct ingestion, querying, storage, and failure-handling systems around ClickHouse.
- Simpler tools may suffice → Some startups can serve most analytics workloads with DuckDB against object storage.

### LLM perspective

- View: ClickHouse’s performance shifts complexity from query execution into disciplined operations and data modeling.
- Impact: Teams without dedicated expertise may exchange infrastructure savings for hidden reliability and staffing costs.
- Watch next: Open-source cloud-storage maturity, zero-copy safety, upgrade automation, and measured total cost across architectures.
