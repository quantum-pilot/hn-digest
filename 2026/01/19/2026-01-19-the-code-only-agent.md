# The Code-Only Agent

- Score: 147 | [HN](https://news.ycombinator.com/item?id=46674416) | Link: https://rijnard.com/blog/the-code-only-agent

### TL;DR
The article argues for “Code-Only” agents that have exactly one tool: `execute_code` in a Turing-complete language (e.g., Python). Instead of calling `ls`, `grep`, or bespoke tools, the agent must always write and run code, producing a “code witness” of its reasoning and work. This makes behavior repeatable, reviewable, and—in strong languages—even verifiable. HN commenters like the simplicity and emergent tooling patterns, but push back on practicality, context bottlenecks, Unix-style tool reuse, and note that multi-tool agents often outperform pure code-only in practice.

---

### Comment pulse
- Single-tool experiments → People successfully use `run_bash`/code-only to auto-create reusable CLIs/skills, but persistence, duplication, and session drift limit long-term reliability.  
- Code witness vs. tools → Critics say wrappers just shell out to `rg` etc., adding bugs and overhead; supporters report fewer errors and more flexibility than shell-only.  
- Performance vs. philosophy → Prior art (smolagents) found modern, small curated toolsets outperform pure code-only, though code-only shines when chaining tools over large, context-busting data.

---

### LLM perspective
- View: Code-only is best treated as a low-level substrate, with higher-level explicit tools for common, stable operations.  
- Impact: Most useful for long-running, auditable workflows, data pipelines, and agent debugging rather than everyday coding assistance.  
- Watch next: Benchmarks comparing code-only vs. mixed-tool agents on reliability, cost, and large-data tasks; standard formats for persisting and reusing generated code tools.
