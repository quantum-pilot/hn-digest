# Since Chromium 148, Math.tanh is now fingerprintable to link underlying OS

- Score: 226 | [HN](https://news.ycombinator.com/item?id=48884853) | Link: https://scrapfly.dev/posts/browser-math-os-fingerprint/

### TL;DR
Chromium 148 started delegating `Math.tanh` to the OS math library, so its bit‑exact output varies by operating system. That gives trackers another high‑entropy fingerprinting signal: they can correlate JavaScript results with the underlying OS (or at least a browser/OS/version range), even if user-agent strings are spoofed. HN commenters note that version fingerprinting via subtle JS/CSS feature probes is already common, debate the motives of a scraping company publicizing this, and digress into correctly rounded math libraries.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- `Math.tanh` output can reveal OS and Chromium version range → but browser features already give finer‑grained version fingerprints with less effort.
- Publishing this helps a scraping company normalize and harden fingerprinting → counterpoint: tracking will happen anyway; exposing issues can push browsers to fix them.
- Discovery fuels calls for correctly rounded transcendental functions and stable libm behavior → some argue fixed‑point/integer math is often preferable to IEEE‑754 floats.

---

### LLM perspective
- View: This is an incremental but clean example of how tiny implementation details leak identity via high‑precision side channels.
- Impact: Browser vendors, privacy tools, and anti‑bot systems must treat math-library behavior as part of their fingerprint surface.
- Watch next: See if Chromium normalizes transcendental functions, and whether testers like Cover Your Tracks add math‑based fingerprint checks.
