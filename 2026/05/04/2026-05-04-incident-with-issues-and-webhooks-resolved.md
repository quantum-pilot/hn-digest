# Incident with Issues and Webhooks – Resolved

- Score: 418 | [HN](https://news.ycombinator.com/item?id=48010301) | Link: https://www.githubstatus.com/incidents/72q3n8yxthcy

### TL;DR

GitHub’s May 4 incident began at 15:45 UTC with degraded Issues and Webhooks, then expanded to Git Operations, Pull Requests, Actions, Packages, Pages, and Codespaces. GitHub reported normalized latency by 16:29, mitigated affected services through 16:36, and closed the incident at 16:40; a root-cause analysis remained pending. Commenters described repeated work interruptions and debated whether agentic coding’s reported activity surge explains the reliability decline. Skeptics argued that inefficient architecture and older deterioration cannot be excused by demand that accelerated only recently.

### Comment pulse

- Users called weekly disruptions a business problem and considered Codeberg — counterpoint: broad uptime aggregators may overcount minor component degradation.
- One camp emphasized commits and Actions minutes multiplying rapidly; another blamed expensive request paths and insufficient simplification of common operations.
- Geographic timing softened impact for some European users, showing global status does not equal uniform user-visible downtime.

### LLM perspective

- The RCA should quantify trigger, saturation points, dependency propagation, mitigation timing, and capacity changes.
- Publish severity-weighted availability for critical workflows, not merely whether any component experienced degradation.
- Watch pricing, rate limits, and free-tier policy if automated usage continues reshaping load.
