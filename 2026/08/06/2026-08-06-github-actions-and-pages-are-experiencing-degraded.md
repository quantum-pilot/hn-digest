# GitHub Actions and Pages are experiencing degraded availability

- Score: 374 | [HN](https://news.ycombinator.com/item?id=49198302) | Link: https://www.githubstatus.com/incidents/qcvjkzcs7j74

### TL;DR

GitHub resolved an approximately 11-hour Actions incident that also degraded Pages, Copilot code review, coding agent, webhooks, self-hosted runners, and Enterprise Importer. Jobs were assigned work that no longer existed, queues backed up, webhook processing fell to 15%, and workflow success dropped to 30–40% before fixes restored throughput near 99%. Some ARC pods remained idle and require deletion or redeployment; missed push and pull-request triggers cannot be replayed automatically. HN blamed several possible pressures—explosive AI-generated activity, Azure migration, Microsoft ownership, and weaker engineering—without incident-level evidence distinguishing them.

### Comment pulse

- Scale was the leading theory: commits and Actions minutes reportedly surged, exposing bottlenecks and making backlog recovery cascade.
- Others blamed LLM-written code or Microsoft — counterpoint: commenters cited a longer uptime decline and an ongoing Azure migration.
- Paying users rejected growth as an excuse, especially because self-hosted runners also failed and some teams considered migration.

### LLM perspective

- View: Unreplayable events make recovery correctness as important as queue throughput; a green status cannot reconstruct missed automation.
- Impact: Teams need independent detection for absent CI runs, not just alerts for workflows that start and fail.
- Watch next: Read the promised root-cause analysis; test ARC auto-recovery, webhook durability, capacity headroom, and customer remediation guidance.
