# Doom crash after 2.5 years of real-world runtime confirmed on real hardware

- Score: 443 | [HN](https://news.ycombinator.com/item?id=45268269) | Link: https://lenowo.org/viewtopic.php?t=31

TL;DR
- An enthusiast validated a theoretical DOOM engine bug: a demo-tracking counter continues incrementing across demos until it overflows and crashes. After estimating a ~2.5‑year rollover, they ran DOOM nonstop on a small PDA powered by a DIY UPS. The game crashed only hours after that mark, confirming a hard crash on real hardware from the overflowed counter comparison. The experiment highlights how long-lived, unbounded counters can hide rare, time-bomb failures outside normal testing horizons.

LLM perspective
- View: Long-haul soak test confirming an integer overflow in DOOM’s demo timer/comparison logic on unmodified hardware.
- Impact: Encourages source ports to audit long-running counters, add bounds checks, and include duration-based regression tests.
- Watch next: Reproduce in popular ports, identify exact variable/type, patch, and publish a minimal repro plus unit test.
