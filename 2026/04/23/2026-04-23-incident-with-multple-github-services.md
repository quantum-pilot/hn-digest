# Incident with multple GitHub services

- Score: 194 | [HN](https://news.ycombinator.com/item?id=47877644) | Link: https://www.githubstatus.com/incidents/myrbk7jvvs6p

### TL;DR

GitHub reported degraded availability across Copilot, Webhooks, and Actions beginning at 16:12 UTC on April 23. It identified the root problem at 16:52, mitigated Actions and Copilot by 17:03, restored Webhooks at 17:10, and declared the incident resolved at 17:30; a root-cause analysis was still pending. Hacker News commenters treated this as part of a recurring reliability problem, citing third-party uptime estimates and considering Forgejo, SourceHut, or Tangled, while debating whether self-hosting’s speed and control outweigh maintaining another system.

### Comment pulse

- Forgejo users praised fast local pages and runners they control — counterpoint: maintaining a homelab after work creates another sysadmin job.
- Even teams with modest Git-and-Actions needs are evaluating alternatives because repeated outages undermine confidence, despite limited operational impact.
- Commenters challenged status-page optimism with aggregate uptime figures as low as 88.15%, although component and combined availability measure different things.

### LLM perspective

- **View:** The sharper signal is users treating GitHub reliability as an architectural dependency rather than an occasional inconvenience.
- **Impact:** Critical CI pipelines may need local mirrors or fallback runners; casual workflows can tolerate brief interruptions.
- **Watch next:** GitHub’s root-cause analysis, mitigation details, and whether rolling service availability recovers over subsequent months.
