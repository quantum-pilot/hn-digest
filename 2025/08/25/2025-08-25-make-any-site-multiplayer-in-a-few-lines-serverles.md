# Make any site multiplayer in a few lines. Serverless WebRTC matchmaking

- Score: 223 | [HN](https://news.ycombinator.com/item?id=45012080) | Link: https://oxism.com/trystero/

### TL;DR

Trystero is an open-source JavaScript library that wraps WebRTC discovery and peer-to-peer communication for multiplayer sites, collaboration, file transfer, presence, and audio or video. Applications join rooms and exchange typed actions or streams without deploying their own signaling service; discovery can use infrastructure including Nostr, MQTT, and BitTorrent, with an optional self-hosted relay. Data is end-to-end encrypted. Commenters caution that “serverless” still relies on external signaling, NAT traversal can fail, and larger rooms generally require TURN or selective-forwarding servers.

### Comment pulse

- Users praised the small API and reported practical success, alongside NAT-punching failures and a mobile pointer-event bug.
- Peer meshes scale poorly: commenters cited connection limits, upload multiplication, battery costs, and the need for an SFU.

### LLM perspective

- View: Trystero meaningfully removes deployment work, but it abstracts infrastructure rather than eliminating dependencies and topology limits.
- Impact: Small-group and local-first experiments become easier, while production reliability still demands explicit fallback and capacity planning.
- Watch next: Document signaling availability, TURN behavior, peer-count thresholds, identity verification, and graceful migration from mesh to SFU.
