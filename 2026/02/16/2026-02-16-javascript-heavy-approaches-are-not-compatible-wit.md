# JavaScript-heavy approaches are not compatible with long-term performance goals

- Score: 158 | [HN](https://news.ycombinator.com/item?id=47029339) | Link: https://sgom.es/posts/2026-02-13-js-heavy-approaches-are-not-compatible-with-long-term-performance-goals/

### TL;DR
JS-heavy “modern” stacks, especially large React SPAs, tend to start slow and reliably get slower: dependencies bloat, frameworks make the slow path easiest, and performance regressions are easy to reintroduce and hard to debug. Keeping them fast long-term needs heavy process (budgets, CI perf tests, RUM, lint rules) and often a dedicated perf team. The author argues many products would be better as server-centric, HTML-first MPAs with light JS “sprinkles,” reserving full client-side apps for truly interaction-heavy use cases.

---

### Comment pulse
- Problem is React and ecosystem churn, not JavaScript itself → newer frameworks (Svelte, Vue, Qwik) plus low-end devices expose React’s heaviness.  
- Server-rendered, progressive-enhancement apps work great in practice → simpler debugging, fewer regressions, clients still perceive UX as modern — counterpoint: data-heavy internal tools benefit from SPA-style navigation.  
- At scale, SPA bundles inevitably bloat → tiny per-PR increases and accidental imports defeat code-splitting; perf teams can’t keep up with many feature teams.

---

### LLM perspective
- View: Treat JS as a scarce client resource; default to HTML/SSR, escalate to SPA only when interaction demands it.  
- Impact: Product managers and tech leads must factor device diversity and perf budgets into framework and architecture choices.  
- Watch next: Tooling that enforces bundle/perf budgets by default and frameworks that minimize hydration or avoid it entirely.
