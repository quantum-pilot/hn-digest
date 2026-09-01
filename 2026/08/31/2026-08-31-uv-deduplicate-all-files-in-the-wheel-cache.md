# uv: Deduplicate all files in the wheel cache

- Score: 217 | [HN](https://news.ycombinator.com/item?id=49506142) | Link: https://github.com/astral-sh/uv/pull/21327

### TL;DR

A merged uv change deduplicates every wheel-cache file by storing content under its BLAKE3 hash and hardlinking objects into archived wheel layouts, leaving installation behavior unchanged. On the author’s local cache, this saved 545.2 MiB, roughly 10%; that is a measurement, not a universal ratio. Controlled Linux/ext4 tests across four pinned wheels measured cold-install slowdowns of about 3.0–4.0%, with warm medians near unchanged. Commenters weigh persistent disk savings against added complexity, platform-sensitive hardlink behavior, and uv’s existing cache-size tradeoff.

### Comment pulse

- Cache growth motivates deduplication → uv’s extracted-wheel cache accelerates warm installs but can expand substantially across many environments.
- Hardlinks raise caution → a pip contributor warns shared mutable files can create surprising cross-environment edits and platform-specific failure modes.
- Percentages hide user priorities → occasional extra seconds may be cheap, while hundreds of persistent megabytes matter on constrained disks.

### LLM perspective

- View: The trade is credible locally, but savings depend on package overlap and costs depend on filesystem behavior.
- Impact: Multi-environment Python users may reclaim cache space without materially changing warm installation latency.
- Watch next: Measure diverse caches, macOS and Windows behavior, copy fallbacks, corruption recovery, and end-to-end network installs.
