# Multi-stroke text effect in CSS

- Score: 330 | [HN](https://news.ycombinator.com/item?id=48032265) | Link: https://yuanchuan.dev/multi-stroke-text-effect-in-css

### TL;DR

A retro multi-outline text effect can be approximated by stacking identical, absolutely positioned text layers, assigning each a progressively wider `-webkit-text-stroke`, alternating colors, and ordering them by `z-index`. The browser expands the glyph outline while preserving the font’s shape; adjacent characters merge into a combined silhouette. The demo uses the css-doodle web component to generate many layers compactly. Results vary by font and engine. Large text also flickers and performs poorly, so the author recommends experimentation or image generation, not production.

### Comment pulse

- Readers enjoyed expressive styling beyond standardized systems — counterpoint: css-doodle is a custom component and DSL, not native CSS alone.
- Real layered text can preserve searchable content better than decorative Unicode, though semantics and accessibility still require checking.
- Rendering debate traced Firefox’s curves to distance expansion and Chromium/Safari’s cusp retention, each with geometric tradeoffs.

### LLM perspective

- For shipping, pre-render decorative output while retaining accessible live text underneath.
- Native multi-stroke support could reduce DOM layers, improve performance, and standardize joins.
- Watch paint benchmarks, animation costs, browser interoperability, selection behavior, and screen-reader output.
