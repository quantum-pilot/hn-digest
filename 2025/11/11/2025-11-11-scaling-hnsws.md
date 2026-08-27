# Scaling HNSWs

- Score: 138 | [HN](https://news.ycombinator.com/item?id=45887466) | Link: https://antirez.com/news/156

### TL;DR

Redis Vector Sets implement HNSW with 8-bit quantization by default, threaded searches, narrowly locked writes, genuine deletion, serialized graph loading, and optional JSON metadata filtering. The author reports roughly 48,000–50,000 operations per second on a three-million-vector Word2Vec workload, about fourfold vector-memory savings with little practical recall loss, and robust recall after deleting 95% of nodes. The design exposes VADD, VREM, and VSIM primitives so clients can partition indexes and merge results, but its benchmarks and deletion claims remain author-reported.

### Comment pulse

- Readers praised the threading work but questioned HNSW’s fit for huge, heavily filtered datasets.
- Alternatives raised included DiskANN, SPFresh, product quantization, and partitioning by metadata before searching.

### LLM perspective

- View: Redis optimizes HNSW for operational simplicity and mutable in-memory workloads, not universal vector search.
- Impact: True deletion and fast serialization address production pain that raw nearest-neighbor benchmarks often omit.
- Watch next: Independent recall, latency, filtering, and churn tests should verify the reported advantages.
