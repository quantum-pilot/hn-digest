# NIST gives up enriching most CVEs

- Score: 161 | [HN](https://news.ycombinator.com/item?id=47806777) | Link: https://risky.biz/risky-bulletin-nist-gives-up-enriching-most-cves/

### TL;DR

NIST’s National Vulnerability Database will no longer fully “enrich” every CVE (add CVSS scores and detailed metadata). Instead it will prioritize three sets: vulnerabilities in CISA’s Known Exploited Vulnerabilities list, software used by US federal agencies, and broadly defined “critical software” (OSes, browsers, security tools, etc.). NIST will also stop providing independent CVSS scores, deferring to whatever the CVE issuer supplies. This ends NVD’s role as a de facto single source of truth and forces vendors to build their own enrichment pipelines amid an AI‑driven CVE explosion.

---

### Comment pulse

- NVD’s CVSS ratings were often low‑quality; losing them is no big loss, but it sadly perpetuates the flawed CVSS ecosystem.  

- Accurate scoring needs deep product knowledge; external bodies frequently misgrade and over‑escalate issues—counterpoint: vendors have strong incentives to understate their own bugs.  

- AI‑assisted and status‑seeking researchers are flooding maintainers with trivial or non‑reproducible “vulns,” dragging retirees back to triage nonsense.  

---

### LLM perspective

- View: Centralized, fully enriched, universal vulnerability catalogs don’t scale; prioritized coverage plus plural data sources is the realistic future.  

- Impact: Security tools, auditors, and regulated orgs must stop hard‑coding NVD assumptions and design for inconsistent, multi‑source vulnerability metadata.  

- Watch next: Third‑party enrichment services, reputation systems for CNAs’ scoring accuracy, and alternative risk models supplanting bare CVSS numbers.
