# Nobody ever got fired for using a struct

- Score: 141 | [HN](https://news.ycombinator.com/item?id=47225655) | Link: https://www.feldera.com/blog/nobody-ever-got-fired-for-using-a-struct

### TL;DR

Feldera traced a slowdown to serializing SQL rows with hundreds of nullable columns as Rust structs. In-memory niche optimizations kept Option fields compact, but rkyv’s archived strings required explicit discriminants, more than doubling a small example and wasting far more in wide sparse rows. Feldera replaced per-field options with a null bitmap, optionally stored only present values through pointers, and selected dense or sparse layouts per row. Row size and disk I/O halved, restoring throughput. HN debated format-first storage, columnar designs, and whether 700-column schemas are pathology or enterprise reality.

### Comment pulse

- Language-derived persistence is convenient — counterpoint: format-first systems add portability, compatibility, indexes, compression, and security boundaries explicitly.
- Very wide tables look like modeling failures, yet query engines must ingest inherited enterprise schemas reaching hundreds or thousands of columns.
- Better data shape can collapse algorithmic complexity, though access patterns must guide the shape rather than follow slogans mechanically.

### LLM perspective

- **View:** Zero-copy serialization still needs workload-aware schema design; avoiding deserialization does not make every archived layout efficient.
- **Impact:** Feldera users recover throughput without changing SQL, while maintainers absorb custom serialization and compatibility obligations.
- **Watch next:** Dense-versus-sparse thresholds, random-access cost, schema evolution, columnar alternatives, and results on 4,000-column workloads.
