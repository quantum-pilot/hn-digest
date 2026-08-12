# Turn Dependabot Off

- Score: 194 | [HN](https://news.ycombinator.com/item?id=47094192) | Link: https://words.filippo.io/dependabot/

### TL;DR

Filippo Valsorda argues Go projects should disable Dependabot security alerts because module-level matching produces noisy pull requests even when vulnerable code is unreachable. His example was a one-line fix in an unused elliptic-curve method that triggered thousands of alerts. He recommends scheduled govulncheck scans, which use Go vulnerability metadata and static reachability analysis, plus CI runs against latest dependencies without automatically changing production lockfiles. Dependency upgrades can then happen during normal project work, when maintainers have context to review them.

### Comment pulse

- Many report alert fatigue from unreachable or development-only issues; counterpoint: Dependabot remains useful for routine upgrades, semver breakage detection, and controlled auto-merging.
- Static reachability works especially well in Go; dynamic ecosystems may need different tools or accept more conservative noise.

### LLM perspective

- **View:** Security automation should optimize triage capacity, not update volume; reachability turns vulnerability metadata into actionable risk.
- **Impact:** Maintainers can reserve urgent review for executable flaws while testing upgrades without immediately shipping fresh dependency code.
- **Watch next:** Package and symbol precision across ecosystems, CI sandbox adoption, false-negative rates, and Dependabot filtering improvements.
