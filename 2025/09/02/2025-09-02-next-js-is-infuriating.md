# Next.js is infuriating

- Score: 1024 | [HN](https://news.ycombinator.com/item?id=45099922) | Link: https://blog.meca.sh/3lxoty3shjc2z

- TL;DR
  - An engineer tries to add request-scoped logging to a Next.js app and hits walls: Middleware defaults to edge (logs in browser), Node runtime inconsistencies, AsyncLocalStorage context doesn’t reach pages/layouts, and the only reliable handoff is stuffing a requestId into headers; custom servers don’t help. They compare SvelteKit’s hooks/locals and lament Next’s docs and issue tracker. HN largely agrees: Next’s abstractions push Vercel-centric patterns; use simpler stacks or the Pages router. A Next.js maintainer acknowledges DX issues, touts Node middleware in 15.5 and OpenTelemetry; many call OTel overkill.

- Comment pulse
  - Next.js fits niche cases (global B2C, edge); otherwise simpler stacks beat complexity → Vercel incentives drive design — counterpoint: Pages router users report fewer problems.
  - Logging/instrumentation should be simple; OTel is heavy → relying on instrumentation.ts adds complexity and experimental tooling.
  - Batteries-included megaframeworks over-abstract; buffet-style stacks (Vite SPA, Rails SSR, Inertia) stay flexible → some cite Laravel/Angular as productive counterexamples.

- LLM perspective
  - View: Treat Middleware as routing-only; create request context in route handlers using AsyncLocalStorage under Node runtime.
  - Impact: Teams doing non-edge SSR or SPAs can drop Next’s App Router features, reduce cognitive load, and gain predictable logging.
  - Watch next: Next 15.5+ middleware Node stability, middleware chaining, and clearer execution docs; compare SvelteKit locals and Inertia for simpler mental models.
