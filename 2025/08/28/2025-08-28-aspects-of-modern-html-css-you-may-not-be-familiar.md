# Aspects of modern HTML/CSS you may not be familiar with

- Score: 453 | [HN](https://news.ycombinator.com/item?id=45056878) | Link: https://lyra.horse/blog/2025/08/you-dont-need-js/

- TL;DR
  - Modern CSS/HTML can now handle many interactions once delegated to JavaScript. The author demos animations and entry transitions (@starting-style), theming (color-scheme, light-dark()), validation (:user-valid/invalid), tabs/accordions (details/summary, :has + radios), and relative colors and nesting for maintainability. New viewport units (lvh/svh/dvh) fix mobile 100vh woes; CSS animations avoid main-thread jank; Baseline clarifies cross‑browser safety. Keep JS for persistence or complex logic via progressive enhancement. HN debates CSS’s design/cascade, the value of noscript users, and notes mixins/sibling-index specs emerging.

- Comment pulse
  - CSS is bolted-on, cascade makes large UIs fragile — counterpoint: Others say CSS is fit-for-purpose; issues come from shallow understanding of the cascade.
  - No‑JS users are niche; don’t optimize for them → Using platform features reduces code, bugs, and TTI; noscript compatibility becomes a free bonus.
  - Modern additions (:has, nesting, Flexbox) ease pain; wishlist items like mixins and sibling-index/count already exist in specs and Chrome.

- LLM perspective
  - View: Prefer declarative CSS for animation, theming, validation, and basic widgets; add minimal JS for persistence and complex state.
  - Impact: Less JS means smaller bundles, smoother rendering (compositor thread), better battery life, and fewer cross-framework integration issues.
  - Watch next: Baseline milestones for :has/nesting, mixins shipping, sibling-index adoption, mobile viewport unit edge cases, Web Animations API uptake.
