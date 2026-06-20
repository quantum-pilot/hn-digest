# Ten years of ClickHouse in open source

- Score: 265 | [HN](https://news.ycombinator.com/item?id=48546890) | Link: https://clickhouse.com/blog/open-source-10

### TL;DR
ClickHouse’s creator recounts how a desperate attempt to speed up Yandex’s web analytics pipeline (OLAPServer + Metrage) evolved into a from-scratch columnar database and, later, a flagship open-source OLAP system. He outlines “levels” of open source, arguing ClickHouse aims for the highest: public roadmap, CI, contributions, experiments, and educational C++ code. The post walks through key architectural milestones (columns, aggregate functions, MergeTree, ReplicatedMergeTree, SQL parser) and makes an explicit appeal: engineers should open-source their own internal systems, even if the early code looks rough.  

---

### Comment pulse
- ClickHouse as ES/Loki/TSDB replacement → huge gains in compression, latency, and cost; some report multi‑million‑dollar savings—counterpoint: legacy and search-specific needs block migrations.  
- Postgres/Timescale users → frustrated by Timescale’s churn and migrations; ClickHouse feels more solid, though Postgres ecosystem is pushing “one database for everything” via extensions.  
- DuckDB comparison → DuckDB praised for embedded analytics; commenters argue ClickHouse scales cluster-wide, while DuckDB targets single-node workflows and smaller-scale problems.  

---

### LLM perspective
- View: This is a rare, detailed blueprint of how a major DBMS was bootstrapped, iterated, and ruthlessly simplified over years.  
- Impact: Reinforces ClickHouse as both production OLAP workhorse and a reference project for serious C++ and systems-performance learners.  
- Watch next: How ClickHouse balances cloud monetization, open governance, and competition from DuckDB, Postgres-based stacks, and proprietary warehouses.
