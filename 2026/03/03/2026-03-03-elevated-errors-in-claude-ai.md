# Elevated Errors in Claude.ai

- Score: 203 | [HN](https://news.ycombinator.com/item?id=47227647) | Link: https://status.claude.com/incidents/yf48hzysrvl5

### TL;DR

Anthropic reported elevated errors across Claude.ai, Claude Code, Cowork, and its developer platform from 03:15 UTC on March 3, implemented a fix at 08:39, and declared resolution at 10:18. The status page gave no root cause. HN users compared sharply different experiences: some described repeated downtime and restrictive Claude Code quotas after switching from OpenAI, while a heavy API customer reported essentially no interruption. Discussion attributed pressure to rapid user growth and constrained GPU capacity, but treated reduced availability as a serious dependency risk rather than evidence about model quality.

### Comment pulse

- AI capacity is procured far ahead and reserve GPUs are expensive — counterpoint: constrained supply does not excuse weak production availability.
- New users reported consuming a four-hour quota within 30 minutes; veterans said complex tasks still justify Claude Max.
- Coding dependence expands outage blast radius, making fallback providers and retained manual engineering skills operational safeguards.

### LLM perspective

- **View:** Recovery updates are not resilience data; users need measured service levels instead of anecdotes from opposite usage patterns.
- **Impact:** Subscribers lose work time; API customers need redundancy; Anthropic risks squandering migration-driven growth.
- **Watch next:** Postmortem, regional metrics, API error rates, quota changes, capacity expansion, and recurring incident frequency.
