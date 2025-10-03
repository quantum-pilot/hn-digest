# Immich v2.0.0 – First stable release

- Score: 506 | [HN](https://news.ycombinator.com/item?id=45446834) | Link: https://github.com/immich-app/immich/discussions/22546

- TL;DR
    - Immich hits v2.0.0, its first stable release after ~3 years, focusing on long-term compatibility (SemVer, 2.x mobile/server interoperability) and reduced tech debt. The team launched a revamped site, a nostalgic DVD, and plans paid, end-to-end encrypted off-site backups (no paywalls), plus community-discussed telemetry and feature polish (auto-stacking, sharing, groups). HN reactions: strong praise, migration tips (CLI, ZFS, external folders), notes on heavy ingest loads; debate over file-structure portability countered by Immich’s storage templates; “cursed knowledge” page sparked JS/DB gotchas discussion.

- Comment pulse
    - Immich feels fast and polished → users report easy imports (CLI, immich-go), recommend ZFS snapshots; ingest can spike CPU/RAM.
    - Concern: library-only traps data → want filesystem-based organization/export. — counterpoint: storage templates can reorganize on disk; external directories are supported.
    - Cursed-knowledge page sparks JS minutiae (setTimeout, dependency bloat) and DB limits talk → fun, practical lessons; some ask for transparency on planned telemetry.

- LLM perspective
    - View: Stable tag signals maturity and long-term maintenance; not a feature freeze; upgrades from 1.144 should be low-risk.
    - Impact: Self-hosters get predictable updates and forthcoming E2EE backups; admins plan around heavy ingest; photographers gain better sharing/group features.
    - Watch next: Telemetry proposal details, opt-in flows, data retention; backup-service pricing; ingest benchmarks and search accuracy at 100k+ photos.
