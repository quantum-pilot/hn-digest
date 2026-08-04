# Your ePub Is fine

- Score: 717 | [HN](https://news.ycombinator.com/item?id=48533848) | Link: https://andreklein.net/your-epub-is-fine-kobo-disagrees-blame-adobe/

### TL;DR

An EPUB that passed EPUBCheck 3.3 and opened in Kindle, Apple Books, and Thorium appeared corrupted on Kobo because its Adobe RMSDK renderer silently rejected valid modern CSS: `max-width: min(150px, 30vw)`. Replacing it with a fixed width restored compatibility. Kobo also has a maintained WebKit renderer, but invokes it only for files named `.kepub.epub`, making conversion or renaming another workaround. HN criticized Adobe’s opaque, DRM-driven legacy stack, while some argued EPUB’s browser-derived living standards exceed what slowly updated embedded readers can realistically support.

### Comment pulse

- Validation proves conformance, not compatibility → EPUBCheck cannot predict undocumented parser crashes, so publishers still need device and renderer matrices.
- KEPUB sidesteps the legacy path → kepubify, Calibre, or the double extension select Kobo’s newer renderer and restore features such as cross-page highlighting.
- Standards scope is contested → modern CSS is valid — counterpoint: embedded readers are not evergreen browsers, and EPUB’s living dependencies can break old books.

### LLM perspective

- **View:** The failure is layered: permissive specifications, incomplete validation, frozen implementations, silent error handling, and extension-based renderer selection compound.
- **Impact:** Independent publishers absorb compatibility testing and support costs that proprietary DRM vendors and device makers externalize.
- **Watch next:** Build ADE, Kobo, Kindle, and WebKit render tests; track renderer retirement, EPUB profiles, CSS baselines, and actionable diagnostics.
