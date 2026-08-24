# Stop Breaking TLS

- Score: 141 | [HN](https://news.ycombinator.com/item?id=46214950) | Link: https://www.markround.com/blog/2025/12/09/stop-breaking-tls/

### TL;DR

A DevOps architect argues that corporate TLS interception replaces end-to-end trust with an organization-controlled certificate and decryption bottleneck, concentrating compromise risk while exposing sensitive traffic. Operationally, custom roots splinter across operating systems, runtimes, containers and appliances; inevitable gaps normalize --insecure workarounds, obscure failures and create availability costs. HN commenters strongly corroborated that friction, blaming compliance theater and inconsistent certificate stores, though some distinguished enterprise interception from deliberate TLS termination at public reverse proxies such as Cloudflare.

### Comment pulse

- Explicit proxies offer cleaner failure boundaries → clients declare interception, while network teams retain a visible troubleshooting point.
- Certificate plumbing is fragmented → Git, Python, Rust, Java, Bazel and Linux distributions each expose different trust paths.
- Centralized inspection invites vendor risk → commenters cited vulnerable appliances, compliance incentives and a powerful private key.

### LLM perspective

- View: Security controls fail when they habituate users to bypass warnings.
- Impact: Developers lose time; organizations inherit broader privacy and outage exposure.
- Watch next: Explicit proxy adoption and native trust-store convergence.
