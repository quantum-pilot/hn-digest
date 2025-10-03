# Signal Protocol and Post-Quantum Ratchets

- Score: 404 | [HN](https://news.ycombinator.com/item?id=45451527) | Link: https://signal.org/blog/spqr/

- TL;DR
    - Signal is rolling out SPQR, a post-quantum ratchet that preserves forward secrecy and post-compromise security against harvest-now, decrypt-later and device-compromise threats. It extends Signal’s earlier PQ handshake to the ratchet; users shouldn’t see slowdowns and sessions migrate automatically. HN compares this to iMessage’s PQ3 and debates priorities: crypto advances vs developer platform (SDK/APIs/bots), risks of phone-number identity vs new usernames/registration lock, and whether iMessage’s PQ matters when many users’ iCloud backups aren’t E2E. The SPQR name drew Roman jokes.
    - Content unavailable; summarizing from title/comments.

- Comment pulse
    - Crypto-first, product-second: no SDK/APIs/bots, undocumented libsignal, features stuck client-side → poor platform coherence — counterpoint: fewer integrations reduces abuse, nonprofit optimizes for security/usability.
    - Phone-number IDs enable SIM hijack, state takeover, metadata linkage → push for usernames-only, metadata resistance — counterpoint: registration lock, no history exposure, usability keeps adoption.
    - Design: chunked ML‑KEM updates with erasure coding → resists rekey blocking, smooth bandwidth; PQ3 uses periodic big updates; iMessage’s value questioned given non-E2E iCloud backups.

- LLM perspective
    - View: PQ ratcheting closes the ratchet‑downgrade hole; attacker focus shifts to endpoints, traffic shaping, and key‑delivery censorship.
    - Impact: Pressures Apple, Meta, Matrix/MLS to adopt ratchet-level PQ; normalizes PCS as table stakes.
    - Watch next: Public cryptanalysis of SPQR, interop plans, bandwidth/latency data on low-end links, and decoupling identity from phone numbers.
