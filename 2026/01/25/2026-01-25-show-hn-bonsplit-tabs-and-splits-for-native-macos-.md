# Show HN: Bonsplit – Tabs and splits for native macOS apps

- Score: 189 | [HN](https://news.ycombinator.com/item?id=46753301) | Link: https://bonsplit.alasdairmonk.com

### TL;DR
Bonsplit is a Swift package that gives macOS apps a modern, high‑performance tab bar with split panes, focusing on SwiftUI but usable with native code. It supports drag‑and‑drop tab reordering, horizontal/vertical splits, keyboard focus navigation, and fine‑grained configuration of behavior, appearance, and lifecycle. HN discussion centers on why this is needed when AppKit has native tabbing, concluding that Apple’s window‑level tab API is too rigid for many real apps, so custom, document‑agnostic tabs are often preferable.

---

### Comment pulse
- Native macOS tabbing is limited → works at the window/document level and is hard to adapt to richer tab models; many serious apps roll their own tabs.  
- High production value for “just a library” → people praise the beautiful docs and UI as raising the bar for dev tools — counterpoint: some question the time investment.  
- Users value interaction quality → drag‑and‑drop and tiling/tabbed splits are hard to implement well; this recalls beloved tiling WMs like ion3/notion.  

---

### LLM perspective
- View: This fills a practical gap between Apple’s basic tabbing and the sophisticated layouts modern developer/design tools need.  
- Impact: Indie and small teams can ship polished IDE‑style layouts without investing months in custom AppKit/SwiftUI plumbing.  
- Watch next: Real‑world adoption, performance under heavy tab counts, and patterns for integrating app state with Bonsplit’s controller and delegate.
