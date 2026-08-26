# iCloud Photos Downloader

- Score: 261 | [HN](https://news.ycombinator.com/item?id=46578921) | Link: https://github.com/icloud-photos-downloader/icloud_photos_downloader

### TL;DR

icloudpd is a volunteer-maintained command-line tool for downloading iCloud Photos on Linux, Windows, macOS, and NAS systems. It supports copy, sync, and move modes; Live Photos, RAW files, deduplication, continuous watching, incremental runs, and EXIF updates. Setup requires web access to iCloud data and disabling Advanced Data Protection, while the project seeks a maintainer. HN readers valued a reliable escape path for large libraries but emphasized that true backup also requires albums, edits, paired assets, dates, restore verification, privacy review, and workable ADP support.

### Comment pulse

- Files alone are incomplete backups → albums, edits, bursts, Live Photo pairings, and dates require state-aware restoration and verification.
- Large Windows libraries expose client weaknesses → users report prolonged transfers, placeholder files, and uncertainty about full-quality completion.
- Alternatives cover different needs → direct USB copying, Mac exports, privacy exports, and paid apps vary in metadata, scheduling, restoration, and ADP support.

### LLM perspective

- View: Photo portability is a state-migration problem, not merely bulk file transfer.
- Impact: Families gain account-lockout resilience, but weak restore fidelity can create false confidence.
- Watch next: Secure a maintainer and publish ADP compatibility, integrity checks, metadata round trips, and large-library recovery tests.
