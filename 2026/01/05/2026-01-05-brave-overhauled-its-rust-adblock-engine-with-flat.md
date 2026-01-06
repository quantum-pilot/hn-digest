# Brave overhauled its Rust adblock engine with FlatBuffers, cutting memory 75%

- Score: 320 | [HN](https://news.ycombinator.com/item?id=46501894) | Link: https://brave.com/privacy-updates/36-adblock-memory-reduction/

### TL;DR
Brave rebuilt its Rust-based adblock engine to store ~100k filters in FlatBuffers, a compact zero-copy binary format, instead of heap-heavy Rust collections. This cuts adblock memory use by 75% (about 45 MB per browser instance), with extra gains for users enabling more filter lists. Additional optimizations improve allocation behavior, regex matching, and resource sharing. Because Brave’s blocker is native—not an extension—it sidesteps Manifest V3 limits and delivers these wins across desktop, Android, and iOS.

---

### Comment pulse
- Firefox vs Brave defaults → Firefox avoids built-in adblocking and depends on Google funding; Brave leans into opinionated tracking protection—counterpoint: neutrality helps compatibility and politics.  
- Rust sharing story → Brave’s blocker reuses Servo crates and is itself reusable, but commenters debate Rust’s static-linking norm and increased supply-chain risk versus shared libraries.  
- Trust and business model → Some want a debranded, BAT-free fork; others praise Brave’s adblocking but criticize past VPN auto-install and affiliate-link incidents as malware-adjacent.

---

### LLM perspective
- View: Native, highly optimized privacy features are becoming a primary way browsers differentiate once core rendering performance is “good enough.”  
- Impact: Helps low-RAM and mobile devices, and pressures extension-based blockers and rival browsers to match performance without compromising privacy.  
- Watch next: Whether Mozilla or Chromium-based browsers adopt similar compiled filter formats, and if a serious Brave-origin / Helium-style debranded fork gains traction.
