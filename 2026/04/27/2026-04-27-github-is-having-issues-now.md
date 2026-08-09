# GitHub is having issues now

- Score: 291 | [HN](https://news.ycombinator.com/item?id=47924775) | Link: https://www.githubstatus.com

### TL;DR

GitHub’s April 27 search incident ran from 16:31 to 22:46 UTC. Connectivity failures and load stressed Elasticsearch, causing intermittent search timeouts and empty or incomplete views across Issues, Pull Requests, Projects, Actions workflow runs, and Packages. GitHub disabled the load source, applied mitigation, and promised a root-cause analysis. A separate overlapping incident caused Copilot Cloud Agent jobs using Codex to fail until 19:02. HN users considered silent empty-result pages more dangerous than explicit errors and renewed calls for forge mirrors or self-hosting, while noting workflows extend far beyond Git repositories.

### Comment pulse

- Missing pull-request lists falsely implied work was complete, creating operational risk beyond ordinary downtime.
- Corporate GitLab-to-GitHub migrations looked especially painful where release dates determine revenue and policies forbid backup arrangements.
- Code mirroring is easy — counterpoint: tickets, permissions, CI, rules, links, and contributor discovery remain difficult to reproduce.

### LLM perspective

- Search-backed views should display freshness and completeness warnings when indexes lag or fail.
- Organizations need tested read-only recovery paths for issues, reviews, workflows, and release metadata.
- Watch GitHub’s promised analysis for isolation changes and controls preventing load amplification.
