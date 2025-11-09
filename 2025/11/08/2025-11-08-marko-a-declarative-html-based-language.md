# Marko – A declarative, HTML‑based language

- Score: 231 | [HN](https://news.ycombinator.com/item?id=45858905) | Link: https://markojs.com/

- TL;DR
  - Marko is an HTML‑first, compiled UI language: extend HTML with reactive tags, target server and browser separately, and ship minimal client JS via fine‑grained bundling; TypeScript is built‑in. HN reactions split: detractors prefer “just JavaScript” React/JSX, while others argue React isn’t “just JS” anymore and praise Marko’s compile‑time optimizations and performance. A cautionary thread recalls XML‑template systems getting unwieldy on complex apps. Context: eBay uses Marko; SolidJS’s author previously collaborated; there’s a Marko 6 HN clone.

- Comment pulse
  - React/JSX familiarity beats HTML‑DSLs → Editors/TypeScript understand JSX; custom tags (<let>, <for>) feel foreign — counterpoint: JSX isn’t JS either, and React’s DSL complexity grows.
  - Marko ships minimal JS and streams early → fine‑grained bundling and SSR streaming boost perf; React’s RSC/SSR era ballooned bundles and lock‑in.
  - Template languages can get unwieldy at scale → prior XML/XHTML systems worked for simple sites but turned ugly with complex logic.

- LLM perspective
  - View: HTML‑first with server‑streaming and sub‑template bundling addresses hydration cost better than islands or heavy RSC stacks.
  - Impact: Best fit for content‑heavy, latency‑sensitive apps; teams burned by React/Next complexity regain control over bundles and routing.
  - Watch next: Independent JS‑shipped metrics, DX reports with TypeScript tooling, adapter ecosystem maturity, and migration guides from React/Vue to Marko 6.
