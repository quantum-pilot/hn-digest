# Moving from GitHub to Codeberg, for lazy people

- Score: 501 | [HN](https://news.ycombinator.com/item?id=47530330) | Link: https://unterwaditzer.net/2025/codeberg.html

### TL;DR
- The author shows that moving projects from GitHub to Codeberg can be surprisingly painless: Codeberg’s GitHub import preserves issues, PRs, releases, and labels; Codeberg Pages (or other static hosts) can replace GitHub Pages; and Forgejo Actions with self‑hosted runners plus cross‑compilation can approximate GitHub Actions. The real friction is losing GitHub’s free macOS CI and network effects. HN commenters like Codeberg/Forgejo for FOSS, but many still stick with GitHub for community, CI, and casual/private repos.

### Comment pulse
- Codeberg suits public FOSS projects but feels weak for casual/private code: private repos discouraged/limited; confusion about Pages—counterpoint: Codeberg Pages exists and works.  
- Many keep OSS on GitHub for community, integrations, and generous CI, even as they criticize lock‑in, proprietary dependencies, and ecosystem requirements that assume GitHub projects.  
- Self‑hosted Forgejo is widely praised: light on resources, hackable, easy with Docker and runners, often more reliable than GitHub while avoiding AI crawlers.  

### LLM perspective
- View: Migration guide is strongest for principled maintainers who value autonomy over GitHub’s polished UX, discovery features, and turnkey macOS CI.  
- Impact: If more projects move early, registries and tools may be pressured to drop GitHub-only dependencies and support alternative Git forges.  
- Watch next: Key metrics: stability of Forgejo Actions on Codeberg, availability of macOS runners, and whether Codeberg can scale governance and funding.
