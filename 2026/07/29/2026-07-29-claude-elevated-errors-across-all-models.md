# Claude: Elevated errors across all models

- Score: 243 | [HN](https://news.ycombinator.com/item?id=49102150) | Link: https://status.claude.com/incidents/q2kg8n613kr3

### TL;DR

Claude experienced elevated error rates across all models from 19:45 to 21:26 UTC on July 29, a 101-minute incident. Anthropic began investigating at 19:49, identified the issue at 20:33, reported broad recovery by 22:20, and marked it resolved at 22:36; no root cause was disclosed. Commenters criticized recurring availability and joked about weak uptime metrics, while heavy users wanted quota resets. Others described automated failover workflows that monitor Claude’s status and resume paused tmux sessions through Codex or DeepSeek after recovery.

### Comment pulse

- Multi-model redundancy is practical → users automate status checks and tmux keystrokes so another agent can restart Claude-dependent work after recovery.
- Subscription impact matters → a user at 96% of a Max allowance argued that outage-related failures justify a full usage reset.
- Reliability reporting drew distrust → commenters questioned capacity honesty and found displayed uptime percentages changed with viewport width.

### LLM perspective

- View: Agent workflows become more resilient when provider status is treated as machine-readable orchestration input.
- Impact: Long-running coding sessions need checkpointing and provider substitution, not assumptions that one model remains reachable.
- Watch next: Anthropic should publish root cause, affected request rates, quota treatment, and corrective reliability measures.
