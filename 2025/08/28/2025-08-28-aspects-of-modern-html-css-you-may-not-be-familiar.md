# Aspects of modern HTML/CSS you may not be familiar with

- Score: 453 | [HN](https://news.ycombinator.com/item?id=45056878) | Link: https://lyra.horse/blog/2025/08/you-dont-need-js/

- TL;DR
    - A tour of modern HTML/CSS that replaces many common JS use‑cases: nesting, :has, range media queries, relative colors, @starting-style transitions, color-scheme/light-dark theming, details/summary, form validation, and responsive viewport units (lvh/svh/dvh). CSS animations run on the compositor, improving smoothness and battery. Baseline signals broad support; use progressive enhancement for persistence. HN debate: CSS feels accreted and brittle vs. “learn the cascade”; “no‑JS users” is niche, but using the platform to ship less code is a clear win.

- Comment pulse
    - CSS is fundamentally messy → decades of bolt‑ons, cascade fragility, flex/grid inconsistencies make debugging hard — counterpoint: well‑designed for documents if you understand the cascade.
    - “No‑JS users” aren’t a priority → better reason is fewer bytes and smoother TTI by using the platform; noscript support is a bonus.
    - Modern features reduce pain → nesting is official; :has, container/range queries help; parts of the wishlist exist (sibling-index, CSS mixins/functions) in Chrome.

- LLM perspective
    - View: Default to CSS-driven interactions; add minimal JS for state persistence, data fetching, or complex logic.
    - Impact: Smaller bundles, better battery and smoothness on mobile/low‑end devices, improved accessibility and resilience.
    - Watch next: Baseline rollouts for :has and dvh/svh/lvh, cross‑engine CSS mixins/functions and sibling-index, broader Web Animations API usage.
