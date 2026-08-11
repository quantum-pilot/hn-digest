# Don't trust AI agents

- Score: 298 | [HN](https://news.ycombinator.com/item?id=47194611) | Link: https://nanoclaw.dev/blog/nanoclaw-security-model

### TL;DR

NanoClaw argues that AI agents should be treated as potentially malicious and constrained outside their own decision-making surface. Its design gives each agent an ephemeral, unprivileged container, separate filesystem and session, explicit mounts, blocked sensitive paths, and host-controlled allowlists. It also favors roughly 3,000 lines of core code plus reviewable skills over OpenClaw’s much larger platform. HN broadly endorsed least privilege and reversible actions, but warned that containers cannot prevent abuse or exfiltration through capabilities an agent is legitimately allowed to use.

### Comment pulse

- Minimize authorized damage → default agents to reading and drafting, then require human approval for consequential side effects.
- Smaller cores aid auditability → fewer dependencies and configurations reduce review burden — counterpoint: line count alone does not establish security.
- Isolation is necessary, not sufficient → email, network, and mounted data remain attack surfaces; production may need VMs, proxies, and egress controls.

### LLM perspective

- **View:** Agent safety is a capability-design problem, not a prompt-writing problem.
- **Impact:** Operators must inventory permissions and make recovery cheap.
- **Watch next:** Adversarial evaluations covering prompt injection, allowed-channel exfiltration, and rollback.
