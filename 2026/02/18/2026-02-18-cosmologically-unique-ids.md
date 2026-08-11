# Cosmologically Unique IDs

- Score: 254 | [HN](https://news.ycombinator.com/item?id=47064490) | Link: https://jasonfantl.com/posts/Universal-Unique-IDs/

### TL;DR

The essay asks how to assign decentralized IDs guaranteed unique across a civilization spanning the universe. Random IDs win pragmatically: 122-bit UUID randomness already makes collisions remote, while an extreme whole-universe computation bound suggests 798 bits. The author then tests deterministic ancestry schemes—Dewey, Binary, and Token—proving every such scheme has linear worst-case growth across possible assignment histories. Simulated settlement makes deterministic IDs balloon to roughly 281 MB, so functionally collision-free randomness beats absolute guarantees. Commenters argue the random bound ignores causal locality and is therefore vastly overstated.

### Comment pulse

- Collisions matter only where IDs can later interact; light cones may make 128 or 256 bits more than sufficient.
- CSPRNGs protect unpredictability but do not create entropy; identical seeds still collide.
- Physical storage limits further reduce how many separately addressable objects can exist.
