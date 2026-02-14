# CSS-Doodle

- Score: 112 | [HN](https://news.ycombinator.com/item?id=47000164) | Link: https://css-doodle.com/

### TL;DR
CSS-Doodle is a custom element (`<css-doodle>`) that turns a block of CSS‑flavored rules into generative art: it auto-builds a grid of divs, then lets you style each cell using extended selectors (`@row`, `@random`, `@match`), functions (`@rand`, `@pick`, `@shape`, `@svg`, `@shaders`), and a reproducible random `seed`. It’s essentially a declarative drawing DSL layered on top of CSS and the DOM, aimed at patterns, animations, and teaching/playing with procedural graphics in the browser.

---

### Comment pulse
- Project context → Author also wrote a behind‑the‑scenes intro; people appreciate the design and history being documented.
- Generative wow factor → Commenters are surprised how a few lines of rules yield rich, randomizable patterns—aliases and utilities hide a lot of complexity.
- CSS vs JS debate → Some see this as a declarative JS graphics framework with CSS syntax; others argue a canvas API might suit complex visuals better — counterpoint: DOM/CSS keeps layout, accessibility, and composability.

---

### LLM perspective
- View: This is a domain-specific language for generative art that piggybacks on CSS, offering power without imperative code.
- Impact: Useful for artists, educators, and front-end devs to prototype visuals, teach math/patterns, or add lightweight decoration.
- Watch next: Benchmarks on large grids, tooling support (linting, autocomplete), and integrations with design systems or creative coding platforms.
