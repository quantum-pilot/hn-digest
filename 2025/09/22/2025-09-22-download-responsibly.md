# Download responsibly

- Score: 311 | [HN](https://news.ycombinator.com/item?id=45329414) | Link: https://blog.geofabrik.de/index.php/2025/09/10/download-responsibly/

### TL;DR

Geofabrik asks users of its free OpenStreetMap download service to stop wasteful automation after clients repeatedly fetched 20GB files—one downloaded nearly 10,000 Italy copies in 24 hours. Whole-planet users should fetch the planet file; daily regional users should apply incremental updates with pyosmium, cutting traffic about 98%; scripts should detect failures such as full disks. Commenters blamed careless CI while asking why rate limits, authentication, requester-pays bandwidth, surgical Parquet access, or BitTorrent are not used to protect shared capacity.

### Comment pulse

- Operator empathy → free infrastructure attracts astonishing misuse, but robust APIs should also offer batching, quotas, and clear 429 responses.
- BitTorrent appeal → peer distribution handles large-file herds well; adoption suffers from reputation, firewall, tooling, and seeding concerns.

### LLM perspective

- View: Responsible clients help, but safety limits should assume unattended scripts will eventually fail pathologically.
- Impact: Incremental updates preserve bandwidth for everyone while making daily refreshes faster for legitimate users.
- Watch next: Redirect-aware clients, per-IP quotas, anomaly blocking, authenticated automation, and measured uptake of pyosmium updates.
