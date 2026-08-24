# Show HN: Bonsplit – Tabs and splits for native macOS apps

- Score: 189 | [HN](https://news.ycombinator.com/item?id=46753301) | Link: https://bonsplit.alasdairmonk.com

### TL;DR

Bonsplit is a Swift package providing custom tabs and nested horizontal or vertical panes for native macOS applications. Its controller can create, update, select, move, and close tabs; split or focus panes; and expose lifecycle events through an optional delegate. Configuration controls reordering, cross-pane dragging, empty-pane cleanup, insertion position, animations, sizing, and whether inactive content is recreated or kept alive. The project targets SwiftUI while supplying keyboard navigation, dirty indicators, icons, and advertised 120-fps transitions.

### Comment pulse

- Native macOS tabs fit document windows → custom models need application-level splits and movement — counterpoint: window-level tab APIs already exist.
- Drag-and-drop polish is deceptively hard → the library’s interaction details carry much of its practical value.

### LLM perspective

- View: Bonsplit packages an interaction system, not merely a decorative tab bar.
- Impact: Native app developers can add editor-style layouts without rebuilding focus, lifecycle, and drag behavior.
- Watch next: AppKit integration rationale, accessibility, large-tab performance, state restoration, and real-world adopters.
