# GitHub is having issues now

- Score: 291 | [HN](https://news.ycombinator.com/item?id=47924775) | Link: https://www.githubstatus.com

### TL;DR
GitHub’s status page shows a fresh April 27 incident where degraded search and Elasticsearch problems intermittently broke viewing issues, pull requests, Actions, and Packages, plus a dense cluster of other April outages across Copilot, Codespaces, Projects, Pages, and more. HN commenters say today’s issues fail silently (empty PR lists, broken filters) and follow earlier silent merge-queue regressions that corrupted main branches. Many who were forced to migrate from GitLab/self-hosting now see GitHub’s reliability as a direct business risk and are exploring multi-forge setups or alternatives.

---

### Comment pulse
- Silent failures erode trust → UI claims “no PRs” or hides items while data still exists; past merge-queue bugs even damaged trunk — counterpoint: some joke it “clears” their backlog.  
- Corporate GitHub mandates hurt → losing GitLab-style groups, awkward account policies, and repeated outages now threaten revenue when release dates slip.  
- Redundancy and exits → people recommend mirroring to other forges or self-hosting Gitea/Forgejo/GitLab, though migrating issues, PRs, and CI remains painful; some suspect broader Azure problems.

---

### LLM perspective
- View: GitHub’s highly coupled services plus rapid AI feature rollout are increasing operational blast radius when core infrastructure falters.  
- Impact: Teams with GitHub-only CI, code review, and AI assistance effectively share one SPOF, turning minor vendor incidents into financial or compliance crises.  
- Watch next: Standardize exports, backups, and federation-friendly workflows so moving or temporarily failing over from GitHub becomes a rehearsed, low-drama procedure.
