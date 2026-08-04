# Show HN: Kage – Shadow any website to a single binary for offline viewing

- Score: 597 | [HN](https://news.ycombinator.com/item?id=48529990) | Link: https://github.com/tamnd/kage

### TL;DR

Kage uses headless Chrome to render pages of a site, snapshot the settled DOM, remove scripts and event handlers, download assets, and rewrite links into an offline mirror. Its resumable, robots-aware crawler can package a whole site as a folder, deterministic ZIM archive, self-serving executable, or desktop app; ZIM remains compatible with Kiwix, while binaries add 13 MiB. HN saw value for offline company documentation and compared SingleFile’s stronger single-page capture. Questions focused on why static output needs HTTP serving, SPA fidelity, binary trust, and demand for a single-HTML option.

### Comment pulse

- Whole-site scope is the differentiator → Kage spiders linked pages and preserves navigation, whereas SingleFile primarily captures one page into portable HTML.

- Serving avoids browser restrictions → opening files directly can break relative navigation or trigger CORS and local-script policies — counterpoint: script-free mirrors should minimize dependencies.

- Preservation format affects trust and longevity → open ZIM archives are interoperable; self-executing viewers are convenient but platform-specific and harder to inspect.

### LLM perspective

- **View:** Rendering first and sanitizing afterward captures JavaScript-built pages while producing a static artifact with fewer runtime dependencies.

- **Impact:** Archivists, travelers, field teams, and schools can carry complete sites offline without trusting future hosting or network availability.

- **Watch next:** Test authenticated wikis, SPAs, lazy assets, incremental refresh accuracy, malicious-page isolation, search indexing, and large-site performance.
