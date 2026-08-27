# Show HN: Diagram as code tool with draggable customizations

- Score: 104 | [HN](https://news.ycombinator.com/item?id=45706792) | Link: https://github.com/RohanAdwankar/oxdraw

### TL;DR

Oxdraw combines Mermaid’s declarative, versionable diagrams with GUI-style fine control. Its Rust CLI renders Mermaid files, while a React editor lets users drag nodes and subgraphs, reshape connector paths, alter colors and arrows, and persist those adjustments as Mermaid comments compatible with other tools. This targets diagrams that outgrow automatic layout but should remain reviewable beside code. Hacker News welcomed coordinate locking and AI-to-manual workflows, while requesting releases and tags for packaging, hosted access, and exposed intermediate representations for extension.

### Comment pulse

- Hybrid editing fills a real gap → automatic layouts become painful beyond small diagrams, while GUI files resist source control.
- Packaging needs maturity → a MacPorts contributor requested Git tags and releases aligned with Cargo versions.
- Extensibility could widen adoption → commenters asked for intermediate inputs and outputs, hosting, and composable rendering stages.

### LLM perspective

- View: Persisting visual overrides beside Mermaid structure creates a practical bridge between reproducibility and human judgment.
- Impact: Architecture diagrams can evolve in the same commits and reviews as the systems they document.
- Watch next: Add stable releases, constraint semantics, exportable intermediate data, hosted trials, and layout regression tests.
