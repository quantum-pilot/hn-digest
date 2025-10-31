# We saved $500k per year by rolling our own "S3"

- Score: 325 | [HN](https://news.ycombinator.com/item?id=45715204) | Link: https://engineering.nanit.com/how-we-saved-500-000-per-year-by-rolling-our-own-s3-6caec1ee1143

- TL;DR
  - At Nanit’s scale (thousands uploads/sec), S3 PutObject and 24‑hour lifecycle storage dominated costs for video segments processed in ~2s. They built N3: a Rust, in‑memory landing zone with delete‑on‑GET and TTL GC; S3 remains overflow. DNS load balancing, c8gn instances, rustls/Hyper tuning, and TCP ACK/timestamp tweaks raised throughput; idle‑socket timeouts fixed a memory leak. Result: ≈$500k/year saved. HN discussion focused on whether serverless was the right fit and how naming versus reality (‘cache’ vs ‘S3’) shapes expectations.

- Comment pulse
  - Title nit → critics say 'rolled S3' oversells; supporters note client-compat constraints and tangible savings — counterpoint: naming aside, clear write‑up.
  - Architectural critique → serverless added per‑request taxes; some propose processing on upload to collapse S3/SQS/Lambda layers.
  - Privacy concern → continuous cloud baby‑monitor video without E2EE alarms some; others prioritize reliability, note E2EE conflicts with cloud analysis, and say self‑hosting isn’t mainstream.

- LLM perspective
  - View: Unit economics matter: request-priced storage punishes fine-grained ingest; ephemeral buffers can arbitrage pricing without sacrificing SLOs.
  - Impact: Teams may adopt memory/NVMe buffers over S3; vendors could respond with Express tiers or lower request fees.
  - Watch next: Benchmark vs alternatives: Redis/KeyDB, NATS JetStream, local NVMe; test QUIC/HTTP/3, ECDSA certs, and session reuse to cut egress/CPU.
