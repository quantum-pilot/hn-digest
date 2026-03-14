# TUI Studio – visual terminal UI design tool

- Score: 533 | [HN](https://news.ycombinator.com/item?id=47362613) | Link: https://tui.studio/

### TL;DR
TUI Studio is a Figma-style visual editor for building terminal UIs: drag-and-drop components, CSS-like layout (absolute, flex, grid), multiple color themes, and saving designs as `.tui` JSON. It aims to export production-ready code to six popular TUI frameworks (Ink, BubbleTea, Blessed, Textual, OpenTUI, Tview), but export is non-functional in this alpha, so it’s currently a layout/prototyping tool. HN discussion focuses on TUI vs GUI philosophy, aesthetics, and whether an export-less alpha is practically useful.

---

### Comment pulse
- Alpha limitations → Without working code export or resize behavior details, it’s only a visual mockup tool, not a full TUI development workflow yet.  
- What is a TUI? → Disagreement whether mouse-support and GUI-like widgets make it a “GUI in disguise”; others cite Turbo Vision, Zellij, and terminal constraints as defining TUIs.  
- Aesthetics and UX → Some want dense, text-first TUIs and dislike “low-res GUIs”; others argue historical TUIs were exactly that and value mouse-aided discoverability.

---

### LLM perspective
- View: Useful as a visual TUI wireframing tool today; real value arrives only when robust multi-framework export ships.  
- Impact: Could lower barriers for designers/devs to prototype TUIs, especially for SSH-centric tools and CLI-driven products.  
- Watch next: Shipping exports, handling terminal resizing responsively, and validating generated code quality in real projects across the six target frameworks.
