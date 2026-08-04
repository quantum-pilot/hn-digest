# GitHub Actions was down

- Score: 646 | [HN](https://news.ycombinator.com/item?id=48278374) | Link: https://www.githubstatus.com/?today

### TL;DR

GitHub Actions and Pages degraded on May 26 from 10:57 to 13:18 UTC. Authentication failures prevented runs from starting and actions from downloading, eventually affecting most Actions runs. GitHub identified the cause by 12:37, reported mitigation around 13:00, and promised a detailed root-cause analysis after resolution. The status history also shows Actions incidents on May 15 and May 20, with 99.66% Actions uptime over 90 days. The supplied HN discussion contains only a pointer to another thread, so no substantive community reaction is available.

### LLM perspective

- **View:** Authentication is a CI control-plane dependency; failures can halt delivery even when repositories and Git operations remain healthy.
- **Impact:** Teams relying exclusively on hosted Actions need manual release paths, retry-safe workflows, and clear rules for bypassing noncritical checks.
- **Watch next:** Authentication isolation changes, runner-start latency, action-download error rates, and whether Pages failures share dependencies with Actions.
