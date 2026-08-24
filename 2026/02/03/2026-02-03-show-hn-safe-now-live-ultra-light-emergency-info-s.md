# Show HN: Safe-now.live – Ultra-light emergency info site (<10KB)

- Score: 171 | [HN](https://news.ycombinator.com/item?id=46868479) | Link: https://safe-now.live

### TL;DR

Safe-Now.live is an 8.6KB emergency-reference site for slow connections in the United States and Canada. It centralizes emergency numbers, active declarations, location pages, disaster actions, kit and home-preparation checklists, aid resources and recovery guidance. Its sparse design favors availability over visual polish. HN’s unintended load test exposed the harder problem: trustworthy crisis information. Commenters reported initial downtime, tiny mobile text, decades-old or wrong-region alerts and cumbersome navigation; the creator said several defects were patched during the discussion.

### Comment pulse

- Reliability concerns dominated: a crisis service must withstand surges and avoid stale or geographically incorrect alerts.
- Accessibility feedback emphasized larger touch targets and type because panic, smoke or one-handed use can impair precision.
- One commenter requested IP-based localization to reduce taps, especially on the small state selector.

### LLM perspective

- View: Small payloads help degraded networks, but correctness and legibility are the service’s real reliability budget.
- Impact: Bad localization or stale alerts could misdirect users precisely when verification is hardest.
- Watch next: Automated data validation, accessible mobile testing, CDN resilience and transparent freshness indicators per alert.
