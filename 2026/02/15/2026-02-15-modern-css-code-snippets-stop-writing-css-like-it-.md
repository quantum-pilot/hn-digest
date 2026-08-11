# Modern CSS Code Snippets: Stop writing CSS like it's 2015

- Score: 161 | [HN](https://news.ycombinator.com/item?id=47025851) | Link: https://modern-css.com

### TL;DR

Modern.css catalogs 56 side-by-side replacements for legacy web hacks, tagged by difficulty and browser availability. Examples move centering to Grid, spacing to gap, responsive behavior to container queries, parent selection to :has(), modals and menus to native dialog and popover controls, and colors, typography, animation, and specificity toward newer platform primitives. HN readers liked the reference but noted that some headline techniques reach only 40–50% support; the site's compatibility filter separates broadly deployable features from experiments. Debate over Tailwind and vanilla CSS remained unresolved.

### Comment pulse

- Compatibility is feature-specific → widely available filters expose mature tools, while creative examples may still need fallbacks.
- Utility classes trade stylesheet separation for component locality → teams disagreed whether Tailwind solves or abandons CSS's cascade.
- Native primitives reduce JavaScript and dependencies → overusing sticky or fixed UI can still consume half the viewport.

### LLM perspective

- **View:** Modern CSS is a menu of progressive enhancements, not a mandate to deploy every new feature.
- **Impact:** Teams can delete workaround code while preserving fallbacks according to audience browser data.
- **Watch next:** Interoperability for style queries, scroll-state, anchor positioning, customizable selects, and CSS functions.
