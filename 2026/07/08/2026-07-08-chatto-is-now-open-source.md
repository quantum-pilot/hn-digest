# Chatto is now open source

- Score: 671 | [HN](https://news.ycombinator.com/item?id=48833116) | Link: https://www.hmans.dev/blog/chatto-is-open-source

### TL;DR

Chatto 0.4 is now open source and self-hostable as a compact team-chat server with a bundled frontend, encrypted-at-rest messages, end-to-end encrypted voice/video, screen sharing, and direct multi-server connections instead of federation. A hosted, portable Chatto Cloud beta is planned. The author calls it production-stable but expects breaking changes before 1.0 and still needs moderation and client polish. HN praised the deployment documentation, while noting that installations also require NATS and LiveKit. Adoption concerns centered on unclear desktop/mobile availability, iOS notification infrastructure, and conflict between cryptographic account deletion and corporate retention.

### Comment pulse

- Self-hosting is thoughtfully documented → Chatto is compact, but NATS, LiveKit, and preferably S3-compatible storage remain part of a complete deployment.
- Mobile support is a migration blocker → iOS notifications require a publisher-operated relay or each self-hoster to distribute and maintain its own app.
- Per-user key shredding strengthens deletion guarantees → employers may require retained work messages — counterpoint: disabling self-deletion could preserve organizational records.

### LLM perspective

- **View:** Chatto’s differentiator is operational simplicity plus data control, but surrounding media, messaging, storage, and notification services define actual complexity.
- **Impact:** Non-federated servers simplify trust boundaries while client-side multi-server access preserves user choice, trading global identity for isolated communities.
- **Watch next:** Mobile clients, push architecture, moderation tools, backup restoration, key-deletion policies, upgrades across breaking changes, and migration from competitors.
