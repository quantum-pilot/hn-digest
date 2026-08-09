# Claude Code Routines

- Score: 363 | [HN](https://news.ycombinator.com/item?id=47768133) | Link: https://code.claude.com/docs/en/routines

### TL;DR

Claude Code Routines, now in research preview, package a prompt, repositories, environment, and connectors into autonomous cloud sessions triggered by schedules, API calls, or GitHub events. They can run shell commands, create branches and PRs, and act through the owner’s connected services without approval prompts while the owner’s computer is offline. Repository, branch, network, secret, and connector settings constrain access; runs consume subscription limits and face daily caps. Commenters saw useful automation but focused on platform lock-in, unclear subscription terms, model reliability, and discrepancies between documented and available triggers.

### Comment pulse

- Some welcomed unattended backlog, alert, review, deployment, documentation, and porting workflows — counterpoint: debugging probabilistic cloud automations could be maddening.
- Users wanted commodity models and portable workflows, distrusting feature sunsets and degradation — counterpoint: agents may make vendor migration fast enough.
- Anthropic’s subscription-versus-third-party automation rules confused developers; documented push and issue triggers also appeared absent from one user’s interface.

### LLM perspective

- **View:** Routines turn an assistant into operational infrastructure; the permission model matters as much as the prompt quality.
- **Impact:** Teams can automate repetitive engineering work, but unattended actions inherit personal identities, secrets, billing, and failure blast radius.
- **Watch next:** Preview stability, trigger parity, ToS clarification, auditability, connector defaults, run caps, and migration paths outside Anthropic.
