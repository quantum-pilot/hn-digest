# GitHub: Git operation failures

- Score: 315 | [HN](https://news.ycombinator.com/item?id=45971726) | Link: https://www.githubstatus.com/incidents/5q7nmlxz30sk

- TL;DR  
GitHub suffered a global incident on Nov 18, 2025 where Git operations over HTTP and SSH, plus Codespaces, intermittently failed. Degradation began around 20:39 UTC and was fully resolved by 21:59, with a root-cause analysis promised later. Discussion centers less on this specific outage and more on a perceived rise in major SaaS/cloud failures, attributing them to cost-cutting, centralization, and eroding ops culture, while others propose concrete mitigations like local mirrors, HTTP caches, and reducing dependence on GitHub-specific workflows.

- Comment pulse  
  - Outages feel more frequent → commenters cite underinvestment in reliability, layoffs, profit‑chasing, and cloud centralization eroding engineering culture and ops quality—counterpoint: may be availability bias.  
  - Git’s decentralization should cushion outages → in practice, reliance on GitHub Actions, PR workflows, and CI means many engineers are blocked when the hub fails.  
  - Some advocate local mirrors, HTTP git caches, and trimming third‑party dependencies to reduce blast radius; others darkly suggest rising LLM usage is quietly introducing fragility.

- LLM perspective  
  - View: Treat GitHub and cloud providers as eventually‑unreliable dependencies; design workflows to continue locally or via mirrors during provider incidents.  
  - Impact: Teams heavily using GitHub Actions should plan graceful degradation paths, e.g., fallback CI runners and alternative artifact registries.  
  - Watch next: Track outage frequency/length across major SaaS vendors internally; let measured risk, not brand reputation, drive redundancy and multi‑provider investment.
