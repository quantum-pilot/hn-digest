# How I use HTMX with Go

- Score: 302 | [HN](https://news.ycombinator.com/item?id=48912175) | Link: https://www.alexedwards.net/blog/how-i-use-htmx-with-go

### TL;DR
The article is a hands-on walkthrough of building a Go web app that uses HTMX for “HTML over the wire” interactivity. It standardizes on embedded templates (base/pages/partials), a reusable `htmlRenderer` to serve either full pages or partials, and helpers that detect `HX-Request` to choose the right response, set `Vary` correctly, and handle redirects and errors via HTMX headers. The author also shows careful HTMX config (history, caching, error swapping) and patterns for multiple layouts. HN discussion centers on stacks, team adoption, and HTMX’s limits vs SPAs.

### Comment pulse
- Go + HTMX fans propose full stacks (e.g., GUS, GoTH) with templ/sqlc/sqlite/goose/etc. → strong tooling makes type-safe, binary-only deployments pleasant.  
- Teams often resist HTMX and html/template’s quirks → skeptics prefer React/Blazor; others suggest templ/gsx or different template patterns to avoid cloning templates.  
- HTMX praised for CRUD/admin apps, less so for complex shared-state UIs → some migrate to SvelteKit SPAs instead — counterpoint: HTMX philosophy questions needing that complexity.

### LLM perspective
- View: HTMX + Go is an efficient “default” for small–medium apps needing interactivity without full SPA complexity.  
- Impact: Shared helpers for templates, redirects, and HTMX headers can become reusable internal libraries, reducing mistakes and bikeshedding.  
- Watch next: Higher-level Go frameworks that bake in these HTMX patterns, plus real-world comparisons vs React/Svelte on maintenance and bugs.
