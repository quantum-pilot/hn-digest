# The RCE that AMD wouldn't fix

- Score: 322 | [HN](https://news.ycombinator.com/item?id=48492215) | Link: https://mrbruh.com/amd2/

### TL;DR

AMD AutoUpdate fetched executable URLs over HTTP and ran downloads without cryptographic authentication, enabling network attackers to substitute code. Its bounty platform rejected the report because its MITM scenario was out of scope; after publicity, AMD issued a CVE, patched products, and ended a 124-day embargo without paying the researcher. Ryzen Master uses HTTPS, but the researcher found only CRC-32—not a secure signature—checking downloads. A separate redirect bug may have blocked exploitation anyway. Hacker News debated bounty eligibility versus remediation duty and whether HTTPS alone limits server compromise.

### Comment pulse

- CRC-32 proves integrity, not origin → attackers controlling the manifest or server can replace both payload and checksum without detection.

- Scope is not severity → bounty programs may exclude environmental attacks — counterpoint: vendors still owe users timely remediation for executable substitution.

- The embargo damaged trust → AMD requested silence, provided sparse updates, and waited 124 days despite the researcher viewing the patch as trivial.

### LLM perspective

- **View:** Update systems are privileged software-distribution channels; optional installation does not reduce consequences once installed.

- **Impact:** Hardware vendors need cryptographic release pipelines, coordinated disclosure owners, and triage routes separate from bounty eligibility.

- **Watch next:** Verify actual executable-signature enforcement, patch coverage across AMD tools, updater reachability, CVE guidance, and future disclosure response times.
