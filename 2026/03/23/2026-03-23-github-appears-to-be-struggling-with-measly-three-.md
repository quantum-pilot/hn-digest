# GitHub appears to be struggling with measly three nines availability

- Score: 430 | [HN](https://news.ycombinator.com/item?id=47487584) | Link: https://www.theregister.com/2026/02/10/github_outages/

### TL;DR
GitHub has suffered a string of incidents in 2025–26 affecting Actions, pull requests, notifications, and Copilot, with delays lasting hours. An unofficial reconstruction of GitHub’s old status page, based on their own feeds, shows overall uptime dipping near 90%—far below the 99.9% SLA promised only to Enterprise Cloud customers. Commenters argue that even core services like Git and Actions often fail to reach “three nines,” while GitHub simultaneously pushes AI features and obscures historical reliability, forcing teams to plan seriously for downtime.

---

### Comment pulse
- Uptime measurement is messy → Some say “platform down if any feature down” is unfair, but reconstructed data shows even Git, Actions, API miss three nines.  
- Scale, Azure, and AI strain → Forced Azure migration and AI-driven infra plus AI-generated PR floods stressed an architecture never built for millions of automated coders. — counterpoint: complexity across whole toolchains also erodes perceived reliability.  
- Security and CI design rot → GitHub Actions’ mutable references, long-known issues, and complex YAML ecosystems enable supply-chain attacks; best practice is pinning actions by hash and simplifying CI.

---

### LLM perspective
- View: Treat GitHub as a fallible dependency; design workflows assuming periodic outages of Actions, web UI, and Copilot.  
- Impact: Serious teams, particularly CI-heavy orgs, should evaluate redundancy: mirrors, alternative CI, or partial migration to other Git hosting.  
- Watch next: Independent uptime trackers, GitHub transparency on postmortems, and whether AI traffic growth continues outpacing reliability engineering investment.
