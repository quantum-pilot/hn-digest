# This website has no class

- Score: 204 | [HN](https://news.ycombinator.com/item?id=45287155) | Link: https://aaadaaam.com/notes/no-class/

- TL;DR
  - An experiment in building a classless site: Adam Stoddard removed CSS classes, leaned on semantic elements, contextual selectors, and then custom tags/attributes (no JS) to model components and variants. Modern CSS (layers, nesting, :has) helped; overuse of structural selectors proved brittle, so custom elements/attributes became the primary mechanism. Results: ~5KB CSS and better accessibility; trade-offs: higher authoring discipline, tighter coupling to structure, poor fit for bigger teams. HN largely prefers middle-ground or classes; some praise semantics; others cite performance and flexibility concerns.

- Comment pulse
  - Structure-bound styling is brittle → markup changes force CSS edits; classes offer flexibility and faster matching — counterpoint: acceptable for static blogs with stable patterns.
  - Prefer semantic elements over div soup → built-in tags convey meaning, enable useful defaults, and improve accessibility.
  - Middle ground and ergonomics → go classless by default, then add scoped classes as exceptions; Tailwind polarizes on velocity versus complexity and variant management.

- LLM perspective
  - View: Classless plus custom tags/attributes is a disciplined pattern for content sites; risky coupling for dynamic, multi-author apps.
  - Impact: Smaller CSS bundles, stricter semantics, but higher authoring cost and harder refactors when structures evolve.
  - Watch next: Benchmarks on attribute selectors, tools that lint semantic-first patterns, and documented hybrid recipes for exceptions and variants.
