# Building an HTML-first site doubled our users overnight

- Score: 1273 | [HN](https://news.ycombinator.com/item?id=48475483) | Link: https://mohkohn.co.uk/writing/html-first/

### TL;DR
A contractor rescued a failing online application for a regulated utility by replacing a broken React SPA with an HTML‑first, Astro-based, progressively enhanced form wizard. Each step posted to the server, saving data and uploads by session ID so users never lost progress, while a tiny web component layered on accessible client-side validation over native HTML. Form completions doubled overnight—exposing how JS analytics had hidden no‑JS users. HN comments connect this to SPA monoculture, “boring” stacks like HTMX+Go, and long-standing GOV.UK practices.

---

### Comment pulse
- SPA-first culture → Many devs only know React-style SPAs; server-rendered HTML and non-JS forms feel like “extra work” due to unfamiliarity.
- Simpler stacks work → HTMX+Go+SQLite handle serious traffic cheaply and cleanly—counterpoint: rich UI without frameworks can mean more custom coding and slower delivery.
- Governments lead by example → GOV.UK/MOJ have long used resilient, multi-page HTML wizards and shared libraries, proving large-scale accessible forms are practical.

---

### LLM perspective
- View: Treat HTML-first as a conversion and compliance strategy, not nostalgia; measure wins in completion rates and reduced support load.
- Impact: Product, not just engineering, should own requirements for offline-tolerant, assistive-tech-friendly flows, especially in regulated or public services.
- Watch next: Compare outcomes of Triptych/HTMX/Remix-style form flows in A/B tests, including JS-disabled scenarios and low-end device performance.
