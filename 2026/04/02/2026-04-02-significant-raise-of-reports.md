# Significant raise of reports

- Score: 272 | [HN](https://news.ycombinator.com/item?id=47611921) | Link: https://lwn.net/Articles/1065620/

### TL;DR

A Linux kernel security-list maintainer reports vulnerability submissions rising from 2–3 weekly two years ago to 5–10 daily in 2026. Unlike last year’s AI-heavy noise, most current reports are valid, duplicates now appear daily, and extra maintainers were recruited. He suspects automated discovery is draining a longstanding bug backlog faster than new defects arrive, potentially ending embargoes and forcing continuous maintenance. HN debated his “security bugs are just bugs; update regularly” conclusion: exploitability is hard to classify, but upgrades can break systems or introduce supply-chain risk, especially for embedded devices.

### Comment pulse

- Kernel defects can become exploitable after initial classification; LTS branches offer bug fixes without adopting every new feature.
- The surge may be temporary because automated tools are flushing decades of accumulated vulnerabilities rather than revealing today’s steady-state creation rate.
- Offline appliances can safely avoid perpetual updates — counterpoint: connected software cannot remain “release-and-disappear” once cheap automated attacks target everything.

### LLM perspective

- **View:** Automation moves the security bottleneck from finding defects to validating duplicates, fixing code, and distributing trustworthy updates.
- **Impact:** Maintainers need triage capacity and durable funding before faster discovery translates into safer software.
- **Watch next:** Valid-report rates, duplicate frequency, backlog depletion, time-to-fix, maintainer burnout, embargo practices, exploitation, and update regressions.
