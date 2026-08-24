# MinIO repository is no longer maintained

- Score: 442 | [HN](https://news.ycombinator.com/item?id=47000041) | Link: https://github.com/minio/minio/commit/7aac2a2c5b7c882e68c1ce017d8256be2feea27f

### TL;DR

The project’s owner archived its public repository and changed the README from maintenance mode to an explicit end-of-maintenance notice. Existing AGPLv3 source and historical binaries remain available without support or warranty, while users are directed toward licensed AIStor Free or commercially supported Enterprise editions. HN discussion immediately shifted to migrations among Ceph, Garage, SeaweedFS, RustFS, NVIDIA AIStore, and hosted storage. Commenters accepted that free-user support can be economically punishing, but others called the transition a bait-and-switch whose true cost is weeks of risky data movement and testing.

### Comment pulse

- RustFS drew performance praise—counterpoint: its contributor agreement raised fears of another relicensing cycle and unclear legal benefits.
- Ceph advocates favored battle-tested scale despite operational complexity; Garage users disputed installation difficulty, while SeaweedFS reliability claims sharply conflicted.
- Operators stressed exit readiness: S3 compatibility hides behavioral differences, and moving 120 TB can take days while exposing unfamiliar failure modes.

### LLM perspective

- View: The archival event exposes governance and exit risk more than a simple product-support change.
- Impact: Operators inherit migration labor and data risk; competing stores gain users but face scrutiny of licensing and reliability.
- Watch next: Track security fixes, fork activity, migration tooling, compatibility tests, AIStor licensing, and production reports from replacement systems.
