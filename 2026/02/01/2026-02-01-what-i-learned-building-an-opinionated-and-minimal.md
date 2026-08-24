# What I learned building an opinionated and minimal coding agent

- Score: 339 | [HN](https://news.ycombinator.com/item?id=46844822) | Link: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/

### TL;DR

Mario Zechner built pi as a transparent, multi-provider coding-agent stack after larger harnesses accumulated hidden context and changing behavior. Its libraries handle provider APIs, agent events, a low-flicker terminal UI and the CLI; sessions can switch models while tracking context and cost. Its prompt and four tool definitions fit below 1,000 tokens: read, write, edit and bash. It omits built-in plans, to-dos, MCP, background processes, sub-agents and permission checks, favoring files, command-line tools and tmux. The author cites benchmarks; commenters praised context control but disputed unrestricted host access.

### Comment pulse

- Supporters valued complete context visibility, branching and reusable markdown artifacts, seeing customizable agent cores as preferable to rigid proprietary clients.
- Security drew the clearest dispute: the author calls guardrails theater — counterpoint: readers argued OS sandboxes and mandatory approvals still reduce harm.
- Commenters noted provider quirks persist below any unified API, including remote token counting and absent tool-call streaming.

### LLM perspective

- View: Minimal primitives can outperform feature-rich orchestration when they preserve context control, observability and predictable behavior.
- Impact: Power users gain adaptability and lower context overhead, while assuming direct responsibility for isolation and workflow discipline.
- Watch next: Reproducible benchmark submissions, compaction, streamed tool output, provider compatibility and empirical security comparisons.
