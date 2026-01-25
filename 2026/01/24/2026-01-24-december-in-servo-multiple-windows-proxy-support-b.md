# December in Servo: multiple windows, proxy support, better caching, and more

- Score: 128 | [HN](https://news.ycombinator.com/item?id=46745259) | Link: https://servo.org/blog/2026/01/23/december-in-servo/

### TL;DR
Servo 0.0.4 makes a noticeable step from experiment toward usable engine: multi‑window support, HTTP proxy handling, system root CAs, better caching APIs, and a stronger embedding story (SiteDataManager/NetworkManager, dialogs, console hooks). Web‑platform coverage improves via more CSS/HTML features, SubtleCrypto algorithms, layout and event‑handling fixes, plus cache eviction and GC safety work for stability. Donations and some EU‑linked public funding are growing. HN commenters see Servo (alongside Ladybird) as critical diversification beyond Blink/WebKit/Gecko.

---

### Comment pulse
- Independent engine needed → Reduces dependence on Chrome/WebKit; Mozilla’s future feels shaky, so a community‑governed Servo is strategically important.  
  — counterpoint: Ladybird is currently more correct on many tests, though slower.

- Embedded engine angle → Progress on stability and web compatibility makes Servo increasingly attractive as a lightweight, embeddable web runtime.

- Funding and public support → Grassroots donations are rising; commenters highlight German/EU grants and argue broader EU backing for non‑Chrome engines is warranted.

---

### LLM perspective
- View: Servo is maturing into a practical, embeddable Rust web engine, not just a research renderer.

- Impact: App developers gain a modern alternative runtime; browser diversity and standards experimentation get a concrete testbed.

- Watch next: Media playback, JS performance, WPT pass rates, and long‑term institutional funding will determine whether Servo can underpin mainstream products.
