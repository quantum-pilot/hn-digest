# Bluesky Protocol Services

- Score: 206 | [HN](https://news.ycombinator.com/item?id=49293324) | Link: https://atproto.com/blog/introducing-bluesky-protocol-services

### TL;DR

Bluesky created Protocol Services to separate documentation and service contracts for its public AT Protocol infrastructure from the social app. The accompanying Jetstream v2 adds server-hosted Network Replay: clients filter compressed historical segments over HTTP, then join the live JSON WebSocket stream without gaps, or request a point-in-time snapshot. Archive access requires a token because of bandwidth; live streaming remains unauthenticated, v1 stays available, and Jetstream remains self-hostable. New TypeScript and Go SDKs handle reconnection, deduplication, cursors, and typed decoding. Commenters welcomed recovery and analytics uses.

### Comment pulse

- Existing users praised browser-simple firehose access and backward compatibility with v1 live streams.
- App builders value replay for restoring public user data after loss; discussion also explored more speculative protocol uses such as DNS-like updates.

### LLM perspective

- View: Treating history and live events as one filtered stream removes substantial client-side backfill and cutover complexity.
- Impact: Developers can build recoverable apps and retrospective analyses without first maintaining a complete local network mirror.
- Watch next: Replay completeness, retention, token issuance, archive bandwidth, SDK stability, v1 lifetime, and seamless live cutover need operational evidence.
