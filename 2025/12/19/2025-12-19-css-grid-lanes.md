# CSS Grid Lanes

- Score: 150 | [HN](https://news.ycombinator.com/item?id=46331586) | Link: https://webkit.org/blog/17660/introducing-css-grid-lanes/

### TL;DR

WebKit introduces `display: grid-lanes`, a native masonry-style layout available in Safari Technology Preview 234. Items flow into the lane that keeps them nearest the container's start, while existing Grid syntax controls responsive columns, unequal widths, spans, explicit placement, gaps, and horizontal “brick” layouts. Appending elements supports infinite content without JavaScript layout calculations. A new tolerance setting treats small height differences as ties, balancing visual packing against logical focus order. Some names and explicit direction controls remain under CSS Working Group discussion.

### Comment pulse

- Developers welcomed replacing JavaScript masonry, absolute positioning, known aspect ratios, and resize recalculation with native layout.
- A critic found lanes cognitively hard to scan because visual rows and source order diverge, especially with infinite scrolling.

### LLM perspective

- View: Grid Lanes solves layout mechanics while leaving content-order usability as a design responsibility.
- Impact: Galleries and variable-height menus gain simpler responsive CSS, spanning, and keyboard-aware placement.
- Watch next: Test cross-browser interoperability, screen readers, focus paths, reflow stability, and final tolerance syntax.
