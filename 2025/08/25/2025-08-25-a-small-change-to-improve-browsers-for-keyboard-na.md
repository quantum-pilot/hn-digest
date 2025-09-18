# A small change to improve browsers for keyboard navigation

- Score: 207 | [HN](https://news.ycombinator.com/item?id=45013737) | Link: https://b.43z.one/2025-07-22/

- TL;DR
  - The author proposes a tiny browser hack: after using quick find or Ctrl+F, pressing Enter should click the element under the current text selection—making buttons/divs keyboard-activatable, not just links. They ship a minimal extension that listens for Enter and clicks the selection’s parent node. HN replies highlight mature alternatives like Vimium/Vimium C/Tridactyl that already hint and click non-links, frustrations with broken keyboard scrolling on modern sites, and a built‑in workaround (Esc then Enter) that still behaves differently across browsers.

- Comment pulse
  - Keyboard extensions beat hacks → Vimium/Vimium C/Tridactyl hint-click any element, offer new-tab mappings, and work across sites.
  - Keyboard scrolling is unreliable → sticky headers, custom scroll areas, and JS hijacks break PageUp/Down; try focus-to-scroll extensions or disable JS — counterpoint: Firefox compensates.
  - Built-in workaround exists → Press Esc to close find, then Enter navigates; Chrome clicks links/buttons, Firefox mostly only links.

- LLM perspective
  - View: Minimal Enter-to-click improves flow, but selection→parentElement is brittle; may misclick nested nodes or non-interactive text.
  - Impact: Helps keyboard users on JS-heavy sites; nudges devs toward semantic buttons, roles, tabindex, and accessible activation via Enter/Space.
  - Watch next: Add heuristics: nearest clickable ancestor, role/button checks, focus ring, exclude contenteditable; test false-click rate versus Vimium/Tridactyl on top sites.
