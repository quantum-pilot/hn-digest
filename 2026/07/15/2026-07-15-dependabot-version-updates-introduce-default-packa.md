# Dependabot version updates introduce default package cooldown

- Score: 203 | [HN](https://news.ycombinator.com/item?id=48913050) | Link: https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/

### TL;DR

Dependabot now waits three days after a package release before opening version-update pull requests, giving maintainers and automated scanners time to expose compromised or broken releases. The default needs no configuration, covers every supported ecosystem on github.com, and reaches GHES 3.23; teams can change or disable it. Security updates remain immediate. HN generally welcomed the buffer but questioned whether widespread delays reduce real-world detection, debated update churn, and flagged a gap: follow-up releases reportedly do not reset the timer, potentially allowing a known-bad version through.

### Comment pulse

- Detection need not sacrifice early adopters → security firms sandbox new packages, while maintainers spot suspicious tags or rapid releases.
- Update frequency remained contentious → smaller, frequent batches simplify debugging — counterpoint: irrelevant severity alerts and uninspected releases create operational churn.
- High-impact packages may warrant stronger controls → commenters proposed requirements based on download volume, though no selective measure was identified.

### LLM perspective

- **View:** Cooldowns reduce timing risk but cannot establish package provenance or safety.
- **Impact:** Security teams should pair smaller update batches with reachability analysis to avoid alert-driven churn.
- **Watch next:** Test timer resets after replacement releases and measure malicious-package detection within the three-day window.
