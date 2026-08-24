# The RCE that AMD won't fix

- Score: 369 | [HN](https://news.ycombinator.com/item?id=46906947) | Link: https://mrbruh.com/amd/

### TL;DR

An explicitly outdated disclosure says AMD AutoUpdate retrieves executable URLs over HTTP, performs no signature or certificate validation, and immediately runs the download. A network attacker controlling DNS, Wi-Fi, a router, or an ISP could therefore substitute malware when the updater requests an available package. The researcher says AMD closed the February 5 report as out of scope. Commenters called the triage severe but noted exploitation depends on the updater running during an update opportunity, and debated blocking HTTP versus permitting separately authenticated payloads.

### Comment pulse

- Malicious hotspots, compromised routers, DHCP or DNS spoofing, and ISP interception could inject binaries; an update must be requested during exposure.
- Blocking outbound HTTP was proposed as a hygiene signal—counterpoint: it can break revocation checks and repositories, while signed payloads can remain safe.
- Readers favored banning the updater rather than AMD hardware and suggested requesting a CVE to force proper security triage.

### LLM perspective

- View: If accurate, this is insecure update delivery; the article’s outdated warning prevents treating vulnerability status as current.
- Impact: Affected Windows users could execute attacker-supplied code through a trusted updater; enterprises may remove or network-restrict the utility.
- Watch next: Updated disclosure, affected versions, package signing, HTTPS migration, CVE assignment, AMD advisory, and exploitation evidence.
