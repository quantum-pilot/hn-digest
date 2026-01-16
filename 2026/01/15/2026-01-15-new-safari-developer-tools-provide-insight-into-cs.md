# New Safari developer tools provide insight into CSS Grid Lanes

- Score: 116 | [HN](https://news.ycombinator.com/item?id=46626210) | Link: https://webkit.org/blog/17746/new-safari-developer-tools-provide-insight-into-css-grid-lanes/

### TL;DR
Safari Technology Preview adds “Order Numbers” to its Grid Inspector, visualizing the actual DOM order of items in CSS Grid, Subgrid, and the new masonry-style Grid Lanes. This makes it far easier to reason about the perpendicular content-flow model and to tune `flow-tolerance` so layouts stay dense without wrecking keyboard and screen reader order. HN commenters like the idea for responsive sidebars and masonry grids, but note Mac-only devtools, Safari’s long-standing memory issues, and weak polyfills elsewhere.

---

### Comment pulse
- Grid Lanes use cases → responsive layouts where sidebar content interleaves on small screens but moves cleanly to sidebars on large screens—counterpoint: current polyfill’s column sizing is inaccurate.  
- Safari quality debate → some see Safari as slow to “decent”; others use it daily as primary dev browser and find complaints outdated.  
- Platform and reliability limits → devtools are macOS-only, and a persistent “silent memory restart” bug makes testing large apps in Safari frustrating.

---

### LLM perspective
- View: Visualizing DOM order for complex layout modes meaningfully bridges layout power with accessibility and predictable tab/screen-reader flows.  
- Impact: Front-end teams building masonry feeds, galleries, and responsive sidebars gain safer tools to compact content without hidden UX regressions.  
- Watch next: Cross-browser devtools parity for order visualization, `flow-tolerance` standardization, and better polyfills or fallbacks for non-Safari environments.
