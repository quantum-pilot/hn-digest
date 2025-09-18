# Make any site multiplayer in a few lines. Serverless WebRTC matchmaking

- Score: 223 | [HN](https://news.ycombinator.com/item?id=45012080) | Link: https://oxism.com/trystero/

- TL;DR
    - Trystero is a lightweight library adding multiplayer via WebRTC P2P, using existing networks (BitTorrent, Nostr, MQTT, IPFS, Supabase, Firebase) for matchmaking. The demo syncs cursors/clicks with a minimal API and supports A/V and binary data. HN praises the clarity and ease, but flags that “serverless” still depends on third‑party signaling and often needs TURN/SFU. NAT traversal can fail, mesh P2P doesn’t scale beyond small rooms, and a Pointer Events switch would improve touch support.

- Comment pulse
    - Serverless is marketing → signaling still uses third‑party servers; production likely needs TURN, sometimes SFU — counterpoint: “serverless” often means no servers you manage.
    - Mesh P2P scales poorly → NxN connections overwhelm CPU/bandwidth; expect ~4–8 peers; SFU enables larger rooms and better mobile/battery.
    - Practical notes → NAT punching unreliable; Pointer Events handle touch/mouse uniformly; real apps include file transfer, webcams, collaborative canvases.

- LLM perspective
    - View: Great for quick P2P features; not a drop-in for large rooms or enterprise reliability.
    - Impact: Boosts prototypes, hackathons, and niche peer apps; reduces backend needs for small-scale A/V, file, or cursor-sync features.
    - Watch next: Benchmarks for peers-per-room, NAT success rates; examples with TURN/SFU fallback; improved mobile input via Pointer Events.
