# Claude Code On-the-Go

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46491486) | Link: https://granda.org/en/2026/01/02/claude-code-on-the-go/

### TL;DR

A mobile development setup runs up to six Claude Code agents on a pay-per-use Vultr VM, controlled through Termius, mosh, and persistent tmux sessions over Tailscale. Git worktrees isolate parallel features and deterministic ports; a PreToolUse hook sends Poke notifications whenever an agent requests input. Permissive execution is confined to a disposable environment without production access, costing $0.29 per active hour. Commenters liked the asynchronous pattern for exploration but argued that serious review, testing, and polish still require focused desk work and limit useful parallelism.

### Comment pulse

- Managed web sandboxes offer simpler phone access, but local or private VMs retain planning, source, tooling, and environment control.
- Review throughput, not typing, caps concurrency; two or three agents may already exceed one person’s ability to inspect and test changes.
- Mobile prompts can capture spare moments—counterpoint: critics fear continuous availability erodes work boundaries and encourages lower-quality output.

### LLM perspective

- View: Notifications convert agent work into an asynchronous queue, making the phone an orchestrator rather than a development workstation.
- Impact: Developers gain portability but inherit stronger obligations around secret isolation, review discipline, cost control, and session hygiene.
- Watch next: Measure accepted-code quality, review time, abandoned branches, VM costs, and security incidents versus focused desktop workflows.
