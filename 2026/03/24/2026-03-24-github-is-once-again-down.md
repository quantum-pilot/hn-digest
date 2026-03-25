# GitHub is once again down

- Score: 316 | [HN](https://news.ycombinator.com/item?id=47508608) | Link: https://www.githubstatus.com/incidents/kp06czybl7dw

### TL;DR
GitHub reported a March 24 outage degrading Actions, Issues, Pull Requests, Webhooks and logins, then declared services recovered and promised a root-cause report. Hacker News commenters focus less on the brief disruption and more on perceived long-term reliability decline since Microsoft’s acquisition and the ongoing Azure migration. Many enterprise users say leadership communications are unconvincing and are planning contingencies or migrations to alternatives, while others note GitHub has always been flaky at scale and joke about increasing “Microsoft-ification.”

### Comment pulse
- GitHub feels too unreliable for critical workloads → leadership’s “we’re migrating to Azure” messaging seems hollow, so some enterprises are actively planning life without GitHub.  
- Rising outages seen as “AI effect” and post-Microsoft decay → commenters blame rushed Azure/AI changes — counterpoint: several recall frequent GitHub flakiness long before acquisition.  
- Developers wonder about successors → GitLab and self-hosting implied, but many feel network effects keep them stuck, resorting mainly to Microsoft jokes and nostalgia.  

### LLM perspective
- View: Treat GitHub like any third‑party SaaS, not infrastructure—design for failover, repo mirroring, and CI/CD fallbacks.  
- Impact: Teams with monolithic GitHub Actions workflows or GitHub‑only auth are most exposed to multi-service incidents like this.  
- Watch next: Concrete postmortem details, any MTTR/uptime commitments, and whether competitors capitalize with migration tooling or hybrid-hosted offerings.
