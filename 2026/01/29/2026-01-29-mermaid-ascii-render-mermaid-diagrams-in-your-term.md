# Mermaid ASCII: Render Mermaid diagrams in your terminal

- Score: 383 | [HN](https://news.ycombinator.com/item?id=46804828) | Link: https://github.com/lukilabs/beautiful-mermaid

### TL;DR

Craft’s MIT-licensed beautiful-mermaid package renders Mermaid source to SVG or synchronous Unicode/ASCII without DOM dependencies. The TypeScript library supports flowchart, state, sequence, class, and ER diagrams, 15 themes, Shiki theme conversion, live CSS-variable switching, and configurable terminal spacing. Its authors say more than 100 diagrams render in under 500 milliseconds. The ASCII engine ports Alexander Grooff’s Go mermaid-ascii and adds three diagram types, Unicode, and configuration. HN discussion values embeddable text output but scrutinizes attribution and derivative work.

### Comment pulse

- Plain-text diagrams work in terminals, source comments, repositories, and Markdown systems lacking Mermaid renderers.
- Critics call the TypeScript implementation derivative — counterpoint: its README credits the Go engine and documents added formats, Unicode, and configuration.
- A reported state-diagram example drops the start edge label → early rendering correctness still needs testing.

### LLM perspective

- View: Text output trades visual expressiveness for portability, diffability, and zero-renderer viewing.
- Impact: CLI tools and coding agents can present architecture without browsers, image files, or hosted rendering services.
- Watch next: Fix state-edge labeling, expand Mermaid syntax coverage, and publish compatibility and rendering-correctness tests.
