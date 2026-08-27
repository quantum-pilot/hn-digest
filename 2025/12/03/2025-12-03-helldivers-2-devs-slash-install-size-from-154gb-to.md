# Helldivers 2 devs slash install size from 154GB to 23GB

- Score: 370 | [HN](https://news.ycombinator.com/item?id=46134178) | Link: https://www.tomshardware.com/video-games/pc-gaming/helldivers-2-install-size-slashed-from-154gb-to-just-23gb-85-percent-reduction-accomplished-by-de-duplicating-game-data-an-optimization-for-older-mechanical-hard-drives

### TL;DR

Arrowhead, assisted by PC-port specialist Nixxes, reduced Helldivers 2's PC installation from about 154GB to 23GB by removing duplicated assets. Duplication had been intended to improve mechanical-drive seek performance, but game-specific measurements showed the assumption was wrong: the 11% of recent players using HDDs would see only a few extra seconds in worst cases because procedural level generation dominates loading. Commenters praised measurement replacing intuition, while debating whether the studio had externalized storage costs and why validation came so late.

### Comment pulse

- Performance engineers stressed measuring end-to-end bottlenecks before trading 131GB of storage for presumed speed.
- Some called duplication a mistaken optimization, not a bug; others emphasized that users bore its accumulated cost.

### LLM perspective

- View: The dramatic reduction came from removing a disproven tradeoff, not discovering exotic compression.
- Impact: Players reclaim substantial storage with minimal downside, including those still using mechanical disks.
- Watch next: Beta load-time data, patch behavior, regressions, and whether asset duplication returns with new content.
