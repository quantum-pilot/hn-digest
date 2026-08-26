# Iconify: Library of Open Source Icons

- Score: 488 | [HN](https://news.ycombinator.com/item?id=46665411) | Link: https://icon-sets.iconify.design/

### TL;DR

This captured Iconify directory snapshot catalogs 204 open-source icon sets across Material, multiple UI grids, programming, logos, emoji, maps, thematic collections, and an archive. Each listing exposes its license and icon count, with filters for category, tag, grid, palette, and maintenance status; collection sizes range from dozens to nearly 19,000 icons. HN readers emphasized practical consumption through SVG APIs and search tools, while discussing animated sets and the performance trade-offs among inline SVG, caching, lazy loading, and reserving dimensions to prevent layout shift.

### Comment pulse

- SVG endpoints integrate cleanly with diagram tools → commenters used Iconify URLs directly inside D2 architecture diagrams.
- Discovery extends beyond static icons → searchable animated sets supported polished offline-editor interfaces.
- Delivery strategy affects performance → inline SVG prevents requests but grows DOMs and sacrifices caching; fixed dimensions address layout shift.

### LLM perspective

- View: The directory’s value is normalized discovery across many licenses and design systems, not a single visual style.
- Impact: Developers can prototype interfaces faster, but must still audit licenses, consistency, accessibility, and bundle behavior.
- Watch next: Recheck collection counts over time and benchmark inline, cached, and lazy-loaded SVGs under realistic repetition.
