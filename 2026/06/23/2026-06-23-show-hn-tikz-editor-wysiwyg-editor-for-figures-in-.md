# Show HN: TikZ Editor – WYSIWYG editor for figures in LaTeX

- Score: 311 | [HN](https://news.ycombinator.com/item?id=48645437) | Link: https://tikz.dev/editor/

### TL;DR

TikZ Editor is an MIT-licensed visual and source editor for LaTeX figures, available on the web and as a desktop app. It keeps canvas edits and TikZ code synchronized while preserving existing whitespace, opens full TeX documents with multiple figures, imports SVG/IPE/PPTX, and exports SVG/PDF/PNG. Common shapes, paths, trees, matrices, loops, and styling work; some advanced constructs remain partial or unsupported. HN praised the polished interface and openness, but questioned absolute-coordinate output that sacrifices TikZ’s semantic positioning. The creator cited ambiguity between editable geometry and preserving author intent.

### Comment pulse

- Semantic TikZ improves maintainability → anchors, relative positions, and alignment constraints express intent better than coordinates generated for every element.
- Direct manipulation creates ambiguous edits → dragging a relatively positioned node could alter its reference, offset, or newly introduced coordinate.
- AI materially accelerated development → roughly 700 million Codex tokens cost about $500 through subscriptions versus an estimated $15,000 at API rates.

### LLM perspective

- **View:** A bidirectional editor succeeds when generated code remains idiomatic enough for humans, not merely render-equivalent and mechanically editable.
- **Impact:** Students and researchers gain faster diagram iteration; experienced TikZ authors may resist workflows that flatten abstractions into coordinates.
- **Watch next:** Benchmark round-trip fidelity on hand-written documents, expand decorations and plots, and test constraint-aware dragging against real academic figures.
