# Phoenix LiveView 1.2

- Score: 200 | [HN](https://news.ycombinator.com/item?id=48524293) | Link: https://phoenixframework.org/blog/phoenix-liveview-1-2-released

### TL;DR

Phoenix LiveView 1.2 adds CSS colocated inside HEEx components, extracted at compile time into the normal bundler pipeline. The compiler now marks template boundaries so scoped styles can avoid leaking into caller slots, although automatic CSS @scope output is withheld because browser support remains incomplete; developers can opt into root attributes and implement a scoping behavior. A tokenizer/parser refactor also simplifies macro components and formatting. HN welcomed the server-driven, low-JavaScript model and reported strong LLM productivity, while cautioning that static pages or richer client frameworks may better fit workload extremes.

### Comment pulse

- Server-driven interactivity reduces moving parts → users praised backend-centric SPAs as maintainable for moderate complexity — counterpoint: mostly static sites may need no SPA.
- Elixir appears agent-friendly → compilation, functional style, concise code, generators, and static analysis provide rapid feedback and conserve context.
- Colocation meets existing demand → former Surface UI users had already found component-level CSS effective and welcomed its move into LiveView.

### LLM perspective

- **View:** LiveView is converging on component locality without abandoning server ownership, but browser standards still constrain framework ergonomics.
- **Impact:** Teams gain fewer cross-file styling jumps and better agent feedback; scoping choices remain explicit migration and compatibility work.
- **Watch next:** Track CSS Scope browser coverage, official default scoping, selector overhead, slot isolation, bundler behavior, and HEEx formatter regressions.
