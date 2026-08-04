# OpenBSD has a use-after-free allowing local privilege escalation to root

- Score: 243 | [HN](https://news.ycombinator.com/item?id=48831658) | Link: https://nvd.nist.gov/vuln/detail/cve-2026-57589

### TL;DR

CVE-2026-57589 affects OpenBSD through 7.9: a context-switch use-after-free after tsleep in sys_semget() can enable local privilege escalation to root. NVD rates it High at 7.8, while MITRE gives 7.4 and differs on required privileges and attack complexity; a source commit is listed as the patch. HN linked discovery to Trail of Bits and OpenAI’s Patch the Planet effort. Discussion emphasized that this is local, not remote, praised OpenBSD’s sparse vulnerability record, and debated whether simplicity, training-data bias, or selective disclosure explains comparisons with Linux and FreeBSD.

### Comment pulse

- Automated auditing found a serious issue in a security-focused codebase → cheaper analysis broadens coverage without nullifying disciplined engineering that leaves fewer defects.
- Cross-project counts are not clean quality rankings → Linux’s larger surface and greater training representation may make models find more issues there.
- OpenBSD’s record drew praise → only one local escalation was reported — counterpoint: reduced functionality and disputed security disclosure practices complicate interpretation.

### LLM perspective

- **View:** Local root escalation remains severe because any compromised low-privilege account can potentially cross the system’s primary security boundary.
- **Impact:** AI-assisted auditing changes vulnerability-discovery economics, making code minimization, memory safety, rapid triage, and explicit advisories increasingly valuable defenses.
- **Watch next:** Official advisory publication, supported-release patches, exploit reliability, root-cause analysis, similar sleep-boundary lifetimes, and reproducible comparisons across operating systems.
