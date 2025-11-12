# Scaling HNSWs

- Score: 138 | [HN](https://news.ycombinator.com/item?id=45887466) | Link: https://antirez.com/news/156

- TL;DR
    - Antirez outlines how to make HNSW practical in Redis: per‑vector int8 quantization (~4× faster/smaller) with near‑identical recall; fully threaded reads and split‑phase writes using per‑thread visited epochs; true deletions via bidirectional links and local repair; serialized graph loading (~100× faster) with integrity checks; and exposing HNSW as a “Vector Set” data structure enabling sharding and JSON‑filtered search. Memory looks workable (3M word2vec ≈3 GB) with ~48k QPS. HN debates filtering at scale, alternatives (Vespa, Turbopuffer), and PQ/DiskANN vs simple int8.

- Comment pulse
    - Filtering dominates performance: HNSW traversal struggles when selectivity is high or unpredictable; Vespa, SPFresh offer alternatives — counterpoint: bound search; far matching results are useless.
    - Quantization matters: commenters favor PQ and DiskANN for production; antirez says int8 already gives near‑perfect recall in‑memory, PQ adds little and slows search.
    - Threading choice stands out: Redis HNSW uses threads despite Redis’s single‑thread heritage, to support parallel reads and partial writes.

- LLM perspective
    - View: Pragmatic design beats novelty: compress vectors aggressively, keep graph simple, thread I/O, and make deletion/serialization first‑class.
    - Impact: Redis becomes a credible in‑memory ANN store for tens of millions of items with simpler sharding and operational recovery.
    - Watch next: Head‑to‑head benchmarks vs DiskANN/Vespa/SPFresh, filter‑selectivity heuristics or cost models, pointer compression, and experiments on single‑level HNSW.
