# The Anatomy of a macOS App

- Score: 171 | [HN](https://news.ycombinator.com/item?id=46181268) | Link: https://eclecticlight.co/2025/12/04/the-anatomy-of-a-macos-app/

### TL;DR
The article traces how Mac software evolved from classic Mac OS “resource forks” to today’s self-contained `.app` bundles. Modern macOS apps are directory hierarchies combining Mach-O executables, resources, frameworks, and metadata such as `Info.plist`, plus optional items like XPC services and plug‑ins. Since Leopard, code signing, Gatekeeper, App Store receipts, and stapled notarization tickets have layered security on top, while still using one bundle format for both Intel and Apple Silicon via universal (“fat”) binaries.

---

### Comment pulse
- Notarization feels de facto mandatory → non-notarized apps trigger scary dialogs, require deep Settings changes, and demand $99/year and invasive identity checks — counterpoint: some users still run many non-notarized apps.
- Compared to Windows → Apple’s process is seen as cheaper and less painful than Windows code-signing, which can cost >$1k and impose hardware-token bottlenecks.
- Bundle structure flexibility → macOS technically allows nonstandard layouts if RPATHs are correct, but iOS and App Store rules are far stricter and poorly documented.

---

### LLM perspective
- View: macOS bundles show how UX, security, and historical compatibility can coexist in a single packaging model.
- Impact: Indie developers bear disproportionate notarization and identity burdens compared to large vendors with legal and ops support.
- Watch next: Tighter Gatekeeper rules, notarization telemetry, and possible alternative distribution channels will shape macOS app viability outside the App Store.
