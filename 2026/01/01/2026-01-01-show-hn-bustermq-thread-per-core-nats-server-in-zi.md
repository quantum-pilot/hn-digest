# Show HN: BusterMQ, Thread-per-core NATS server in Zig with io_uring

- Score: 128 | [HN](https://news.ycombinator.com/item?id=46449812) | Link: https://bustermq.sh/

### TL;DR
BusterMQ is an experimental NATS-compatible message broker written in Zig, using a thread-per-core design and Linux io_uring to push very high fan-out throughput. On a 16‑core Ryzen 9 9950X, its early benchmarks show roughly 2–3× higher publish and delivery rates and much lower tail latency than the Go NATS server in a synthetic 50M‑message test. The HN discussion centers on its architecture, AI-assisted “vibe-coded” development process, unusual Bazel build choice, and expectations around transparency for such projects.

---

### Comment pulse
- Technical curiosity about the stack → People compare Zig vs Rust for thread-per-core servers, ask about hardware, and share similar io_uring experiments.
- Build tooling confusion → Using Bazel for an all-Zig project seems odd; turns out an LLM suggested it and the author just adopted it.
- Meta on “vibe coding” → Single squashed commit and flashy landing page trigger questions about AI involvement and intent; author clarifies there was real iteration and agrees transparency matters.

---

### LLM perspective
- View: A focused NATS-compatible, ultra-fast broker in Zig is compelling for specialized low-latency, high-fan-out workloads.
- Impact: Could appeal to teams hitting scaling limits with Go NATS, and to Zig users needing a native high-performance message bus.
- Watch next: Realistic multi-node benchmarks, durability/streaming features, operational tooling, and how maintainable AI-assisted Zig codebases prove over time.
