# How functional programming shaped and twisted front end development

- Score: 116 | [HN](https://news.ycombinator.com/item?id=45473019) | Link: https://alfy.blog/2025/10/04/how-functional-programming-shaped-modern-frontend.html

- TL;DR
    - The essay argues FP-flavored habits pushed frontend to fight the platform: CSS-in-JS/Tailwind avoid cascade, synthetic events abstract the DOM, CSR/hydration duplicate work, and libraries reimplement dialogs/forms/routing—costing performance, a11y, and simplicity. It urges rediscovering HTML/CSS/DOM and frameworks that enhance, not replace, the web (HTMX, Qwik, Astro, Remix, SvelteKit). HN pushes back on strawmen and timelines (browser normalization and late support for dialog/select), while others agree organizational incentives and fading CSS fluency drove overreliance on JS; several dispute React’s “functional” label.

- Comment pulse
    - Strawman critique → React’s synthetic events solved browser quirks; <dialog>/custom selects only recently viable; reads like HTMX promo — counterpoint: momentum still entrenches bad defaults.
    - React isn’t functional → Hooks are stateful, side‑effectful, and hard to unit test; composition resembles mixins more than FP pipelines.
    - Org constraints drive CSS → Tailwind enforces consistency; devs lack CSS depth; some tout CSS Modules/SCSS — counterpoint: enforcement is weak and features stabilized recently.

- LLM perspective
    - View: Prefer platform primitives; use JS to progressively enhance gaps; avoid hydration when links/forms work natively.
    - Impact: Simpler stacks, smaller bundles, better a11y; teams must relearn HTML/CSS/events and audit libraries that shadow native features.
    - Watch next: Baseline labels, popover/<dialog>/customizable select maturity; resumability benchmarks versus hydration; router/form APIs that default to progressive enhancement.
