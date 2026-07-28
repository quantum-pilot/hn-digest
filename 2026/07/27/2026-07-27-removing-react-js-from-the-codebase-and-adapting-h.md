# Removing React.js from the codebase and adapting Htmx for UI interactivity (2023)

- Score: 214 | [HN](https://news.ycombinator.com/item?id=49067301) | Link: https://misago-project.org/t/removing-reactjs-from-the-codebase-and-adapting-htmx-for-ui-interactivity/1267/

### TL;DR
Misago, a Django-based forum engine, is removing its React front end and returning to classic server-rendered pages, adding HTMX “islands” only where interactivity is needed. The previous hybrid duplicated templates, APIs, and translations, confused customizers and plugin authors, and shipped large JS bundles. HTMX lets Misago send focused HTML fragments instead of JSON, cutting JavaScript size and stack complexity, with a gradual migration that temporarily reintroduces full-page reloads. HN debate centers on where HTMX shines versus when SPAs or lighter JS tools are preferable.

---

### Comment pulse
- HTMX can lag with large HTML responses → some switch to Alpine Ajax or finer-grained partials. — counterpoint: others say hx-targeting avoids re-rendering form markup.  
- Forums and form-centric apps are seen as ideal for HTMX → server-rendered HTML plus a few JS widgets matches user needs without SPA complexity.  
- Skeptics warn HTMX apps still accumulate custom JS → you risk recreating 2000s-era PHP+AJAX tangles; some suggest Liveview-style tools like PyView instead.  

---

### LLM perspective
- View: Misago exemplifies a broader swing back to server rendering plus small JS, especially for content-heavy, plugin-extended systems.  
- Impact: Theming, extensions, and translations become simpler; fewer duplicated stacks lowers contributor barrier and improves performance on low-end mobile devices.  
- Watch next: empirical UX benchmarks comparing HTMX, Alpine, and SPA stacks for forums, plus better patterns for offline-capable HTMX-based PWAs.
