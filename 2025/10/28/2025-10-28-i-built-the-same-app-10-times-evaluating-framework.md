# I built the same app 10 times: Evaluating frameworks for mobile performance

- Score: 227 | [HN](https://news.ycombinator.com/item?id=45729437) | Link: https://www.lorenstew.art/blog/10-kanban-boards/

### TL;DR

The author implemented the same database-backed kanban app in ten web frameworks to compare cold-load mobile performance and JavaScript size. In these controlled builds, Marko had the smallest board bundle, while SolidStart, SvelteKit, Qwik, and Nuxt achieved roughly 35–39 ms First Contentful Paint; Next.js measured 467 ms with a much larger bundle. The author recommends choosing among modern alternatives by architecture and team priorities. Results reflect minimal dependencies and one benchmark setup, so they do not establish universal production performance.

### Comment pulse

- Readers welcomed the mobile focus but questioned the article’s prose and whether bundle size dominated practical offline resilience.
- Practitioners favored Svelte or Vue developer experience, while others cited React ecosystem and hiring constraints.

### LLM perspective

- View: The study usefully exposes baseline costs, but framework choice still depends on workload and organizational constraints.
- Impact: Greenfield teams have measurable reasons to test alternatives instead of accepting React by default.
- Watch next: Independent reproductions, realistic production dependencies, offline behavior, and tail performance on slower devices.
