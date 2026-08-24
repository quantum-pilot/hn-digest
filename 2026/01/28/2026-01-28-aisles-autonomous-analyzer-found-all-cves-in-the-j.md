# AISLE’s autonomous analyzer found all CVEs in the January OpenSSL release

- Score: 191 | [HN](https://news.ycombinator.com/item?id=46789913) | Link: https://aisle.com/blog/aisle-discovered-12-out-of-12-openssl-vulnerabilities

### TL;DR

AISLE says its autonomous analyzer discovered all 12 vulnerabilities fixed in OpenSSL’s coordinated January 2026 release after beginning its hunt in August 2025. OpenSSL’s CTO confirmed that all 12 disclosures came from AISLE; one issue was high severity, one moderate, and ten low. AISLE says five proposed fixes were incorporated, while six additional findings were repaired before release and never received CVEs. Commenters applaud responsible disclosure but warn automated discovery could overwhelm abandoned software and slow distribution patching; several blame OpenSSL’s complex C code.

### Comment pulse

- Responsible reports included reproduction, root cause, and patches → maintainers could validate and coordinate fixes rather than receive unactionable alerts.
- Automated discovery cuts both ways → defenders may find more bugs, while attackers can cheaply target unmaintained long-tail software.
- OpenSSL’s hostile complexity draws blame → commenters argue memory-unsafe C and poor readability make manual assurance especially weak.

### LLM perspective

- View: OpenSSL’s quoted confirmation strengthens AISLE’s claim; broader conclusions about AI security remain the vendor’s interpretation.
- Impact: Maintainers could face a disclosure-volume bottleneck even as analyzers improve detection and patch proposals.
- Watch next: Reproduce AISLE’s recall on unseen codebases, measure false positives, and track downstream patch adoption.
