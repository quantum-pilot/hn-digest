# A faster way to calculate the day of the week

- Score: 244 | [HN](https://news.ycombinator.com/item?id=49323795) | Link: https://www.benjoffe.com/fast-day-of-week

### TL;DR
The article digs into how to turn a 32‑bit “day count since epoch” into a weekday index much faster than standard `% 7` code. It improves on Hinnant and Neri’s well-known algorithms by exploiting that 7 is a Mersenne number (2³–1), enabling clever multiply–add–shift sequences that avoid full division, work over full 32/64‑bit ranges, and benchmark 2–3× faster than the best existing scalar methods. HN comments branch into mental weekday tricks, real-world date-heavy domains, and praise for the explorable write‑up.

---

### Comment pulse
- Real-world calendars are messier than Unix dates → many people juggle Gregorian, Islamic, Persian, and Orthodox calendars; the hard part is remembering which context uses which.
- Mental algorithm fans → detailed “key dates” trick lets you compute any Gregorian weekday in your head; others question how often that’s actually useful.
- Practicality of micro-optimizing `% 7` → some doubt hot-spot relevance; others cite finance, yield-curve engines, and mass timestamp formatting as performance-critical users.

---

### LLM perspective
- View: This work shows how domain-specific arithmetic (Mersenne-based modulus) can materially beat generic compiler division in tight scalar code.
- Impact: High-throughput date libraries, financial engines, logging systems, and databases can shave cycles off ubiquitous weekday/time computations.
- Watch next: Compiler intrinsics or patterns that recognize mod 7/24/60 and auto-emit these mul–shift forms, plus SIMD/generalized 2ⁿ−2ᵏ support.
