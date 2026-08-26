# Cowork: Claude Code for the rest of your work

- Score: 520 | [HN](https://news.ycombinator.com/item?id=46593022) | Link: https://claude.com/blog/cowork-research-preview

### TL;DR

Anthropic’s Cowork research preview repackages Claude Code’s agentic workflow for non-programmers on macOS. Max subscribers can grant selected folders and connectors, then ask Claude to organize files, build spreadsheets, draft documents, queue tasks, or combine skills with browser access. Anthropic says users retain permission boundaries and approval points, but warns about destructive actions and prompt injection. HN discussion focused overwhelmingly on safety: commenters questioned asking novices to detect attacks, demanded automatic snapshots and rollback, and debated whether a virtual-machine sandbox meaningfully prevents data exfiltration.

### Comment pulse

- Sandboxing narrows exposure → only selected folders enter a VM — counterpoint: permitted network or filesystem actions can still leak data.
- Irreversible operations alarm experts → Cowork lacks built-in revision history, so commenters proposed automatic snapshots or hidden version control.
- Early access exposed product gaps → users asked about Linux support, commercial terms, and basic website reliability.

### LLM perspective

- View: Cowork’s accessibility increases the importance of safety defaults because its target users cannot audit agent behavior.
- Impact: Document work may accelerate, but destructive mistakes or injected instructions can produce losses outside ordinary chat boundaries.
- Watch next: Require transactional file operations, rollback, restricted networking, clearer permissions, and measurable prompt-injection resistance before broad release.
