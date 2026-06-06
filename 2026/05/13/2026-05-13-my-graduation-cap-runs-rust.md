# My graduation cap runs Rust

- Score: 208 | [HN](https://news.ycombinator.com/item?id=48116207) | Link: https://ericswpark.com/blog/2026/2026-05-12-my-graduation-cap-runs-rust/

### TL;DR
A Purdue student hacked together a Rust-powered graduation cap that lights up when the tassel moves, using an ATtiny85, WS2812B LEDs, a reed switch, and a USB-C power bank. Getting Rust to run on the ATtiny85 required forking `avr-hal` and `ws2812-avr` and patching clock settings, so the two-hour coding session was mostly tool-wrangling, while hardware took 3+ hours. Hacker News enjoyed the “married to the blog title” commitment and veered into a debate about US cap-and-gown rental practices.

---

### Comment pulse
- Rust-on-ATtiny for a joke title → Commenters love the dedication to aesthetics and wordplay over practicality—counterpoint: some would have preferred a simpler Arduino-based build.
- Cap/gown rentals are overpriced and sometimes mandatory → Many report $90–130 fees and no-ceremony-without-regalia rules—counterpoint: others say their schools allowed cheap purchase or options.
- People game or skip ceremonies to avoid costs → Sharing gowns across time slots, skipping in-person graduation, or doing online programs all cited as ways to dodge regalia markups.

---

### LLM perspective
- View: This project nicely illustrates “fun-first” engineering: a contrived tech choice (Rust, ATtiny85) becomes a small exploration of embedded ecosystems.
- Impact: Encourages students and hobbyists to treat ceremonies and milestones as excuses for playful hardware experiments, not just formalities.
- Watch next: More robust Rust support for small AVRs, plus better docs and examples for ultra-low-resource microcontrollers and wearable LED builds.
