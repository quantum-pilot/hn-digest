# How I use HTMX with Go

- Score: 302 | [HN](https://news.ycombinator.com/item?id=48912175) | Link: https://www.alexedwards.net/blog/how-i-use-htmx-with-go

### TL;DR

Alex Edwards presents a Go-first HTMX pattern for adding app-like interactions while retaining server-rendered, escaped HTML. Assets and templates are embedded in one binary; a renderer clones shared base/partial templates and executes either full pages or fragments. Handlers inspect `HX-Request`, set `Vary`, preserve history behavior, use `HX-Redirect` with non-HTMX fallbacks, and configure visible error swaps, timeouts, no local history cache, and explicit attributes. HN users praised deployment simplicity and reduced JavaScript, but debated `html/template` ergonomics, team acceptance, and HTMX’s limits once interfaces require interconnected client state.

### Comment pulse

- Minimal-stack enthusiasm ran high → commenters paired Go and HTMX with SQLite, templ, sqlc, Hyperscript, or Alpine for type safety and local interactions.
- Team fit can outweigh technical merit → unfamiliar request/HTML flows attracted blame and resistance — counterpoint: entrenched SPA stacks accumulate their own scaling costs.
- HTMX suits server-shaped CRUD → larger shared-state interfaces became hard to coordinate — counterpoint: supporters question whether many applications genuinely need that client complexity.

### LLM perspective

- **View:** HTMX makes HTTP-delivered HTML fragments the composition unit; success depends on aligning product behavior with that model.
- **Impact:** Backend teams can own more UI and ship one artifact, while browser-state complexity becomes an explicit architectural threshold.
- **Watch next:** Cache/history edge cases, localization-friendly templates, accessibility, onboarding, and criteria for switching to client components.
