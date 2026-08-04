# Incident with Pull Requests, Issues, Git Operations and API Requests

- Score: 252 | [HN](https://news.ycombinator.com/item?id=48293080) | Link: https://www.githubstatus.com/incidents/xy1tt3hs572m

### TL;DR

GitHub reported degraded API requests, Git operations, Issues, and Pull Requests beginning at 12:10 UTC on May 27. It continued investigating at 12:54 and declared the incident resolved at 13:16, promising a later root-cause analysis but providing no cause or remediation details. HN users framed the 66-minute event as part of an unusually unstable month. The sharpest concern was stale pull-request state allegedly omitting commits or branch changes, which could undermine review safety; speculation blamed Azure migration, AI-driven load, or declining engineering rigor without evidence.

### Comment pulse

- Repeated recent incidents eroded goodwill → commenters who normally defended GitHub now viewed May’s apparent severity cluster as exceptional.
- Stale PR comparisons create more than inconvenience → missing commits in UI or API can cause reviewers to approve an incomplete diff.
- Causes remained contested → Azure migration and agent-generated traffic were proposed, but no status-page evidence connected either to this outage.

### LLM perspective

- **View:** Availability metrics understate incidents when stale metadata can silently corrupt developers’ understanding of what they are reviewing.
- **Impact:** Teams relying on GitHub as a control plane may need independent commit verification before merge during degraded periods.
- **Watch next:** GitHub’s root-cause report, timeline precision, stale-read safeguards, recurrence rate, and evidence separating load growth from deployment defects.
