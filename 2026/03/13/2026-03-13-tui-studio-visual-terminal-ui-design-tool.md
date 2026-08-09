# TUI Studio – visual terminal UI design tool

- Score: 533 | [HN](https://news.ycombinator.com/item?id=47362613) | Link: https://tui.studio/

### TL;DR

TUI Studio is an alpha visual editor for terminal interfaces: users drag 21 components onto a live ANSI canvas, arrange them with absolute, Flexbox, or Grid layouts, apply eight themes, and save portable `.tui` JSON locally without an account. It promises exports for Ink, Bubble Tea, Blessed, Textual, OpenTUI, and Tview, but code generation is not functional yet, making this primarily a layout prototype today. Discussion splits over whether mouse-driven visual design betrays keyboard-first TUIs; others cite decades of graphical terminal applications.

### Comment pulse

- The editor lowers layout friction → instant cell-based feedback may beat repeated edit-run cycles across several TUI frameworks.
- Production utility is deferred → without code export, designs still require manual translation and maintenance.
- “TUI” describes the rendering medium, not one interaction style → counterpoint: GUI-like controls can sacrifice compact keyboard workflows users expect.

### LLM perspective

- **View:** A framework-neutral intermediate format could matter more than the editor if exporters preserve semantics cleanly.
- **Impact:** TUI authors gain rapid mockups now; cross-framework handoff remains aspirational.
- **Watch next:** Working exporters, resize constraints, keyboard navigation, round-tripping, and accessible component metadata.
