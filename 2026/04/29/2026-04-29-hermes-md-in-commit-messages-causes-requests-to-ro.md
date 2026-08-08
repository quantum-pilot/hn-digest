# HERMES.md in commit messages causes requests to route to extra usage billing

- Score: 935 | [HN](https://news.ycombinator.com/item?id=47952722) | Link: https://github.com/anthropics/claude-code/issues/53262

### TL;DR

A Claude Code user found that the exact, case-sensitive text `HERMES.md` in recent Git commit messages made requests consume paid extra-usage credits instead of the quota included with a Max plan. A minimal reproduction showed lowercase, other extensions, files on disk, and history-free branches did not trigger it. The reporter said $200.98 was consumed while most weekly capacity remained. Anthropic identified an overactive anti-abuse system, fixed the bug, and closed the issue. It later promised affected users full refunds plus usage credits equal to one monthly subscription.

### Comment pulse

- Readers questioned why an anti-abuse system would upcharge rather than block requests, calling the behavior difficult to reconcile.
- The initial refusal dominated reactions — counterpoint: it may reflect a broken support path, not an official compensation policy.
- Several commenters described unrelated double charges and support-bot dead ends, suggesting a broader escalation problem.

### LLM perspective

- Billing decisions must ignore arbitrary prompt content and expose a traceable routing reason.
- Cost anomalies should trigger automatic holds, alerts, and human review before exhausting prepaid balances.
- Support automation needs reliable escalation for reproducible billing defects, with remediation tied to affected accounts.
