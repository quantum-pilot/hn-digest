# Show HN: ThoughtDAG – An editable context graph for LLM conversations

- Score: 111 | [HN](https://news.ycombinator.com/item?id=49307700) | Link: https://chenxiachan.github.io/thoughtdag/

### TL;DR

ThoughtDAG is an MIT-licensed, local-first desktop canvas where edges define exactly which prior nodes enter an LLM prompt. Users—not autonomous agents—fork, prune, merge, summarize, cite PDF passages, and replay descendants invalidated by upstream edits. It supports many hosted and local models, read-only sharing, file backups, and Markdown export. Commenters recognized an operational version of hand-maintained decision trees but wanted editor integration and cache benchmarks. A reviewer found shell-execution and network-binding vulnerabilities; the creator says rebuilt packages remove shell use, validate input, restrict origins, and bind locally.

### Comment pulse

- Manual context-tree users like executable pruning and staleness replay, but prefer integration with editors and existing Markdown workflows.
- Graph edits improve relevance—counterpoint: early changes may lose prefix-cache reuse, and the project has not benchmarked that tradeoff.

### LLM perspective

- View: Explicit context provenance is valuable, but it explains supplied evidence—not the model's hidden causal process.
- Impact: Researchers and long-running projects gain controllable memory without surrendering graph structure to an autonomous agent.
- Watch next: Security re-audit, editor APIs, cache behavior, hundred-node scaling, replay determinism, and Linux signing should guide adoption.
