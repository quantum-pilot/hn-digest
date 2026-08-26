# The Overcomplexity of the Shadcn Radio Button

- Score: 474 | [HN](https://news.ycombinator.com/item?id=46688971) | Link: https://paulmakeswebsites.com/writing/shadcn-radio-button/

### TL;DR

Updating a radio style led the author through Shadcn’s 45-line wrapper, Radix’s 215-line primitive, three imports, 30 Tailwind classes, a button re-labeled with ARIA, an SVG circle, and a conditionally rendered hidden native input. He argues a real radio input plus modern CSS can supply equivalent styling without JavaScript or extra dependencies, reducing cognitive load, bugs, and page weight. HN broadly shared the frustration but split on cause: React itself, its ecosystem, reluctance to learn CSS, designer demands, and organizational pressure for standardized stacks.

### Comment pulse

- Native baseline → appearance, pseudo-elements, checked state, and padded labels cover many radio designs; selects remain harder.
- Abstraction defense → React can wrap a native input cleanly — counterpoint: ecosystems make layered component stacks the default.
- Organizational drivers → custom designs, hiring standardization, deadlines, and large-team consistency encourage libraries even when individual controls become opaque.

### LLM perspective

- View: Component reuse is valuable only when its accessibility and styling benefits exceed the new semantic and runtime complexity.
- Impact: Small abstractions compound into bundle weight, debugging burden, dependency risk, and diminished knowledge of browser capabilities.
- Watch next: Inspect rendered semantics, keyboard behavior, mobile hit targets, JavaScript cost, and whether native CSS meets requirements.
