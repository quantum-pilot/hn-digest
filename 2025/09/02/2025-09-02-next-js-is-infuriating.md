# Next.js is infuriating

- Score: 1024 | [HN](https://news.ycombinator.com/item?id=45099922) | Link: https://blog.meca.sh/3lxoty3shjc2z

### TL;DR

The author argues Next.js makes ordinary request-scoped production logging needlessly difficult. Middleware runs in a separate runtime and async context from page rendering, cannot be freely chained, and exposes headers as the practical bridge for a request ID. A custom server still did not preserve the author's AsyncLocalStorage context through Next's handler. They contrast this with SvelteKit's composable hooks and `event.locals`, and criticize Next's documentation and issue response. The post is a detailed account of one team's debugging experience, not a comprehensive framework evaluation.

### Comment pulse

- Many developers echoed the complexity complaint; others said it reflects Next's edge, server, middleware, and browser execution domains.
- A Next.js representative pointed to stable Node middleware and OpenTelemetry, prompting objections that observability should not require heavier machinery.

### LLM perspective

- View: The real failure is an execution model whose boundaries surface only after familiar server patterns stop working.
- Impact: Hidden context transitions raise debugging costs and can lock teams into framework-specific observability paths.
- Watch next: Whether Node middleware, documentation, and request-local APIs converge into a simpler supported logging pattern.
