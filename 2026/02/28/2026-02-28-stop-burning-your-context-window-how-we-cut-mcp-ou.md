# Stop Burning Your Context Window – How We Cut MCP Output by 98% in Claude Code

- Score: 200 | [HN](https://news.ycombinator.com/item?id=47193064) | Link: https://mksg.lu/blog/context-mode

- TL;DR  
Context Mode is an open-source MCP server that drastically shrinks Claude Code tool output before it hits the 200k-token window, using sandboxed subprocesses and an FTS5-powered knowledge base. Real-world tests show ~98% reduction in context consumed by logs, snapshots, CSVs, and other bulky outputs, extending interactive coding sessions from minutes to hours. HN discussion centers on broader context lifecycle management, comparisons with other output-trimming tools, and whether better tool selection could rival such compression.

- Comment pulse  
  - Context should be editable, not append-only → commenters want automatic pruning of failed attempts, transient logs, and even subagent-based “fork and rollback” workflows.  
  - Author clarifies scope → Context Mode doesn’t shrink MCP tool definitions; it targets output, with subagent routing a surprising driver of overall savings.  
  - Alternative strategies discussed → some argue for simply fewer tools or existing truncation limits; others compare rtk-style local trimming versus searchable indexing approaches.

- LLM perspective  
  - View: Output-side abstraction layers like this will likely become standard for agent IDEs as tool ecosystems and logs keep growing.  
  - Impact: Lowers token costs and latency while enabling richer multi-tool workflows without constantly hitting or degrading the context window.  
  - Watch next: Native vendor support for searchable side stores, better per-message pruning controls, and benchmarks across models and tool-chaining patterns.
