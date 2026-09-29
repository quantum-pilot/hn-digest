# Show HN: Reladraw – A diagram language where you decide where to place things

- Score: 405 | [HN](https://news.ycombinator.com/item?id=49858513) | Link: https://github.com/reladraw/reladraw

### TL;DR

Reladraw is an early-stage text language for diagrams that combines concise source with human-controlled relative placement. Unlike automatic-layout tools such as Mermaid, Graphviz, and D2, it lets authors specify relationships like “right of” or “below” without maintaining absolute coordinates or verbose XML. Version 0.13.0 provides a TypeScript parser, layout engine, SVG renderer, CLI, embeddable web component, and agent skill with zero runtime dependencies. HN sees value for architecture alignment, while noting D2 TALA’s controls, routing bugs, and rapid API churn.

### Comment pulse

- Relative placement fills a practical gap → flowcharts need intentional composition without draw.io’s manual coordinates or auto-layout’s unpredictability.
- Diagrams can align humans and agents → shared visual models preserve architectural understanding while generated code accelerates implementation.
- Existing tools overlap partially → D2 TALA offers layout constraints — counterpoint: Reladraw targets direct composition rather than coaxing an automatic engine.

### LLM perspective

- View: Reladraw’s useful abstraction is spatial intent expressed symbolically, making diagrams editable without surrendering composition.
- Impact: Documentation workflows could keep diagram source compact, reviewable, and easier for agents to modify safely.
- Watch next: Test complex edge routing, layout stability, accessibility, editor support, syntax evolution, and round-trip behavior on real architectures.
