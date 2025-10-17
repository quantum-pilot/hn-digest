# Tor browser removing various Firefox AI features

- Score: 324 | [HN](https://news.ycombinator.com/item?id=45605842) | Link: https://blog.torproject.org/new-alpha-release-tor-browser-150a4/

- TL;DR
  - Tor Browser 15.0a4 strips Firefox’s new AI integrations (e.g., chatbot sidebar), citing un‑auditable privacy/security risks and avoiding implied endorsement. The alpha also renames meek‑azure to meek, shifts WebAssembly controls to NoScript to fix PDF issues, stops hiding URL protocols on desktop, and updates fonts and UI. HN reaction: privacy‑minded users applaud; others like the sidebar for translation/research but note it’s off by default and key‑gated; many argue AI should be optional extensions, not baked into browsers; Waterfox reports similar removals.

- Comment pulse
  - Remove AI features → Reduces attack surface for high-risk users; AI in chrome considered un-auditable and exploitable. — counterpoint: Some find sidebar valuable for papers/translation.
  - Make AI an extension, not core → Keeps core lean, configurable; hardcoded provider list contradicts Firefox’s pluggable tradition and neglects extensions ecosystem.
  - Alternatives and settings → Waterfox removes AI too; Orion praised but not OSS; Firefox AI sidebar off by default and requires user API keys.

- LLM perspective
  - View: Tor’s stance is consistent: minimize unreviewable code paths and third‑party data flows in anonymity-critical software.
  - Impact: Pressures Mozilla to modularize AI into opt-in extensions; validates forks (Waterfox, Zen) prioritizing privacy defaults.
  - Watch next: Expect enterprise policies and ESR prefs to disable AI; look for sandboxing, telemetry guarantees, and clear API-key isolation.
