# Native all the way, until you need text

- Score: 374 | [HN](https://news.ycombinator.com/item?id=48168058) | Link: https://justsitandgrin.im/posts/native-all-the-way-until-you-need-text/

### TL;DR

After testing SwiftUI, NSTextView, NSCollectionView, and TextKit 2 for streaming Markdown chat, a veteran Apple developer found cross-message selection impossible, updates CPU-heavy or flickery, integration awkward, and basic interactions costly to rebuild. WebKit delivered strong typography, selection, and performance; Electron added convenient diffs and platform integration, explaining why chat-heavy apps adopt web stacks. HN split: some cited performant native editors and Markdown libraries, while others reproduced streaming slowdowns and emphasized browser engines’ mature text systems. Several favored embedding WebKit for rich text rather than replacing the whole app.

### Comment pulse

- Native performance is demonstrably possible → one TextKit 2 editor restyles each keystroke under 8 ms — counterpoint: it required eight months of specialized work.

- Existing SwiftUI libraries help but miss stress targets → Textual exceeded 16.7 ms budgets during long scrolling, live updates, and thousand-turn histories.

- WebKit is already a macOS framework → use it for Markdown surfaces without adopting Electron everywhere, accepting each web view’s memory overhead.

### LLM perspective

- **View:** Rich text is a subsystem, not a widget; selection, accessibility, incremental layout, typography, and interaction semantics compound quickly.

- **Impact:** Teams can preserve native shells while delegating document rendering to WebKit, minimizing both framework fights and full-Electron resource costs.

- **Watch next:** Benchmark streaming latency, frame-time percentiles, selection continuity, accessibility, memory per view, large tables, code blocks, and older hardware.
