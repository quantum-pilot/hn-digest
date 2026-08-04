# MicroUI – A tiny, portable, immediate-mode UI library written in ANSI C

- Score: 173 | [HN](https://news.ycombinator.com/item?id=48569205) | Link: https://github.com/rxi/microui

### TL;DR

microui is an MIT-licensed immediate-mode GUI foundation in 1,100 lines of ANSI C. It performs no extra allocation, operates within fixed memory, supplies windows, panels, buttons, sliders, text boxes, labels, checkboxes, wrapped text, and layout, then emits drawing commands for any backend capable of rectangles and text. Users praised how easily it embeds into games, debug menus, WebAssembly, and cross-platform experiments. HN’s debate focused on whether its tiny footprint justifies lower-level integration and whether sparse recent maintenance reflects abandonment or a finished substrate.

### Comment pulse

- Minimality produces measurable footprint → a Sokol WebAssembly sample downloaded at 79.6 KB, roughly half Nuklear and one-sixth Dear ImGui.

- Low-level integration is the tradeoff → adopters implement a renderer and input bridge, gaining portability but doing more work than with PyGTK.

- Maintenance status is ambiguous → no recent releases and an alignment bug worry users — counterpoint: under 2,000 lines are feasible to patch locally.

### LLM perspective

- **View:** microui succeeds as infrastructure, not a full toolkit; its deliberately narrow contract is both strength and limitation.

- **Impact:** Embedded, game, and tooling developers gain deterministic memory and backend freedom; application teams inherit rendering, input, and widget-extension work.

- **Watch next:** Verify alignment on strict architectures, compare binary sizes and frame costs, evaluate forks, and document maintained backend examples.
