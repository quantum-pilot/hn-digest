# I built the same app 10 times: Evaluating frameworks for mobile performance

- Score: 227 | [HN](https://news.ycombinator.com/item?id=45729437) | Link: https://www.lorenstew.art/blog/10-kanban-boards/

- TL;DR
  - A developer rebuilt the same kanban app in 10 meta‑frameworks to test mobile performance. Next‑gen stacks (Marko, SolidStart, SvelteKit, Qwik) and Nuxt all feel “instant” (~35–39ms FCP); bundle size is the real differentiator. Marko leads (28.8 kB compressed board page) versus Next.js (176.3 kB) and Analog/Angular (203.4 kB). React’s baseline cost persists: TanStack Start (React) ~118.2 kB compressed; swapping to Solid halves size under the same router. MPA models (Marko/HTMX) stay lean per route. HN praise mobile focus/Svelte/Vue DX; critiques target rhetoric and note offline/SDK realities.

- Comment pulse
  - Mobile-first matters → SPAs struggle on P75–P90 devices; devs fight frameworks for performance—counterpoint: offline-first/caching can outweigh raw bundle differences.
  - Svelte and Nuxt praised → simpler DX and patterns; perceived better trajectory and agentic coding fit; some still pick Next.js for vendor SDK support.
  - Writing tone criticized → “ChatGPT-slop” and “technofeudalism” rhetoric undermines credibility for some readers.

- LLM perspective
  - View: Compare architectures, not micro-FCP; bytes and hydration model dominate mobile reality.
  - Impact: React web’s baseline persists; expect pressure toward compile-first and selective hydration/resumability.
  - Watch next: Vue Vapor Mode maturity, Marko 6 GA, CrUX trends shifting; broader SaaS SDK support beyond React.
