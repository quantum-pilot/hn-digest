# Helldivers 2 devs slash install size from 154GB to 23GB

- Score: 370 | [HN](https://news.ycombinator.com/item?id=46134178) | Link: https://www.tomshardware.com/video-games/pc-gaming/helldivers-2-install-size-slashed-from-154gb-to-just-23gb-85-percent-reduction-accomplished-by-de-duplicating-game-data-an-optimization-for-older-mechanical-hard-drives

## TL;DR
Arrowhead shrank Helldivers 2’s PC install from ~154GB to ~23GB (an 85% cut) by de-duplicating assets that had been repeatedly copied to “optimize” HDD loading. With help from PC port specialist Nixxes, they discovered that mission load times are dominated by level generation, not disk I/O, and only ~11% of players still use mechanical drives—so the huge bloat was unnecessary. HN discussion focuses on how common unmeasured “optimizations” quietly externalize hardware costs onto users, and how culture, not tech, is the real blocker.

---

## Comment pulse
- Dev incentives misalign with user costs → disk bloat is “free” to the studio but expensive at scale for players’ SSDs—counterpoint: many players have ample space and don’t notice.  
- This wasn’t unique → past titles (e.g., Titanfall, likely CoD) shipped uncompressed or duplicated assets to dodge CPU or seek-time concerns, often on dubious performance assumptions.  
- Performance work is organizationally hard → real profiling, cross-hardware testing, and perf engineering are tedious cost centers, so teams rely on rules of thumb until pain becomes visible.

---

## LLM perspective
- View: Storage “optimization” should be treated like performance and security: measured, reviewed, and tested across real user hardware.  
- Impact: Engines, build systems, and publishers may add size budgets, telemetry, and tooling to flag pathological asset duplication early.  
- Watch next: Other big live-service games adopting “slim builds,” console/PC parity for asset layouts, and platform rules around reporting on-disk vs download sizes.
