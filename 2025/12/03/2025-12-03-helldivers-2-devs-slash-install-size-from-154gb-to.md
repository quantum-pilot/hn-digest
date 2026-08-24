# Helldivers 2 devs slash install size from 154GB to 23GB

- Score: 370 | [HN](https://news.ycombinator.com/item?id=46134178) | Link: https://www.tomshardware.com/video-games/pc-gaming/helldivers-2-install-size-slashed-from-154gb-to-just-23gb-85-percent-reduction-accomplished-by-de-duplicating-game-data-an-optimization-for-older-mechanical-hard-drives

### TL;DR

Arrowhead and Nixxes produced a beta PC build that removes duplicated assets, shrinking the installation from roughly 154GB to 23GB while preserving progression, purchases, and functionality. Duplication had been intended to reduce mechanical-drive seek times, but game-specific measurements showed that level generation, running alongside asset loading, dominates mission startup. The 11% of recent players using hard drives should see only a few extra seconds in worst cases. The change saves about 131GB and exposes the cost of optimizing from industry assumptions instead of measurements.

### Comment pulse

- Commenters criticized externalizing storage costs and not validating the bottleneck earlier; others called the choice a mistaken optimization, not a bug.
- Performance engineers emphasized measuring whole-system bottlenecks, because intuitive optimizations often target work hidden behind slower parallel tasks.
- Technical discussion explained duplicating shared assets per level can improve sequential HDD reads, while Steam compression already reduced download size.

### LLM perspective

- View: The dramatic reduction came from removing a legacy tradeoff, not inventing extraordinary compression.
- Impact: Players recover storage while the small HDD minority accepts modestly longer loads.
- Watch next: Beta regressions, measured load-time distributions, engine constraints, and whether other PC games audit duplicated assets.
