# Pandas Should Go Extinct

- Score: 187 | [HN](https://news.ycombinator.com/item?id=49668198) | Link: https://eddie.codes/posts/pandas-should-go-extinct/

### TL;DR

The author argues Pandas pushes medium-sized analytics workloads toward distributed systems prematurely, while Polars and DuckDB can handle much of the gap on one machine. In the author’s one-billion-row benchmark, Pandas took 4m28s and 38.12GB memory; Polars and DuckDB finished near five seconds, with DuckDB using 1.93GB. A laptop taxi-data test showed a similar pattern. The post recommends gradual adoption through Apache Arrow, while acknowledging ecosystem switching costs, imperfect benchmarking, and workload-dependent choices. Commenters largely welcome renewed attention to data tooling.

### Comment pulse

- Medium data deserves single-machine tools → commenters see DuckDB and Polars as meaningful progress beyond a supposedly stagnant data-science ecosystem.
- Migration depends on workflow fit → existing Pandas integrations and familiar APIs may outweigh performance gains for smaller workloads.
- The provocative title worked → several readers expected wildlife controversy before discovering a detailed Python performance argument.

### LLM perspective

- View: The strongest case is avoiding distributed complexity, not declaring one library universally obsolete from a narrow benchmark.
- Impact: Analytics teams can reduce infrastructure and iteration costs by testing DuckDB or Polars before adopting clusters.
- Watch next: Reproduce results across joins, strings, nulls, mixed types, storage formats, and end-to-end production pipelines.
