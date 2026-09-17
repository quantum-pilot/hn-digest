# Salesforce Global Outage

- Score: 273 | [HN](https://news.ycombinator.com/item?id=49724488) | Link: https://status.salesforce.com/products/all

### TL;DR

Salesforce recorded a 7-hour-36-minute Core Service disruption, from 07:50 to 15:26 UTC, causing severe delays, intermittent errors, inaccessible services, and failed support-case creation across affected Hyperforce instances. Requests stalled on an internal login service until server resources were exhausted; restarts were abandoned, a tested mitigation rolled out regionally, and incomplete automation required reapplication and manual recovery. Telemetry stayed healthy after 15:26, but Salesforce had not yet published the technical trigger or root cause. Commenters debated operational competence, scale, and platform complexity.

### Comment pulse

- Large-platform reliability is difficult → defenders cited millions of customized tenant applications and continuous upgrades as unusually complex operating conditions.
- Restart attempts drew skepticism → Salesforce tested rolling restarts, then explicitly abandoned them when they failed to address the issue.
- Status transparency was mixed → the detailed instance timeline aided customers, while its sprawling interface frustrated other readers.

### LLM perspective

- View: The timeline shows disciplined narrowing and validation, but mitigation success does not yet explain the originating failure.
- Impact: Customers depending on login and support channels need contingency paths that do not share Salesforce’s affected dependencies.
- Watch next: Review the promised root-cause analysis, permanent fix, recurrence protections, rollout gaps, and scheduled-job impact.
