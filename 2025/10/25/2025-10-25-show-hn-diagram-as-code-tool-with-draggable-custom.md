# Show HN: Diagram as code tool with draggable customizations

- Score: 104 | [HN](https://news.ycombinator.com/item?id=45706792) | Link: https://github.com/RohanAdwankar/oxdraw

- TL;DR
  - Oxdraw is a Rust CLI + React editor that renders Mermaid diagrams and lets you drag nodes/edges, colors, and routes, then persists those tweaks back into the .mmd as comments. It outputs SVG/PNG and offers a local editing server. HN liked the “diagrams-as-code with precise control” blend, citing pain with PlantUML/Mermaid layouts and desire for lockable coordinates. Feedback focused on distribution (Git tags/releases, Homebrew/MacPorts), adding a license (now MIT), possible hosting, exposing intermediate data, and tight loops with AI-generated diagrams.

- Comment pulse
  - Packageability needs Git tags/releases; MacPorts port exists; Homebrew likely similar; npm/node version noted; hosting requested — counterpoint: server-side dependency complicates cheap static hosting.
  - Diagrams-as-code plus draggable overrides solves layout frustration; users want lockable coordinates/hard constraints to keep automation while preserving manual placements.
  - Expose intermediate model I/O to integrate pipelines and custom renderers; pair with AI to generate Mermaid, then refine visually.

- LLM perspective
  - View: Bridges Mermaid reproducibility with GUI precision; persisting edits as comments preserves compatibility across tools.
  - Impact: Benefits teams documenting architectures, code review pipelines, and AI-assisted reverse-engineering of large codebases.
  - Watch next: Add Git tags/releases, Homebrew/MacPorts builds, explicit coordinate constraints, exportable intermediate schema, and a minimal hosted or desktop option.
