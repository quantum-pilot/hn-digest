# Auto mode is now the default in Claude Code

- Score: 275 | [HN](https://news.ycombinator.com/item?id=49239021) | Link: https://claude.com/blog/auto-mode-default-in-claude-code

### TL;DR

Claude Code now defaults to Auto mode, which lets a classifier approve or block commands instead of requiring a user decision each time. Commenters stressed that this differs from `--dangerously-skip-permissions`: Auto still applies a safety gate, reportedly blocking 89% of dangerous commands in testing. Reactions split between users tired of approval fatigue and those who use prompts to monitor alignment, cost, compliance, or unwanted implementation choices. Several argued that neither classifier review nor reflexive clicking substitutes for version control, scoped credentials, backups, or a VM-grade sandbox.

### Comment pulse

- Default Auto may help code-naive users reach a first result; experts can retain manual control, assuming settings remain respected.
- Command safety is narrower than task alignment: a harmless action can waste tokens, violate process, or steer implementation wrongly.
- Some prefer unrestricted agents inside VMs — counterpoint: sandbox escapes and sensitive credentials still require layered controls.

### LLM perspective

- **View:** Approval UX is a throughput bottleneck, so Anthropic is automating judgment rather than eliminating it.
- **Impact:** New users see fewer interruptions; regulated teams inherit classifier risk and must enforce external policy boundaries.
- **Watch next:** False allows, false blocks, default migration behavior, manual-mode durability, auditing, and enterprise compliance controls.
