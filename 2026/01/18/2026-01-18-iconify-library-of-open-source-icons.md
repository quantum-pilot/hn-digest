# Iconify: Library of Open Source Icons

- Score: 488 | [HN](https://news.ycombinator.com/item?id=46665411) | Link: https://icon-sets.iconify.design/

### TL;DR
Iconify aggregates a huge collection of open‑source icon sets (material, UI, logos, emojis, flags, thematic, programming, etc.), exposing them via a unified catalog and API. Developers can query icons by name, style, and license, then fetch individual SVGs (e.g., directly embedding them in tools like D2 diagrams or web apps). HN comments highlight practical usage, search tools like icones.js.org, and deep concerns about icon optimization, layout shift, and tradeoffs between inlining, caching, and lazy loading.

---

### Comment pulse
- Iconify API usage → Simple URLs provide SVGs, making it easy to integrate icons into diagrams (D2) and apps without managing assets manually.  
- Icon selection and search → icones.js.org offers a better search UI; some animated icons exist, but discoverability and filtering for animation are limited.  
- Icon performance pitfalls → Poor icon handling causes layout shift; reserving space (width/height) is key—counterpoint: inlining hurts caching, so lazy loading/sprites may be preferable.

---

### LLM perspective
- View: Iconify effectively standardizes access to many icon ecosystems, reducing friction in prototyping, design systems, and documentation tools.  
- Impact: Frontend devs, technical writers, and infra diagrammers gain a consistent, license-aware icon source instead of scattered downloads and bespoke sprite sets.  
- Watch next: Tooling that auto-bundles Iconify SVGs with CLS-safe dimensions, deduplication, and license notices integrated into build pipelines.
