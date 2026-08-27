# We saved $500k per year by rolling our own "S3"

- Score: 325 | [HN](https://news.ycombinator.com/item?id=45715204) | Link: https://engineering.nanit.com/how-we-saved-500-000-per-year-by-rolling-our-own-s3-6caec1ee1143

### TL;DR

Nanit says it cut about $500,000 in annual costs by placing a Rust, memory-backed service called N3 before S3 in its video-processing pipeline. Thousands of short uploads previously incurred per-request fees and roughly a day of storage despite being processed in seconds. N3 deletes objects after download, garbage-collects stragglers, drains gracefully, and sends overflow to S3. Production testing exposed burstable-network limits, TLS cost, outbound ACK traffic, and stalled-connection memory growth. This is specialized ephemeral buffering, not a general S3 replacement.

### Comment pulse

- Readers praised the engineering detail but disputed the headline’s “rolling our own S3” characterization.
- Some argued the original S3-and-serverless pipeline created avoidable cost; others defended it as a sensible early architecture.

### LLM perspective

- View: N3 succeeds because narrow lifetime and loss constraints make the managed service’s guarantees unnecessary on the happy path.
- Impact: Hybrid fallback preserves durability during trouble while eliminating routine request and storage charges at scale.
- Watch next: Long-term maintenance cost, failure rates, capacity margins, and whether processing can move closer to ingestion.
