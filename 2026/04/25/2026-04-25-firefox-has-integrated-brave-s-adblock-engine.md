# Firefox Has Integrated Brave's Adblock Engine

- Score: 374 | [HN](https://news.ycombinator.com/item?id=47897891) | Link: https://itsfoss.com/news/firefox-ships-brave-adblock-engine/

### TL;DR

Firefox 149 includes Brave’s MPL-licensed `adblock-rust` library as a disabled prototype for richer content blocking, without bundled filter lists or a user interface. The Rust engine can process network blocking, cosmetic rules, and uBlock Origin-compatible syntax, but Mozilla says it is testing one open-source component to improve Enhanced Tracking Protection—not shipping Brave’s full blocker—and has no plan to abandon Manifest V2 extensions. HN reaction mixed cautious optimism about native, memory-safe filtering with fears it could eventually justify weakening add-ons; others considered that speculation premature.

### Comment pulse

- Firefox’s MV3 retains request blocking, so equating Manifest V3 universally with disabled ad blockers is technically inaccurate.
- Waterfox independently adopted the engine for full blocking, showing the library can support broader uses than Mozilla’s prototype.
- Cross-platform users want equivalent custom filtering on iOS — counterpoint: Apple’s WebKit requirement limits what browser vendors can control.

### LLM perspective

- Watch whether Mozilla exposes configurable lists, cosmetic filtering, telemetry, or only tracker-list processing.
- Any migration should preserve uBlock Origin capability, user control, and extension APIs before changing defaults.
- Benchmark rule compatibility, page breakage, memory, CPU, and update latency against current protection and extensions.
