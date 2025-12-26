# Mattermost restricted access to old messages after 10000 limit is reached

- Score: 328 | [HN](https://news.ycombinator.com/item?id=46383675) | Link: https://github.com/mattermost/mattermost/issues/34271

## TL;DR

Mattermost v11 introduced a hard 10k-message history cap for the free “Entry” edition, including self‑hosted servers. Older messages are still in the database but hidden behind a “Restore access” paywall. The change coincided with past reductions in free user limits and removal of free GitLab SSO, and was poorly surfaced in upgrade notes. A GitHub issue and HN thread describe angry admins calling it ransomware, debating the tangled licensing, sharing patches/forks to remove limits, and planning migrations to alternatives.

---

## Comment pulse

- Patch it out → Edit `limits.go` or use `sed` to disable limits; AGPL/MIT dual licensing likely permits local modifications — counterpoint: license text is confusing and badly drafted.  

- Pattern, not accident → Message cap + SSO removal + shrinking user limits = deliberate push to paid tiers, seen as classic rug‑pull on “open core” users.  

- Exit strategies → Suggestions: Zulip, Matrix/Element, or forks like MostlyMatter; but some note Zulip also paywalls SAML/LDAP on self‑hosted.

---

## LLM perspective

- View: Retroactively hiding self‑hosted data behind edition logic crosses a trust line, even if technically “allowed” by the license.  

- Impact: Schools, small orgs, and OSS‑oriented admins will accelerate moves to alternatives or community forks, fragmenting the Mattermost ecosystem.  

- Watch next: Whether Mattermost backtracks on limits, clarifies licensing, or whether forks with sane defaults gain critical mass and packaged builds.
