# Immich v2.0.0 – First stable release

- Score: 481 | [HN](https://news.ycombinator.com/item?id=45446834) | Link: https://github.com/immich-app/immich/discussions/22546

- TL;DR
    - Immich hits its first stable release, and commenters report it already functions as a fast, polished self‑hosted Google Photos alternative: easy setup, solid face recognition, flexible imports (CLI/external folders). Some still prefer Nextcloud for sharing and file-centric workflows, worry about database lock‑in and longevity; others cite FUTO backing, active contributors, and snapshots for safety. Public, Flickr‑style galleries need add‑ons. A “Cursed Knowledge” page sparked side debates on JS timing quirks and database parameter limits.
    - Content unavailable; summarizing from title/comments.

- Comment pulse
    - Fast and featureful; imports via CLI/external dirs; recommend ZFS snapshots; pet/object detection weaker, especially on modest hardware.
    - Prefer Nextcloud and file-system workflows; fear database lock-in, future abandonment — counterpoint: storage templates reorganize files; FUTO-backed, active contributors ease longevity concerns.
    - Not a Flickr replacement out of the box; use immich-public-proxy or a CMS/theme for chromeless, public-facing albums.

- LLM perspective
    - View: v2 stable suggests real maturity; verify export paths to avoid metadata lock-in and ensure reversible on-disk structure.
    - Impact: Could accelerate exits from Google Photos; expect CPU/GPU spikes during indexing, face clustering, and dedupe on modest home servers.
    - Watch next: Native public galleries, search quality benchmarks vs Google/Apple, encrypted off-site backups, and governance/funding disclosures for sustainability.
