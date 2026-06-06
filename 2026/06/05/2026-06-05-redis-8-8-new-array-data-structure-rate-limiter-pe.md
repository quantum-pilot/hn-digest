# Redis 8.8: New array data structure, rate limiter, performance improvements

- Score: 197 | [HN](https://news.ycombinator.com/item?id=48382047) | Link: https://redis.io/blog/announcing-redis-8-8/

### TL;DR
Redis 8.8 adds a major new core type—arrays—plus a built-in rate limiter primitive and several quality-of-life features, while significantly boosting throughput. Arrays are sparse, index-addressable containers with fast random access, ring-buffer mode, server-side aggregations, and text search, offering 2x list performance for sliding windows. A new `INCREX` command turns rate limiting into a first-class primitive. Streams gain explicit NACKing, hashes get subkey notifications, time series support multi-aggregations per query, JSON gains explicit float-precision control, and sorted sets add a COUNT aggregator.

---

### LLM perspective
- View: Arrays plus `INCREX` shift Redis further from “just a cache” into a small real-time data/compute platform.
- Impact: Streaming, fraud detection, monitoring, and AI/RAG backends get simpler schemas, fewer Lua scripts, and lower memory usage.
- Watch next: Client-library support patterns for arrays and `INCREX`, benchmarks vs. custom Lua limiters and TSDBs, and cloud-provider adoption of 8.8.
