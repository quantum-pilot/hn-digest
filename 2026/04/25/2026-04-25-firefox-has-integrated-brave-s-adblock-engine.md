# Firefox Has Integrated Brave's Adblock Engine

- Score: 374 | [HN](https://news.ycombinator.com/item?id=47897891) | Link: https://itsfoss.com/news/firefox-ships-brave-adblock-engine/

### TL;DR
Firefox 149 quietly bundled adblock-rust, Brave’s Rust-based ad/tracker blocking engine, as an *experimental* “rich content blocking” backend. It ships disabled, with no UI or default filter lists; power users can enable it via `about:config` and load EasyList/EasyPrivacy. Mozilla says this is about improving Enhanced Tracking Protection, not replacing extensions, and that Manifest V2 adblockers like uBlock Origin remain supported. HN discussion welcomes Rust and better built-in blocking but is wary of future MV2 deprecation or “acceptable ads” creep.

---

### Comment pulse
- Mozilla’s line: this is a Rust library trial to process tracker lists more efficiently; MV2 and uBlock Origin stay supported—counterpoint: “no plans to” sounds fragile.
- Some fear a path to native-only, possibly compromised adblocking and eventual MV2 removal; others note dual MV2/MV3 support is costly if native blocking is solid.
- Users compare Brave vs Firefox: Brave praised for integrated blocking and scriptlets, but criticized for Chromium dependence and crypto; Firefox valued as the main non-Chromium engine.

---

### LLM perspective
- View: A high-quality, open Rust engine in Firefox raises the floor for privacy protections even if extensions remain primary for power users.
- Impact: Web developers, advertisers, and filter-list maintainers must assume stronger default blocking in non-Chromium browsers over time.
- Watch next: Whether Mozilla exposes a UI, clarifies long-term MV2 policy, and brings similar capabilities to constrained platforms like iOS.
