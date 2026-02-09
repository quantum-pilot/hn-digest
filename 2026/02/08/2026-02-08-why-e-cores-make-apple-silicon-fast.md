# Why E cores make Apple silicon fast

- Score: 226 | [HN](https://news.ycombinator.com/item?id=46933365) | Link: https://eclecticlight.co/2026/02/08/last-week-on-my-mac-why-e-cores-make-apple-silicon-fast/

### TL;DR
Apple silicon’s standout “speed” largely comes from its efficiency (E) cores and macOS’s Quality of Service (QoS) scheduling, not just raw performance (P) cores. macOS aggressively pushes indexing, malware scans, media analysis, and other background work onto E cores, keeping P cores mostly free for responsive UI and user apps, even right after boot. QoS tags keep low‑priority threads off P cores entirely, trading some background latency for consistent foreground performance, lower contention, and better battery life—at the cost of complexity and debuggability.

---

### Comment pulse
- Many tiny processes are good → Fine‑grained services let macOS assign accurate QoS and pack E cores, rather than one big app competing with user work.  
- Apple silicon “fast” means perf‑per‑watt and UX → Fanless laptops feel like desktops; against Linux on x86 it’s closer, and Intel’s Panther Lake narrows the gap.  
- Complexity bites back → Hundreds of daemons make misbehaving Spotlight/iCloud/Photos hard to diagnose; logs are noisy, modeling system behavior is difficult.

---

### LLM perspective
- View: Hybrid-core plus strict QoS separation is a software–hardware co-design pattern others should copy, especially for laptops and phones.  
- Impact: OS schedulers, app frameworks, and performance tools must expose QoS and core-type behavior clearly to developers and power users.  
- Watch next: Better Activity Monitor–style UIs that normalize for frequency, plus APIs to surface “why is this thread here?” scheduling decisions.
