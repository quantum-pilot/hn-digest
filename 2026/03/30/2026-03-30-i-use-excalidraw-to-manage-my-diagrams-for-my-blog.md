# I use Excalidraw to manage my diagrams for my blog

- Score: 267 | [HN](https://news.ycombinator.com/item?id=47571376) | Link: https://blog.lysk.tech/excalidraw-frame-export/

### TL;DR

A blogger automated Excalidraw exports after each diagram revision required nine clicks and 45 seconds to produce separate light- and dark-mode SVGs. An initial GitHub Action rendered changed frames but had bugs, depended on an x86 container unavailable locally on the author’s ARM Mac, and left previews stale until push and pull completed. The replacement is a forked VS Code extension: wrap elements in a frame named `export_<name>`, and it writes both SVG variants beside the source on every change. HN discussion broadened into format compatibility and diagramming-tool tradeoffs.

### Comment pulse

- Separate SVGs preserve GitHub compatibility because it reportedly cannot switch embedded SVG colors through preference-aware CSS.
- Mermaid excels at process flows and can be pasted into Excalidraw, then manually rearranged for higher-level visual polish.
- Users praised the concept but reported arrow attachment, resizing, undo, styling, and stalled-feature frustrations in Excalidraw itself.

### LLM perspective

- **View:** Naming frames as build targets turns an editable canvas into a lightweight source format with deterministic derived assets.
- **Impact:** Writers can iterate prose and visuals together without breaking local preview or manually synchronizing theme variants.
- **Watch next:** Upstream adoption, ARM-compatible rendering, stale-export deletion, filename collisions, CI reproducibility, and extension maintenance.
