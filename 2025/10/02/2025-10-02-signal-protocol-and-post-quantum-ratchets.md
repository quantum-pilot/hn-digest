# Signal Protocol and Post-Quantum Ratchets

- Score: 543 | [HN](https://news.ycombinator.com/item?id=45451527) | Link: https://signal.org/blog/spqr/

- TL;DR
    - Signal adds a post‑quantum Sparse Post‑Quantum Ratchet (SPQR) alongside the existing Double Ratchet to form a Triple Ratchet. It uses ML‑KEM 768 with erasure‑coded chunking and a state machine (“ML‑KEM Braid”) to overcome large key sizes, dropped/reordered messages, and selective‑drop attacks, while avoiding parallel epochs that widen compromise impact. Keys are hybrid‑mixed via a KDF, rollout is downgrade‑resistant, and the design/implementation are formally verified. HN discusses iMessage PQ3 tradeoffs and recurring critiques on phone‑number identity and product openness.

- Comment pulse
    - Phone numbers are a weak identifier → SIM takeover/state coercion risks; — counterpoint: usernames and registration lock help, and hijacks don’t reveal past history.
    - Opening SDK/APIs would grow the ecosystem → developers can’t build; — counterpoint: tighter surface reduces attack vectors, aligning with a privacy‑first mission.
    - Signal chunks ML‑KEM with erasure codes → smoother bandwidth, harder to censor; iMessage uses infrequent big rekeys; iCloud backups undercut iMessage secrecy.

- LLM perspective
    - View: Hybrid Triple Ratchet is sensible: combine mature Double Ratchet with PQ KEM, minimize parallel epochs to limit compromise blast radius.
    - Impact: Users keep UX; bandwidth stays predictable; adversaries need both ECC and ML‑KEM breaks or visible DoS to win.
    - Watch next: Measure latency/data overhead; timeline to enforce SPQR-only sessions; any movement on metadata reduction and identity beyond phone numbers.
