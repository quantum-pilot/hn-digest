# Six Years Perfecting Maps on WatchOS

- Score: 117 | [HN](https://news.ycombinator.com/item?id=47990606) | Link: https://www.david-smith.org/blog/2026/04/29/maps-on-watchos/

### TL;DR
An indie developer spent six years turning the Apple Watch into a credible wrist-mounted hiking navigator inside Pedometer++. Early versions used server-rendered map images and clunky UIs, limited by tiny screens and slow hardware. He then built a custom SwiftUI map engine, commissioned a cartographer for legible light/dark topo tiles tuned for watchOS’s new Liquid Glass design, and collaborated with a designer to merge map and metrics in a single, layered layout. He rejected MapKit for finer control, offline use, and richer trail data.

---

### Comment pulse
- Apple’s lack of first‑party hiking/topo maps and GPX import on Apple Watch is a miss → even “Ultra” feels lifestyle-first, not expedition-ready.  
  — counterpoint: weak Apple apps leave room for higher-quality third‑party tools.

- The article resonates as a model of long-term craft → shows how breaking symmetry and platform conventions can produce better watch UIs.

- Technically, static/raster tiles suit constrained devices → simpler rendering, predictable performance; vector tiles and dynamic rendering strain watch hardware and APIs.

---

### LLM perspective
- View: This is a case study in patiently iterating UX under severe constraints until hardware, OS, and design all align.

- Impact: Power users gain a credible offline nav tool on their wrist; Apple gets quiet pressure to improve MapKit and first‑party fitness apps.

- Watch next: Measure battery/performance tradeoffs, offline coverage quality, and whether future watchOS exposes better map/vector APIs to third parties.
