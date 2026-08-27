# Stop Breaking TLS

- Score: 141 | [HN](https://news.ycombinator.com/item?id=46214950) | Link: https://www.markround.com/blog/2025/12/09/stop-breaking-tls/

### TL;DR

The author argues corporate TLS inspection recreates a man-in-the-middle, concentrates trust in one organizational key, adds performance and availability bottlenecks, and creates extensive certificate-distribution work across operating systems, runtimes, containers, and appliances. Incomplete coverage then trains technical staff to normalize certificate failures and use insecure bypasses. He favors endpoint detection, metadata analysis, network telemetry, and zero-trust designs, while later acknowledging nuance. Commenters largely confirmed operational pain, suggested explicit proxies when inspection is mandatory, and debated comparisons with public TLS termination services such as Cloudflare.

### Comment pulse

- Explicit proxies make interception visible and failures diagnosable, though they do not remove privacy or policy concerns.
- Fragmented certificate stores across Java, Python, Rust, Git, containers, and proxies turn compliance tooling into recurring outages.
- Cloudflare comparisons drew a counterpoint: terminating a public site differs materially from decrypting every connection inside an organization.

### LLM perspective

- View: Inspection’s hidden cost is cultural: routine breakage teaches users to distrust the signal TLS errors provide.
- Impact: Security teams inherit centralized risk and troubleshooting responsibility while developers embed dangerous workarounds into portable automation.
- Watch next: Exception rates, bypass usage, appliance CVEs, and explicit-proxy pilots measured against endpoint-focused controls.
