# CERT is releasing six CVEs for serious security vulnerabilities in dnsmasq

- Score: 211 | [HN](https://news.ycombinator.com/item?id=48112042) | Link: https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html

### TL;DR
CERT has issued six serious CVEs affecting almost all non-ancient dnsmasq versions. Simon Kelley released 2.92rel2 with backported fixes and is rushing 2.93 after a wave of AI-driven security reports uncovered many long-standing bugs. He argues long embargoes are often pointless and prefers rapid, forward-looking fixes over perfect backports. HN discussion circles around alternative DNS servers, whether C-based infra like dnsmasq should be replaced by memory-safe implementations, and how distros like Debian and OpenWRT handle such vulnerabilities.

---

### Comment pulse
- Smaller DNS servers (e.g., MaraDNS) claim spotless recent audits → fewer users and bundled outdated components may just mean issues are undiscovered — counterpoint: simpler designs can indeed reduce bug surface.
- Many want critical network daemons rewritten in Rust/Go → most recent bugs trace to C memory issues; some argue AI tooling mitigates risk without rewrites.
- Packaging and ops concerns: Debian likely backports patches into old dnsmasq; OpenWRT is still building updates; some admins dislike dnsmasq’s all-in-one design and prefer separate DNS/DHCP tools.

---

### LLM perspective
- View: AI security tooling is shifting economics toward continuous vulnerability surfacing, forcing maintainers to favor rapid release cycles over long embargo choreography.
- Impact: Network infra daemons, embedded firmware vendors, and conservative distros must streamline patch pipelines and testing to keep pace.
- Watch next: Emergence of memory-safe drop-in DNS/DHCP replacements, standardized AI-assisted fuzzing in CI, and metrics on vendor patch lag for critical CVEs.
