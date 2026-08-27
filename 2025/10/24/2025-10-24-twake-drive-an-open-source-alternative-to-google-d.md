# Twake Drive – An open-source alternative to Google Drive

- Score: 288 | [HN](https://news.ycombinator.com/item?id=45692984) | Link: https://github.com/linagora/twake-drive

### TL;DR

Twake Drive presents an Affero GPLv3-licensed, self-hostable alternative to proprietary cloud drives. Its repository provides a minimal Docker Compose launch and a Node.js/MongoDB development setup with local document storage. The frozen README offers little detail about end-user features, native synchronization clients, storage backends, identity integration, backup procedures or migration, so direct parity with Google Drive is not established. Discussion focuses on the harder requirements for durable self-hosted storage: predictable sync, understandable conflict handling, restorable backups, painless upgrades, interoperable storage and a community or business capable of maintaining it.

### Comment pulse

- Experiences with Nextcloud, ownCloud and Seafile vary sharply, reinforcing that operational reliability is deployment-specific.
- Readers ask for S3 or WebDAV interoperability, LDAP, native clients, a headless CLI and explicit manual synchronization.

### LLM perspective

- View: Source availability is necessary for autonomy, but dependable data lifecycle and migration determine whether a drive is trustworthy.
- Impact: A narrow self-hosted service may avoid suite bloat, while leaving administrators responsible for continuity and recovery.
- Watch next: Publish supported clients, storage architecture, threat model, upgrade guarantees and tested restore procedures.
