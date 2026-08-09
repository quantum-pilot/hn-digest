# Pgbackrest is no longer being maintained

- Score: 391 | [HN](https://news.ycombinator.com/item?id=47919997) | Link: https://github.com/pgbackrest/pgbackrest

### TL;DR

After thirteen years, pgBackRest’s lead maintainer is ending development and archiving the PostgreSQL backup tool because post-acquisition sponsorship and job searches failed to fund its substantial maintenance workload. Version 2.58 remains available, with mature support for parallel, incremental, encrypted, multi-repository, object-storage backups and WAL management, but any successor must fork under a new name and rebuild user trust. Hacker News thanked the author while debating open-source sustainability: commercial users should fund critical dependencies, yet the code remains available and a company could support a fork if demand converts into revenue.

### Comment pulse

- Users praised reliable local and cloud backups, but their gratitude exposed the gap between production dependence and recurring funding.
- Some saw acquisition as infrastructure risk — counterpoint: existing releases still work, and a fork can continue development.
- Donations seem insufficient for maintenance-heavy infrastructure; commenters proposed paid support, corporate stewardship, or customers directly sponsoring dependencies.

### LLM perspective

- **View:** Obsolescence is a governance and funding event, not an immediate backup outage.
- **Impact:** Operators inherit security, compatibility, and recovery-risk decisions as PostgreSQL and cloud APIs evolve.
- **Watch next:** Repository archival, credible forks, maintainer succession, package-distribution status, and migration guidance.
