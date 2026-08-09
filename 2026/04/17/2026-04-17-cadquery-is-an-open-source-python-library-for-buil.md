# CadQuery is an open-source Python library for building 3D CAD models

- Score: 216 | [HN](https://news.ycombinator.com/item?id=47772725) | Link: https://cadquery.github.io/

### TL;DR

CadQuery is an open-source Python library for defining parametric 3D CAD models as code, enabling version control, sharing, reusable functions, and parameter-driven iteration without a GUI. Hacker News users described building a slide-rule bracelet, cosplay helmet, winch, functional prints, and prototype brackets. They valued composability and relational “design intent” geometry queries, which can survive earlier model changes better than clicked references. The tradeoff is cognitive load: complex selections remain hard to visualize, GUI CAD can be faster for simple parts, and current AI assistance still struggles with spatial correctness.

### Comment pulse

- Code made design variants cheap: moving triangle indices, changing parameters, or composing functions replaced fragile manual model edits.
- Relational geometry selection preserves intent — counterpoint: users must keep many selectors mentally indexed without richer visual labeling.
- Commenters wanted bidirectional tools where clicks generate code and code updates views; current VS Code viewers only partly bridge that gap.

### LLM perspective

- **View:** Code-first CAD excels when a design is algorithmic, repetitive, configurable, or maintained longer than a one-off sketch.
- **Impact:** Software-fluent makers gain reproducibility and Git workflows, while mechanical expertise remains essential for manufacturable geometry.
- **Watch next:** Bidirectional GUI generation, selection visualization, build123d interoperability, robust import workflows, and measurable improvements in AI spatial reasoning.
