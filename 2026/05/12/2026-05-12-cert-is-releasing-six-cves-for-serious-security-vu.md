# CERT is releasing six CVEs for serious security vulnerabilities in dnsmasq

- Score: 211 | [HN](https://news.ycombinator.com/item?id=48112042) | Link: https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html

### TL;DR

Dnsmasq released 2.92rel2 with fixes for six serious, long-standing CVEs affecting nearly every non-ancient version; vendors received advance notice, and the development branch gets broader root-cause rewrites. Maintainer Simon Kelley says AI security research has produced a continuing flood of reports and duplicates, making triage, embargo coordination, and backports expensive while attackers likely have equal access. He plans to prioritize a timely 2.93 release, requesting rapid release-candidate testing. Commenters debated replacing C with memory-safe languages, distribution backport policies, dnsmasq’s broad scope, and whether less-popular alternatives are genuinely safer.

### Comment pulse

- Memory-safe rewrites gained urgency because many recent findings involve unsafe C — counterpoint: improved automated audits may strengthen existing implementations faster.
- Debian users split over old stable packages: some distrust backport-only forks, while others value predictable maintenance over feature freshness.
- MaraDNS advocates cited clean audits, but replies noted smaller usage and bundled legacy Lua weaken comparisons with dnsmasq’s exposure.

### LLM perspective

- View: AI shifted vulnerability discovery from scarcity to triage overload, reducing the practical value of long embargoes.
- Impact: A small maintainer must balance disclosure, vendor coordination, backports, root-cause work, and frequent releases simultaneously.
- Watch next: Vendor packages, OpenWRT builds, 2.93 testing, exploitability details, and recurring report quality.
