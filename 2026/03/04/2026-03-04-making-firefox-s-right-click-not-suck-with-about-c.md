# Making Firefox's right-click not suck with about:config

- Score: 233 | [HN](https://news.ycombinator.com/item?id=47251480) | Link: https://joshua.hu/firefox-making-right-click-not-suck

### TL;DR
The author shows how bloated Firefox’s macOS right‑click menu has become—26 items including AI, OCR, Lens, and dev tools—and walks through `about:config` flags to remove most of them (translations, screenshots, AI chat, link previews, OCR, autofill, print, etc.). Some stubborn items (e.g., “Bookmark Link…”, “Save Link As…”) require `userChrome.css`, to be covered later. They argue Firefox should offer a built‑in, toolbar‑style “Customize context menu” UI, instead of hiding this behind obscure settings.

---

### Comment pulse
- UI tradeoff: long menu helps power users and discoverability; short menu pleases minimalists → consensus: let users customize menus directly—counterpoint: author’s anger feels disproportionate.  
- AI and privacy: bundling AI actions and Google Lens by default feels disrespectful for a “privacy” browser → users wanted explicit opt‑in, not hidden `about:config` flags.  
- Old-school UI norms: ellipses and greyed-out items convey “more info needed” / “feature exists but unavailable” → some see author’s complaints as ignorance of long‑standing conventions.

---

### LLM perspective
- View: Firefox should expose a simple, supported “Edit context menu…” dialog rather than forcing users into `about:config` and `userChrome.css`.  
- Impact: Power users stay happier on Firefox; enterprises and privacy-conscious users can standardize cleaner, non-AI defaults.  
- Watch next: Whether Mozilla adds menu customization, ships saner defaults, or further integrates AI/partner features into prominent UI surfaces.
