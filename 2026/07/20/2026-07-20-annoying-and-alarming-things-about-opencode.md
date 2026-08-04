# Annoying and alarming things about OpenCode

- Score: 367 | [HN](https://news.ycombinator.com/item?id=48978112) | Link: https://wren.wtf/shower-thoughts/stop-using-opencode/

### TL;DR

A source-level critique argues OpenCode’s local-model workflow wastes prompt caches through changing system inputs, brittle compaction, awkward subagents, and a heavy TUI. Its larger concern is security: remote-first defaults, unrestricted networked shells, textual Bash permission filters, persistent prefix approvals, incomplete path checks, and prior HTTP APIs allegedly make restrictions easy to bypass and expose local data or execution. HN found the audit useful but debated whether its criticisms were unique, current, or actionable.

### Comment pulse

- Security critique extends beyond one tool → commenters saw the same unsafe shell-plus-network model across agent CLIs, making harness design the real target.
- Some findings may be stale or fixable → an OpenCode developer says pruning was removed and V2 minimizes instruction-driven cache misses.
- Rhetoric undermined persuasion → readers who agreed technically still rejected insults toward open-source contributors — counterpoint: others found the abrasiveness funny.

### LLM perspective

- **View:** Ambient shell and network access cannot be secured by parsing command text; enforcement must occur below Bash.
- **Impact:** Agent harnesses need OS-level filesystem, executable, credential, and egress policies with deny-by-default capabilities and auditable exceptions.
- **Watch next:** Compare OpenCode V2 against the cited commit using bypass tests, cache benchmarks, outbound telemetry, and independent security review.
