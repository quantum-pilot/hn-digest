# Stop Breaking TLS

- Score: 141 | [HN](https://news.ycombinator.com/item?id=46214950) | Link: https://www.markround.com/blog/2025/12/09/stop-breaking-tls/

### TL;DR
The article argues that TLS “inspection” in enterprises is just institutionalized man‑in‑the‑middle: it breaks TLS guarantees, centralizes catastrophic key risk, and creates endless operational friction. Keeping custom root CAs working across OSes, languages, containers, and pinned clients is nearly impossible, so engineers get trained to ignore TLS errors or use `--insecure`, weakening security culture. TLS interception boxes also add latency, bottlenecks, and single points of failure. The author advocates less invasive, more modern approaches like Zero Trust, anomaly detection, EDR, and traffic‑metadata analysis instead. HN comments largely agree, adding war stories and nuance around tooling and Cloudflare.

---

### Comment pulse
- Use explicit HTTPS proxies, not transparent MITM → keeps TLS semantics intact, isolates bugs in one place, and makes network troubleshooting far clearer.

- Fragmented cert/proxy handling is the real nightmare → every tool/OS (Git, Python, Rust, JVM, Bazel, websockets) has its own store and quirks, burning massive engineering time.

- Big vendors ship buggy MITM boxes for compliance theatre → management wants checkbox security; some prefer DNS/IP blocking instead — counterpoint: Cloudflare fronting public sites isn’t equivalent to inspecting all internal traffic.

---

### LLM perspective
- View: Treat TLS inspection as an exception for narrow, regulated use-cases; default to endpoint and metadata-based controls instead.

- Impact: Enterprises and tool vendors should prioritize consistent CA/proxy integration, plus better UX around TLS errors to avoid “curl -k” culture.

- Watch next: Standardized POSIX-style TLS APIs, benchmarks of MITM vs EDR/anomaly detection, and vendor roadmaps for key management and CT-log monitoring.
