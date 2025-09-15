# Nicu's test website made with SVG (2007)

- Score: 134 | [HN](https://news.ycombinator.com/item?id=45240391) | Link: https://svg.nicubunu.ro/

- TL;DR
  - Nicu’s 2007 Inkscape-built site tested whether Google indexed SVG text and followed links, seeding a unique token to verify. Today, commenters confirm Google does index SVG text (sometimes surfacing in image results, sometimes normal), and share where SVG shines: crisp charts and UI icons, CSS styling, smaller files, dark mode. Caveats: font and sizing headaches, RSS/reader quirks if not self-contained, accessibility inconsistencies, and performance issues with thousands of SVG elements—canvas may be better. Also: optimize path precision; inline sprites reduce requests.

- Comment pulse
  - SVG charts/UI look sharp and searchable → CSS theming, selectable text, smaller files; font management and sizing coupling are fiddly — counterpoint: users don’t notice.
  - Indexing: text works; links unclear → test token surfaces; HTML-wrapped SVG may rank better; also test <desc> metadata and JS-generated SVG.
  - Implementation caveats → make SVG self-contained for RSS/reader views, optimize path precision (SVGOMG), watch accessibility; for thousands of elements, prefer canvas for performance.

- LLM perspective
  - View: SVG-as-document is viable; prioritize semantics (<title>, <desc>, ARIA), fallback text, and standalone files over fragile inline styling.
  - Impact: Blogs, data viz, and icon systems gain crispness and theming; complex scenes should combine SVG UI with canvas/WebGL drawing.
  - Watch next: Google/Bing indexing rules for SVG, screen-reader support parity, and perf guidance past 1–5k nodes across browsers.
