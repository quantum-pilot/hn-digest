# Modern CSS Code Snippets: Stop writing CSS like it's 2015

- Score: 161 | [HN](https://news.ycombinator.com/item?id=47025851) | Link: https://modern-css.com

- TL;DR  
  Modern.css is a catalog of 56 “old vs modern” snippets showing how recent CSS features replace 2010s-era hacks, JavaScript utilities, and Sass mixins. It covers layout, animation, typography, color, and workflow enhancements like container queries, popover/dialog, :has, subgrid, scroll animations, and new color/logic functions. HN readers like having a single, up-to-date reference but note many features are only recently supported, debate Tailwind vs “real CSS,” and conclude teams should mix approaches pragmatically.

- Comment pulse  
  - Modern examples impress but many rely on 2022–2026 features with ~50% support, demanding fallbacks—counterpoint: filtering to “widely available” shows many are already practical.  
  - Several see Tailwind-style utilities as 2005 inline styling and a concern-mixing regression; others argue CSS’s cascade fails and colocated styles improve component maintenance.  
  - Ecosystem feels fragmented (Tailwind, CSS-in-JS, Sass, vanilla), yet many say choose what suits the team—and please stop filling viewports with fixed chrome.

- LLM perspective  
  - View: Treat this as a migration guide—swap individual hacks/JSlibs for standards one by one, not a wholesale rewrite.  
  - Impact: Stronger native CSS means smaller bundles, fewer dependencies, simpler theming; design systems teams gain the most.  
  - Watch next: IDE linters and devtools suggesting modern equivalents, plus benchmarks comparing JS-heavy versus CSS-native patterns for performance and a11y.
