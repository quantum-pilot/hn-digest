# Does anybody like React?

- Score: 230 | [HN](https://news.ycombinator.com/item?id=48274077) | Link: https://jsx.lol

### TL;DR

The page is a deliberately cherry-picked archive of React criticism from 2023–2026, spanning client-side performance, hydration duplication, Server Components security, Next.js/Vercel lock-in, API complexity, accessibility, and adoption driven by hiring inertia rather than project fit. HN split between practical defenders and critics of the monoculture. Many credited React with improving on earlier JavaScript stacks, while others favored Vue, Svelte, HTMX, server rendering, or native web APIs. A deeper thread argued that the real unsolved problem is expressing visual, stateful interfaces naturally in code; every framework still carries awkward architectural compromises.

### Comment pulse

- Co-location wins supporters → one component can decide behavior and render markup together, avoiding controllers, templates, and scripts split across files.
- Popularity is not voluntary consensus → corporate standards, legacy code, vendor integrations, hiring pools, and résumé incentives constrain framework choice.
- Server-first advocates prioritize browser semantics → they accept scattered implementation to preserve native navigation — counterpoint: React users prefer component-local complexity despite runtime cost.

### LLM perspective

- **View:** React’s durability reflects a coordination equilibrium: predictability across teams can outweigh superior local ergonomics or performance.
- **Impact:** Architecture reviews should begin with interaction complexity, latency budgets, and maintenance ownership, then choose the smallest sufficient rendering model.
- **Watch next:** Server Components security remediation, real-world mobile benchmarks, and maintenance results from migrations to native DOM, Svelte, or LiveView.
