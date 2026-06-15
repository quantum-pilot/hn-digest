# Your ePub Is fine

- Score: 717 | [HN](https://news.ycombinator.com/item?id=48533848) | Link: https://andreklein.net/your-epub-is-fine-kobo-disagrees-blame-adobe/

### TL;DR
An ebook author found a fully standards-compliant EPUB—passing epubcheck and working on Kindle, Apple Books, and others—was flagged as “corrupted” on Kobo. Root cause: Kobo routes standard EPUBs through Adobe’s ancient RMSDK engine, whose CSS parser silently chokes on valid modern CSS (here, `max-width: min(150px, 30vw)`), offering no error and just dropping the book. Kobo actually ships a newer WebKit-based renderer but only uses it for its proprietary KEPUB format, illustrating how DRM-driven, stagnant implementations sabotage the open EPUB ecosystem.

---

### Comment pulse
- Adobe’s pattern: fragile platforms, weak QA, poor support → Flash’s fall and RMSDK’s stagnation continue this history of unreliability and user-hostility.  
- RMSDK access is effectively closed; combined with publisher dependence on Adobe DRM, this looks like anticompetitive lock-in blocking independent ereader innovation.  
- Pragmatists: target EPUB 2/3.1 and avoid modern CSS; convert to KEPUB to trigger Kobo’s better renderer — counterpoint: entrenches fragmentation and proprietary quirks.

---

### LLM perspective
- View: Standards plus validators are insufficient when dominant runtimes lag; publishers need explicit “minimum runtime” targets like browser support matrices.  
- Impact: Locked-down renderers with DRM incentives concentrate power in a few vendors, constraining typography, accessibility, and experimental publishing formats.  
- Watch next: Useful follow-up: a public EPUB compatibility matrix, automated ADE/RMSDK regression tests, and tools that auto-flag CSS unsupported on common devices.
