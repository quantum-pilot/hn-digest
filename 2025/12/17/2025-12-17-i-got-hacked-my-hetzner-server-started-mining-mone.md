# I got hacked: My Hetzner server started mining Monero

- Score: 160 | [HN](https://news.ycombinator.com/item?id=46305585) | Link: https://blog.jakesaunders.dev/my-server-started-mining-monero-this-morning/

### TL;DR
Hetzner warned the author their server was attacking others; they found a Monero miner running inside an Umami analytics container exploited via a critical Next.js RSC deserialization bug (CVE-2025-66478). Because the container ran as a non‑root user, with no mounts or privileges, the compromise stayed inside Docker: deleting the container and tightening the firewall solved it. HN focuses on better firewall tools and outbound filtering, container resource limits, and not treating Docker as a strong security boundary or storing secrets in app containers.

---

### Comment pulse
- Host firewall choice matters → firewalld with StrictForwardPorts handles Docker better than UFW; also restrict outbound connections and consider podman to avoid container bypasses.  
- Apply container resource limits → CPU, memory, and read-only filesystems cap damage from miners or bugs; rotate VMs for workloads handling untrusted user content.  
- Don’t over-trust Docker isolation → root/privileged containers and misconfigurations can enable escapes or DoS. — counterpoint: Non-root, unprivileged containers suffice for many low-value self-hosted setups.

---

### LLM perspective
- View: Story shows real-world value of sane defaults: non-root containers, no mounts, and quick deletion averted a rebuild.  
- Impact: Expect more supply-chain-style incidents where “supporting” frameworks like Next.js are exploited via third-party services admins barely realize they run.  
- Watch next: Watch for hardened orchestration defaults: outbound egress policies, secret-scanning, automatic CVE-based restarts, and opinionated templates discouraging root or privileged containers.
