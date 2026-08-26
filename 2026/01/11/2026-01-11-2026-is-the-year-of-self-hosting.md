# 2026 is the year of self-hosting

- Score: 140 | [HN](https://news.ycombinator.com/item?id=46580326) | Link: https://fulghum.io/self-hosting

### TL;DR

Cheap mini PCs, Tailscale, and terminal agents can turn self-hosting from a sysadmin hobby into an approachable workflow: install Linux, connect privately, and ask Claude Code to configure containers, security, monitoring, and backups. The author runs 13 services—including Vaultwarden, Immich, Plex, and ReadDeck—on a $379 N150 box using roughly 4 GB of RAM. HN readers welcomed the lower barrier but stressed that security and maintenance remain real; several favored WireGuard, cooperatives, or fewer third-party dependencies.

### Comment pulse

- Private networking is the real unlock → Tailscale simplifies remote access under CGNAT, while WireGuard advocates prefer controlling keys and infrastructure.
- Agents accelerate setup and debugging → veterans still expect constant probing, patching, isolation, and email-deliverability problems.
- Claude-assisted independence is conflicted → the workflow reduces SaaS reliance by depending on a closed, non-self-hosted agent.

### LLM perspective

- View: Agents reduce configuration friction, but operational judgment—not YAML generation—still defines safe self-hosting.
- Impact: Software-literate households can replace selected SaaS products without becoming full-time infrastructure specialists.
- Watch next: Measure breach rates, recovery time, energy costs, and agent-induced misconfigurations across novice deployments.
