# Glassworm Is Back: A New Wave of Invisible Unicode Attacks Hits Repositories

- Score: 205 | [HN](https://news.ycombinator.com/item?id=47387047) | Link: https://www.aikido.dev/blog/glassworm-returns-unicode-attack-github-npm-vscode

### TL;DR

Aikido reports a March 2026 Glassworm campaign across GitHub, npm, and VS Code, with at least 151 repositories matching its decoder pattern. Attackers encode bytes as invisible Unicode variation selectors inside an apparently empty JavaScript string; a visible decoder and eval reconstruct and execute the payload, historically fetching a second stage that steals credentials, tokens, and secrets. The campaign disguises injections within project-specific maintenance commits, which Aikido attributes to likely LLM assistance. Commenters argue visual review is insufficient, while noting that eval and unexplained decoding should already block approval.

### Comment pulse

- GitHub should flag abnormal invisible spans platform-wide — counterpoint: source-level ASCII enforcement also mitigates risk but restricts legitimate Unicode use.
- One researcher says GitHub validated a related report, paid $500 and lifetime Pro, yet declined a fix.
- Compromised trusted accounts or rewritten history may explain malicious changes appearing under old, previously clean contributions.

### LLM perspective

- **View:** Treat invisible executable data as a machine-detectable policy violation, not a reviewer puzzle.
- **Impact:** Maintainers, registries, and code hosts share exposure when trusted identities or histories are compromised.
- **Watch next:** Retroactive repository scans, registry removals, account forensics, and host-level Unicode warnings.
