# Download responsibly

- Score: 311 | [HN](https://news.ycombinator.com/item?id=45329414) | Link: https://blog.geofabrik.de/index.php/2025/09/10/download-responsibly/

- TL;DR
  - Geofabrik upgraded its OSM download infrastructure and now redirects .../latest to the concrete file, but pleads for “responsible” use after abuses like 10,000 Italy downloads in 24 hours. They propose: use the planet file for global data, apply incremental updates with pyosmium-up-to-date (~98% less bandwidth), and monitor automation to avoid repeated fetches. HN suggests technical guardrails—rate limiting, lightweight auth, CI detection, “downloader pays”, torrents—while noting practical barriers to BitTorrent and how CI/Docker habits often cause accidental thundering herds.

- Comment pulse
  - Use BitTorrent/CDN-like distribution → reduces single-origin load; companies saw big speedups. — counterpoint: bad reputation, firewall issues, lack of ubiquitous clients/tooling.
  - Enforce rate limits and lightweight auth → shields service from abusers; teach via 429s/leaky buckets; enable “downloader pays” cost-shifting.
  - Many overfetches originate in CI/Docker → automated builds curl large files repeatedly; require keys, detect CI user-agents, or offer diff-friendly formats (Parquet over GPKG).

- LLM perspective
  - View: Combine mirrors, token-bucket limits, and HEAD/ETag checks; publish curl examples that honor If-Modified-Since.
  - Impact: Reduces bandwidth and collateral IP blocks; smoother peaks; fewer CI misconfigurations silently waste terabytes.
  - Watch next: Offer signed URLs or API keys, a public quota dashboard, and explore torrents or zsync for large regional snapshots.
