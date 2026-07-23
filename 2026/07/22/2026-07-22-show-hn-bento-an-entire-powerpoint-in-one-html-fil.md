# Show HN: Bento - An entire PowerPoint in one HTML file (edit+view+data+collab)

- Score: 609 | [HN](https://news.ycombinator.com/item?id=49008211) | Link: https://bento.page/slides/

### TL;DR
Bento is a self-contained presentation tool where a single HTML file is the slide deck, viewer, and editor, saving changes directly into itself. Internally it stores slide data as JSON and embeds the app as a compressed base64 blob, using browser APIs to rewrite the file and ECDSA to sign updates. A CRDT-based, end‑to‑end encrypted collab mode runs via Cloudflare Durable Objects. HN readers connect it to the broader “single-file web app” trend, while raising questions about performance, UX, trust, and versioning.

---

### Comment pulse
- Architecture is clever: JSON slide data + compressed app blob, local writeback, encrypted CRDT collab relay. — counterpoint: concerns about Cloudflare reliance, v1→v2 migration, long-term maintenance.  
- Many see Bento as part of a “single-file web app” wave, alongside TiddlyWiki, mdwiki, Polyglot-HTML-ZIP-PNG, suggesting similar approaches for SVG, spreadsheets, and micro‑apps.  
- Stress tests (guestbook) exposed freezes and focus resets; some dislike LLM-generated copy, but appreciate FOSS licensing and compare favorably to heavy office formats.

---

### LLM perspective
- View: This showcases how modern browser APIs enable rich, offline, self-contained tools without servers or installs.  
- Impact: Especially attractive for privacy-conscious teams, educators, and travelers needing portable decks independent of PowerPoint/Google Slides.  
- Watch next: Real-world scaling of CRDT collab, browser support for File System Access/DecompressionStream, and emerging conventions for signed, versioned single-file apps.
