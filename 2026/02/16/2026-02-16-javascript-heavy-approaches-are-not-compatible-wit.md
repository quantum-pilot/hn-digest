# JavaScript-heavy approaches are not compatible with long-term performance goals

- Score: 158 | [HN](https://news.ycombinator.com/item?id=47029339) | Link: https://sgom.es/posts/2026-02-13-js-heavy-approaches-are-not-compatible-with-long-term-performance-goals/

### TL;DR

A web-performance specialist argues that JavaScript-heavy applications, especially React projects, start with costly dependencies and accumulate regressions because the easiest development paths favor global state, static imports, rerenders, and monolithic bundles. Budgets, code splitting, linting, CI profiling, and real-user monitoring can slow deterioration but demand sustained organizational vigilance. For most sites, the author prefers server-rendered HTML with progressive enhancement, reserving client-heavy architectures for genuinely interactive destinations. Commenters largely accept React’s problems while disputing whether they condemn JavaScript or only particular frameworks and team practices.

### Comment pulse

- Large teams inevitably accumulate dependency and bundle debt → small individually acceptable changes compound beyond what one performance team can reverse.
- Server-first developers report durable speed and simpler debugging → forms, links, islands, and native transitions cover many application needs.
- SPAs remain justified for all-day interactive tools → counterpoint: React is not the only client framework, and alternatives use finer-grained reactivity.

### LLM perspective

- **View:** Architecture should make performance defaults enforceable; monitoring compensates for fragility but cannot remove incentive mismatches.
- **Impact:** Lower-end mobile users bear bandwidth, parsing, compilation, and execution costs hidden by developers' hardware.
- **Watch next:** React Compiler results, median-phone RUM, bundle-budget enforcement, and framework comparisons under sustained development.
