# Play snake in the URL address bar

- Score: 239 | [HN](https://news.ycombinator.com/item?id=45408021) | Link: https://demian.ferrei.ro/snake/

- TL;DR
  - A JavaScript demo lets you play Snake entirely in the browser’s address bar by rapidly updating the URL with Unicode Braille blocks. It’s responsive and avoids history spam via history.replaceState; but some browsers rate-limit URL changes, forcing a fallback that can break the Back button. Rendering varies by font—some see uneven spacing—prompting suggestions to invert using a full ⣿ background. Related experiments include a favicon-based Snake. A clever, tiny canvas that doubles as an API and UX stress test.

- Comment pulse
  - replaceState avoids history spam → smooth back behavior — counterpoint: fallback for rate‑limited URL updates can nuke the back button.
  - Braille patterns animate the URL → some fonts render spaces unevenly; proposal: use full ⣿ background and carve snake/food as negative space.
  - Related hack → play Snake in the favicon; shows similar minimalist rendering in a tiny canvas.

- LLM perspective
  - View: URL bar as a render surface via Braille shows browser chrome can be co-opted for micro-UX.
  - Impact: Encourages treating URL/title/favicon as composable status channels; requires precise scheduling to avoid caps and history side-effects.
  - Watch next: Profile per-engine update budgets; try multiplexing URL+favicon; add font packs or invert-to-⣿ mode toggle.
