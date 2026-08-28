# Debian 13, Postgres, and the US time zones

- Score: 262 | [HN](https://news.ycombinator.com/item?id=45218111) | Link: https://rachelbythebay.com/w/2025/09/11/debtz/

### TL;DR

After upgrading from Debian 12 to 13, a PostgreSQL installation rejected `US/Pacific`, then silently fell back in a way that produced UTC-aligned daily graphs. Replacing it with `America/Los_Angeles` fixed the issue. The author criticizes Debian’s release notes for omitting the tzdata change. Commenters supplied deeper history: `US/*` names had lived in IANA’s backward-compatibility collection since the 1990s before Debian moved them into `tzdata-legacy`. Others reported similarly disruptive upgrade changes and recommended listing accepted zones with `timedatectl`.

### Comment pulse

- Readers debated whether decades-old deprecation was adequate warning when upgrades can still break production configuration.
- Other Debian 13 upgrade gotchas reinforced complaints that relevant notices are scattered across package-specific documentation.

### LLM perspective

- View: Long deprecation periods do not replace migration diagnostics at the moment compatibility is removed.
- Impact: A rejected timezone can stop services or, worse, silently shift reporting boundaries after a workaround.
- Watch next: Audit legacy zone aliases before upgrades and check service logs, release notes, and package NEWS together.
