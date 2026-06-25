# "Fix" MacBook Neo Cursor Lag: Record 1 Pixel of the Screen Every 10 Seconds

- Score: 207 | [HN](https://news.ycombinator.com/item?id=48654465) | Link: https://gist.github.com/retroplasma/ec21767d0a8380c7ea9c2fbee1c7d6bf

### TL;DR
A MacBook Neo bug causes sporadic mouse cursor lag, likely when macOS switches from a hardware cursor overlay to a software-drawn cursor. A hacky workaround is to run a tiny screen-recording script that captures a single pixel every 10 seconds, forcing the WindowServer to keep compositing the cursor and avoid the lag-triggering transition. Commenters dissect GPU/display pipeline details, mention related historical macOS graphics quirks, suggest cursor-size tweaks, and debate the trade-off between such hacks and waiting for an official fix.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Lag source → Likely GPU/display pipeline transition from hardware to software cursor, involving command-queue flushes or fences delaying updates—counterpoint: modern display and render paths are separate, so this shouldn’t inherently block.
- Alternative tweaks → Changing cursor size can push macOS onto a different compositing path; similar GPU/CPU crossover bugs showed up in TV app and fullscreen low-power mode.
- Fix quality → Scripted 1‑pixel recording is a deliberate, power-wasting nudge to WindowServer; widely seen as an awful-but-pragmatic hack that might pressure Apple to fix.

---

### LLM perspective
- View: This is a classic “tickle the scheduler” hack: add trivial work to bypass a fragile optimization boundary.
- Impact: Power users gain a workaround; Apple’s graphics stack team gets a high-visibility repro of a deeper cursor/compositing bug.
- Watch next: Measure power and latency impact, share reproducible cases, and track macOS updates or driver notes mentioning cursor or compositing fixes.
