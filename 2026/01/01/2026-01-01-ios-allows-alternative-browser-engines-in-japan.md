# iOS allows alternative browser engines in Japan

- Score: 340 | [HN](https://news.ycombinator.com/item?id=46453950) | Link: https://developer.apple.com/support/alternative-browser-engines-jp/

## TL;DR
Apple will let iOS apps in Japan use non-WebKit browser engines starting with iOS 26.2, via two entitlements: full browser apps and embedded in‑app browsers. Eligible engines must be Japan-only builds, pass strict standards tests (Web Platform Tests, Test262), use memory-safe approaches for web-content code, adopt modern mitigations (PAC, MIE), and enforce strong privacy defaults (blocked third‑party cookies, partitioned storage). HN discussion centers on Chrome/Chromium dominance fears, Apple’s regional compliance strategy, and whether these tight rules will block real competition.

---

## Comment pulse
- Chrome hegemony worry → WebKit lock-in is seen as a bulwark against Chromium dictating web features—counterpoint: relying on Apple as “savior” is learned helplessness.  
- Real choice vs practicality → Some welcome “real” Chrome/Firefox with full extensions; others think Japan-only scope and shrinking mobile web limit real impact.  
- Rules as de facto barrier → Japan reuses EU-style constraints (separate binaries, local presence, strict tests), which commenters say has so far stopped any non-WebKit EU browsers.

---

## LLM perspective
- View: The security/memory-safety requirements are reasonable individually but collectively function as a high regulatory and engineering barrier.  
- Impact: Only major engine stewards (Google, Mozilla) are likely to qualify; small or experimental engines are effectively excluded.  
- Watch next: Whether any alternative engine actually ships, and if other regulators demand global—not region-scoped—engine openness from Apple.
