# Clawdbot - open source personal AI assistant

- Score: 363 | [HN](https://news.ycombinator.com/item?id=46760237) | Link: https://github.com/clawdbot/clawdbot

### TL;DR

Clawdbot is an MIT-licensed, self-hosted personal assistant whose local gateway connects many chat services to model APIs, persistent sessions, scheduled jobs, skills, and device tools. It can operate browsers, files, cameras, screens, location, and system commands, with optional Docker isolation for non-main sessions. That breadth enables a genuinely proactive remote secretary, but the main session runs with the user’s full host access. Commenters reported high token costs, rapid self-debugging, and serious security findings, while disputing how broadly those findings apply.

### Comment pulse

- Persistence unlocks practical assistance → scheduled tasks, messaging access, and learned skills let the system act between explicit prompts.
- Default authority is dangerous → the main session can reach host resources — counterpoint: pairing, allowlists, and optional containers provide partial controls.
- Security maturity appears unsettled → roughly 300 open issues and a report alleging hundreds of high-risk findings alarmed users, though commenters disputed scope.

### LLM perspective

- View: A personal agent’s usefulness and attack surface rise together because both come from persistent access.
- Impact: Nonexperts may gain automation while accepting API bills and machine-level compromise risks they cannot evaluate.
- Watch next: Independent audits, safer defaults, permission granularity, cost telemetry, and reproducible review of agent-authored fixes.
