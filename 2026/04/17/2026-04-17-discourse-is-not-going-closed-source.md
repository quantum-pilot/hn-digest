# Discourse Is Not Going Closed Source

- Score: 206 | [HN](https://news.ycombinator.com/item?id=47802233) | Link: https://blog.discourse.org/2026/04/discourse-is-not-going-closed-source/

### TL;DR

Discourse will keep its GPLv2 codebase open despite Cal.com arguing AI makes public source too exploitable. Its case: SaaS internals remain observable through browsers, APIs, binaries, and behavior, while openness lets maintainers and researchers use the same scanners as attackers. Discourse scans controllers, requires agents to reproduce candidates with failing tests, and ships validated patches; its release fixed 50 AI-found issues. It frames closure as competition, governance, or investor pressure rather than security. Hacker News agreed that AI erodes obscurity and easily reverse-engineered products gain little moat from hidden implementation.

### Comment pulse

- Public code creates urgency and widens review — counterpoint: it does not guarantee defenders discover or patch a vulnerability before attackers.
- Discourse validates scanner findings with failing tests and candidate patches, converting abundant AI reports into a human-reviewable security queue.
- Commenters saw source secrecy losing value because AI can clone behavior or attack endpoints blindly without repository access.

### LLM perspective

- **View:** Openness is not the control; rapid discovery, validation, patching, least privilege, and blast-radius reduction are the security system.
- **Impact:** Maintainers face higher vulnerability throughput, researchers gain leverage, and bounty programs must adapt when discovery becomes abundant.
- **Watch next:** Patch latency, scanner false positives, exploit races, scan pricing, bounty redesign, and evidence comparing open versus closed SaaS.
