# LittleSnitch for Linux

- Score: 1259 | [HN](https://news.ycombinator.com/item?id=47697870) | Link: https://obdev.at/products/littlesnitch-linux/index.html

### TL;DR

Little Snitch for Linux monitors outbound connections by application, records traffic, and blocks destinations through process-aware rules or automatically updated domain and CIDR blocklists. It uses eBPF, requires Linux 6.12 plus BTF, and serves a local web UI that should be authenticated if local software is untrusted. The project explicitly targets privacy rather than adversarial security: caches can overflow and DNS-to-process attribution is heuristic. Its eBPF code and UI are GPLv2, while the free daemon remains proprietary. Early Fedora reports exposed serious compatibility and resource problems.

### Comment pulse

- OpenSnitch users questioned the proprietary daemon → firewall-level visibility is precisely where many Linux users demand inspectable code.
- Process attribution has escape hatches → an allowed browser or interpreter can relay traffic unless rules inspect parent chains and invocation style.
- Fedora users hit failed startup, huge memory use, and CPU saturation → the author acknowledged limited pre-release distro testing.

### LLM perspective

- **View:** It is a polished observability tool with candid limits, not a mandatory-access-control boundary.
- **Impact:** Desktop users gain easier outbound auditing, while security-sensitive deployments still need sandboxing or MAC policies.
- **Watch next:** Fedora and Btrfs fixes, eBPF portability, daemon source policy, and reliable parent-process attribution.
