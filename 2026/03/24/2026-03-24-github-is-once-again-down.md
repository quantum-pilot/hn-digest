# GitHub is once again down

- Score: 316 | [HN](https://news.ycombinator.com/item?id=47508608) | Link: https://www.githubstatus.com/incidents/kp06czybl7dw

### TL;DR

GitHub reported a 38-minute incident on March 24, from 20:18 to 20:56 UTC. Actions first showed degraded performance, followed by Webhooks, Issues, and Pull Requests; an update also cited Codespaces and login errors. Services recovered, but GitHub had not yet published the promised root-cause analysis. HN treats the outage as part of a reliability pattern, with customers losing confidence in leadership and the ongoing Azure migration. Others reject easy blame: commenters recall GitHub being slow and flaky before Microsoft’s acquisition or the current AI wave.

### Comment pulse

- Critical workflows need fallback plans → Actions, code review, webhooks, and authentication can fail together on one hosted platform.
- Azure migration draws suspicion — counterpoint: the status page provides no cause, and long-time users remember outages predating Microsoft.
- No clear successor emerged → frustration is high, but migration costs and GitHub’s integrated ecosystem keep teams dependent.

### LLM perspective

- **View:** The incident’s short duration understates its blast radius because multiple development control-plane functions degraded simultaneously.
- **Impact:** Teams with centralized CI and review lost throughput; webhook consumers may need reconciliation after recovery.
- **Watch next:** Root-cause report, recurrence rate, Azure migration milestones, webhook delivery guarantees, and customer continuity measures.
