# Molly guard in reverse

- Score: 204 | [HN](https://news.ycombinator.com/item?id=47455138) | Link: https://unsung.aresluna.org/molly-guard-in-reverse/

### TL;DR

A traditional molly guard adds deliberate friction before a consequential action; Marcin Wichary proposes the reverse pattern for low-risk prompts. A reverse molly guard visibly counts down and automatically chooses a safe default unless the user intervenes, letting long updates, renders, or installations continue unattended instead of waiting overnight for an inconsequential answer. The broader design lesson is to distinguish decisions requiring confirmation from those where progress matters more. Commenters connected the idea to poka-yoke, lockout systems, keyed connectors, and operational safeguards built after mistakes.

### Comment pulse

- DevOps examples ask operators to type a remote hostname or inspect active connections before rebooting production systems.
- Automatic continuation is welcome for trivial choices — counterpoint: surprise reboots can destroy overnight work and violate user intent.
- Defensive hardware succeeds by making incorrect assembly impossible, not merely warning people after they choose badly.

### LLM perspective

- **View:** Good defaults should encode reversibility, consequence, and confidence rather than applying confirmation dialogs uniformly.
- **Impact:** Long-running tools become more trustworthy when users can leave after seeing an explicit path to completion.
- **Watch next:** Timeout accessibility, audit logs, pause controls, and guidance distinguishing safe defaults from destructive automation.
