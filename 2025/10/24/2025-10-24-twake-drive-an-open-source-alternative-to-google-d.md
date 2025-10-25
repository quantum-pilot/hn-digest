# Twake Drive – An open-source alternative to Google Drive

- Score: 288 | [HN](https://news.ycombinator.com/item?id=45692984) | Link: https://github.com/linagora/twake-drive

- TL;DR
  - Twake Drive is an AGPLv3, self-hosted Google Drive alternative from Linagora, with a Docker quick start and Node/Mongo backend. HN discussion centers less on feature checklists and more on longevity and interoperability: can it build a sustaining community and integrate with standards like S3/WebDAV/LDAP and enterprise auth? Commenters compare it with Nextcloud, Seafile, and ownCloud, and outline a bar for adoption: dependable sync and conflict handling, no-drama upgrades, solid docs, migration tooling, and native clients.

- Comment pulse
  - Backups must be verifiable → restores often fail despite “enabled” backups; tooling to test/verify is a top concern.
  - Client quality and upgrades dominate UX → Seafile sync praised; ownCloud clients buggy; Nextcloud feels bloated without tuning — counterpoint: tuned AIO runs stable.
  - Bypassing Google Drive backups → on Android, a PWA share-target could capture exports when apps lack alternative cloud options.

- LLM perspective
  - View: Publish a clear threat model and migration/import path; ship a tiny headless CLI for scripted sync and backups.
  - Impact: Strong object-storage and directory-auth support unlocks SME and regulated-sector adoption.
  - Watch next: Public sync/conflict benchmarks, desktop/mobile client roadmaps, backup-restore checks, and sustainable funding/governance signals.
