# I Stored a Website in a Favicon

- Score: 288 | [HN](https://news.ycombinator.com/item?id=48606619) | Link: https://www.timwehrle.de/blog/i-stored-a-website-in-a-favicon/

### TL;DR

A playful storage experiment encodes a 208-byte HTML payload plus a four-byte length header directly into a PNG favicon’s RGB channels. Three bytes per pixel require 71 pixels, so a 9×9 image provides 239-byte capacity at 87% use. A JavaScript bootstrap draws the icon to canvas, reads its colors, decodes UTF-8, and replaces the page with recovered markup; the favicon therefore holds content, not a standalone site. HN readers proposed SVG embedding, PNG metadata, polyglot files, and favicon-cache tracking as related alternatives and risks.

### Comment pulse

- Pixel encoding was intentionally whimsical → the author rejected simpler SVG markup because the payload’s bytes should reside in actual color data.
- Single-file packaging is possible → commenters cited HTML/PNG polyglots, including variants also readable as ZIP or PDF, eliminating the separate bootstrap.
- Favicons carry privacy implications → cross-domain cache reuse has enabled supercookie-style fingerprinting, though commenters questioned whether browsers have since mitigated it.

### LLM perspective

- **View:** File roles are conventions; once readable through browser APIs, image bytes can become application data.
- **Impact:** The trick is educational for steganography and format design, but operationally inferior to explicit resources and stronger compression.
- **Watch next:** Test canvas security boundaries, favicon caching isolation, browser compatibility, and payload size after PNG or WebP compression.
