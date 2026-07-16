# Dependabot version updates introduce default package cooldown

- Score: 203 | [HN](https://news.ycombinator.com/item?id=48913050) | Link: https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/

### TL;DR
GitHub’s Dependabot now waits three days after a new package version appears in its registry before creating a *version update* PR. This default “cooldown” reduces the risk of immediately pulling in compromised or broken releases, a known supply-chain attack vector. Security updates remain immediate so critical patches aren’t delayed. Teams can override or disable the delay using the `cooldown` option in `.github/dependabot.yml`. The change applies to all supported ecosystems and will ship in GHES 3.23.

### LLM perspective
- View: This nudges teams toward safer dependency practices by default while preserving opt-out flexibility for fast-moving projects.  
- Impact: Most repos see slightly slower upgrades but fewer emergency rollbacks from bad upstream releases.  
- Watch next: Data on compromised releases caught during cooldown windows and how often projects override the default delay.
