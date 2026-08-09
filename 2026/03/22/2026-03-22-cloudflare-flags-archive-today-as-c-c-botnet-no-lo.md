# Cloudflare flags archive.today as "C&C/Botnet"; no longer resolves via 1.1.1.2

- Score: 363 | [HN](https://news.ycombinator.com/item?id=47474255) | Link: https://radar.cloudflare.com/domains/domain/archive.today

### TL;DR

Cloudflare’s security-filtering resolver at 1.1.1.2 returns 0.0.0.0 for archive.today and sibling domains after categorizing them under command-and-control, botnet, DNS tunneling, and other filters. The supplied page mostly shows resolver and certificate data, so the motive is inferred from discussion rather than established there. Commenters connected the block to allegations that archive.today has used visitor-side JavaScript to flood a blogger’s search endpoint; others emphasized investigations, pressure on the archive, and disputes over attempts to identify its operator.

### Comment pulse

- This is the malware-filtering resolver, not ordinary 1.1.1.1 → users choosing 1.1.1.2 should expect category-based blocking.
- Blocking supporters cited an ongoing browser-mediated denial-of-service campaign → counterpoint: defenders framed the archive as a pressured, free public service.
- Operator anonymity remains contentious → some called identity research doxxing, while others saw scrutiny of a widely used service as legitimate.

### LLM perspective

- **View:** The resolver behavior is observable; Cloudflare’s evidentiary basis is not in the supplied material.
- **Impact:** Users of security-filtering DNS lose these archive domains, while normal resolver behavior is not demonstrated here.
- **Watch next:** Cloudflare’s classification explanation, remediation path, domain rechecks, and confirmation of the alleged client-side traffic.
