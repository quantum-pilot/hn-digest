# How to Code Claude Code in 200 Lines of Code

- Score: 240 | [HN](https://news.ycombinator.com/item?id=46545620) | Link: https://www.mihaileric.com/The-Emperor-Has-No-Clothes/

### TL;DR

The tutorial builds a functional coding agent in roughly 200 Python lines: describe read, list, and edit tools; ask an LLM for textual tool calls; execute them locally; return results; and loop until it answers normally. HN agreed this demystifies the core, but argued production value lives in omitted machinery: TODO-based planning, context compaction, reliable editing, error recovery, queued user input, snapshots, approvals, and async state. Commenters also flagged the title and implementation’s close similarity to Thorsten Ball’s earlier article and requested attribution.

### Comment pulse

- Minimal core → an agent is fundamentally tools in a loop, making a useful educational implementation and bootstrap point.
- Production gap → TODO reinjection prevents premature stopping — counterpoint: context management, safety, and concurrency rapidly multiply complexity.
- Provenance → readers found title, framing, tools, and terminal colors unusually similar to an earlier tutorial.

### LLM perspective

- View: Two hundred lines explain the control loop, not the reliability envelope that distinguishes a production agent.
- Impact: DIY agents are accessible, but omitted state and recovery mechanisms shift failures onto users and repositories.
- Watch next: Ablation benchmarks for planning and memory, standardized traces, robust tool errors, and resumable approval workflows.
