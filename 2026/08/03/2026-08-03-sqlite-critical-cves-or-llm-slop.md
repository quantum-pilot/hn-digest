# SQLite Critical CVEs or LLM Slop?

- Score: 721 | [HN](https://news.ycombinator.com/item?id=49154332) | Link: https://research.jfrog.com/post/sqlite-critical-cves-or-llm-slops/

### TL;DR

JFrog investigated six newly published SQLite CVEs and found fabricated functions, impossible line numbers, nonexistent fixes, wrong signatures, and proofs of concept that either parsed incorrectly or ran cleanly under AddressSanitizer. It says 54 of 55 advisories from one account were false, despite rapid critical scoring and downstream ingestion. The episode exposes a CVE pipeline with weak identity and reproduction requirements after NVD’s validation slowdown. HN worried that cheap AI reports can denial-of-service security teams, pollute scanners, and hide real vulnerabilities beneath administratively expensive noise.

### Comment pulse

- Verification cost is asymmetric → plausible reports take minutes to generate and hours to refute, making human accountability essential.
- Existing CVE signal was already weak → inflated CVSS scores and non-exploitable findings primed automated enterprise gates for failure.
- Maintainer control may restore trust → CNA status can block unreviewed assignments — counterpoint: centralized triage can also suppress legitimate reports.

### LLM perspective

- View: Vulnerability identifiers should record claims only after reproducible evidence and accountable review.
- Impact: Security teams face wasted remediation work; attackers can exploit false-report floods as operational denial of service.
- Watch next: NVD corrections, proof-of-concept requirements, submitter reputation, vendor corroboration, and scanner handling of disputed records.
