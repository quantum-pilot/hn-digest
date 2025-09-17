# React is winning by default and slowing innovation

- Score: 449 | [HN](https://news.ycombinator.com/item?id=45252715) | Link: https://www.lorenstew.art/blog/react-won-by-default/

- TL;DR
    - The author argues React now “wins by default,” creating an innovation ceiling: VDOM overhead, hooks pitfalls, and RSC/Compiler workarounds reflect model constraints. Alternatives—Svelte (compile-time), Solid (fine-grained signals), Qwik (resumability)—often deliver faster startup/updates with lower cognitive load but get sidelined by network effects, hiring, and inertia. Proposed fix: choose by constraints with small pilots, not habit, to diversify skills and push the platform forward. HN debates ergonomics, stability, interop via Web Components, and React’s fit for simple sites.

- Comment pulse
    - React wins on “just JavaScript” ergonomics, ecosystem, and React Native reach — counterpoint: hooks, RSC, compilers erode the “just JS” simplicity.
    - React scales poorly for small sites: compile step, tooling, no CDN-first path; Vue/Alpine feel more progressive and lightweight.
    - Web Components pitched as interop escape hatch; skeptics cite weak typing, DX tradeoffs, and desire to avoid React-wrapped components.

- LLM perspective
    - View: Treat React as baseline, not default; run pilot spikes against Svelte, Solid, Qwik using production user flows and constraints.
    - Impact: Shifts evaluation to measurable KPIs: TTI, interaction latency, hydration cost, memory, bundle size, dev cognitive load, upgrade churn.
    - Watch next: React Compiler stability, RSC maturity, signals proposals in standards, large-scale resumability case studies, and web-component design systems replacing framework-locked libraries.
