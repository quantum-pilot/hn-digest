# Play snake in the URL address bar

- Score: 239 | [HN](https://news.ycombinator.com/item?id=45408021) | Link: https://demian.ferrei.ro/snake/

### TL;DR

URL Snake turns the browser's address bar into a tiny Snake display controlled by arrow keys or WASD, using changing Braille-pattern characters in the URL while the page hosts controls and scorekeeping. The source provides little implementation explanation, so discussion supplies the technical observations: users found it responsive, noticed careful history handling, compared a favicon-based version, and proposed denser Braille rendering to avoid uneven whitespace glyphs. Browser rate limits may require a fallback that harms back-button behavior.

### Comment pulse

- Users praised the responsive novelty and, in supported browsers, returning to Hacker News without polluted history.
- Braille's 256 possible 4×2 patterns were suggested for uniform spacing and a negative-space rendering alternative.

### LLM perspective

- View: The project succeeds by treating browser chrome as a constrained creative display surface.
- Impact: URL mutation enables playful interfaces, but browser compatibility and navigation semantics limit reliability.
- Watch next: Cross-browser behavior under URL-update throttling and whether rendering remains legible across fonts.
