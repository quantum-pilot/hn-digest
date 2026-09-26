# Show HN: Whiteboard (YC W26) – An open-source IDE for thoughtful software design

- Score: 401 | [HN](https://news.ycombinator.com/item?id=49833867) | Link: https://github.com/devdotfast/whiteboard

### TL;DR

Whiteboard is an MIT-licensed desktop canvas where coding agents explain architecture, diffs, and implementation decisions visually while linking diagrams and trace excerpts back to local code. It adds VS Code navigation, an AST-aware Rust diff viewer, decision logs, and WASM customization, with macOS and Fedora builds. It cannot yet edit files or handle multi-repository review well. HN commenters praise streaming diagrams and semantic diffs but question the “IDE” label, differentiation from text-based diagram tools, and whether this is a product or agent-interface feature.

### Comment pulse

- Visual review addresses an emerging bottleneck → developers need architecture-level explanations and traceability as agents produce more code than humans can inspect linearly.
- The IDE label overpromises → Whiteboard offers navigation and review but no file editing — counterpoint: familiar terminology helps users understand its intended workflow.
- Simpler artifacts remain credible competitors → Markdown, Mermaid, PlantUML, and C4 diagrams are portable, inspectable, and easy for agents to generate.

### LLM perspective

- View: Whiteboard’s strongest differentiation is bidirectional traceability among diagrams, decisions, diffs, and code rather than diagram generation alone.
- Impact: Agent-heavy teams may review intent and architecture faster, but still need separate editing, testing, and approval workflows.
- Watch next: Evaluate editing support, diagram extensibility, multi-repository reviews, collaborative synchronization, and measurable review accuracy.
