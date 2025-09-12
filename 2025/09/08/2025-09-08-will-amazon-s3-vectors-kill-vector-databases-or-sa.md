# Will Amazon S3 Vectors kill vector databases or save them?

- Score: 275 | [HN](https://news.ycombinator.com/item?id=45169624) | Link: https://zilliz.com/blog/will-amazon-s3-vectors-kill-vector-databases-or-save-them

- TL;DR
    - Amazon S3 Vectors adds approximate-nearest-neighbor on S3, trading features and throughput for simplicity and cost. Reverse-engineering suggests post-filter retrieval and “good enough” latency, but limited recall under complex filters and deletes. HN sees it as a cold, low-QPS tier, not a replacement for vector databases powering recommender/search. Preview status may improve limits, yet documentation gaps frustrate engineers. Alternatives like pgvector/AlloyDB and services like Turbopuffer compete on performance and ops. Net: a tiered ecosystem, not a winner-take-all.
    - Content unavailable; summarizing from title/comments.

- Comment pulse
    - AWS secrecy hurts planning → Post-filter behavior, degraded TopK after deletes, and reverse-engineering show internals matter — counterpoint: exposing details bloats abstractions; internals change.
    - Right fit: cold, low-QPS workloads → S3 Vectors offers controlled latency and lower storage; vector DBs still win for recall, filtering, concurrency, and write-heavy recsys.
    - Alternatives and cost focus → pgvector/AlloyDB ScaNN and Turbopuffer cited; Azure Search pricey; some apps spend more on retrieval than LLM calls.

- LLM perspective
    - View: S3-as-index formalizes an object-store tier; vector DBs remain for millisecond latency, complex filters, freshness, and heavy writes.
    - Impact: Teams with huge cold corpora reduce storage costs; high-QPS recommendation/search keep dedicated engines or memory-resident indexes.
    - Watch next: GA benchmarks on recall/QPS, documented filtering/consistency semantics, egress-pricing impacts, and connectors to pgvector, Milvus, LangChain, and RAG frameworks.
