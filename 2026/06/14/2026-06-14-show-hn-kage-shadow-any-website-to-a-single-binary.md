# Show HN: Kage – Shadow any website to a single binary for offline viewing

- Score: 597 | [HN](https://news.ycombinator.com/item?id=48529990) | Link: https://github.com/tamnd/kage

- TL;DR  
Kage is a Go-based tool that crawls and “shadows” an entire website by driving headless Chrome, snapshotting the rendered DOM, stripping all JavaScript, and localizing assets into static HTML you can browse offline. It can then pack the mirror into a ZIM archive, a self-contained executable, or a double-clickable app, optionally using native webviews. Hacker News discussion compares it to SingleFile and browser “Save As,” debates why a server is needed, and suggests single-file and Markdown-export modes.

- Comment pulse  
  - Offline docs/wikis use case → people want easy distribution, ideally a single HTML shim or Markdown+Git export; author is open to both.  
  - Comparisons to SingleFile/SingleFileZ and Save As → those excel at single pages; Kage targets whole-site mirroring and better SPA handling—counterpoint: some see them as simpler, sufficient solutions.  
  - Questioning “no tracking, no network calls” phrasing → plus confusion about needing kage serve; replies note file:// CORS/JS issues and that any static HTTP server will work.

- LLM perspective  
  - View: Neatly combines crawling, headless rendering, sanitization, and packaging into a practical “freeze this site exactly as seen” workflow.  
  - Impact: Helps archivists, developers, and companies preserve docs or essays in low-connectivity or high-trust environments without runtime third-party code.  
  - Watch next: Real-world tests on large SPAs, auth-gated sites, and feature parity with SingleFile; GUI/extension frontends would broaden adoption.
