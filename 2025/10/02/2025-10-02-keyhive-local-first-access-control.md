# Keyhive – Local-first access control

- Score: 160 | [HN](https://news.ycombinator.com/item?id=45445114) | Link: https://www.inkandswitch.com/keyhive/notebook/

- TL;DR
  - Ink & Switch’s Keyhive aims to bring cloud-like access control to local-first/CRDT apps without a central server. It layers convergent capabilities (delegation), a group-management CRDT, and E2EE with causal keys. BeeKEM, a causally ordered TreeKEM variant, provides group key rotation with typical O(log n) cost, handling revocation and concurrent updates via blanking and conflict keys; worst cases degrade to linear. Pre‑alpha Rust/WASM libraries are open. HN discussed cloud-auth comparisons, shared BeeKEM resources, and praised the research-driven approach.

- Comment pulse
  - Cloud auth not always a hot-path DB → bearer tokens enable offline validation; still central guardianship, not local-first — counterpoint: authors emphasize data-local enforcement.
  - BeeKEM explainer aids adoption → external deep dive clarified conflict-keys and concurrency for teams evaluating Keyhive in distributed chat.
  - Ink & Switch praised → research-first, local-first ethos appeals; some nitpicks on site UI tilt/underlines.

- LLM perspective
  - View: Local-first ACL needs CRDT-aware capabilities plus decentralized CGKA; Keyhive’s layering is a sane, pragmatic path.
  - Impact: If it holds, sync servers become interchangeable relays; enterprises get offline-ready E2EE docs with revocation and large-group support.
  - Watch next: Benchmarks under churn, worst-case conflict/blank stress; formal BeeKEM proofs; security audits; developer ergonomics for policy modeling and key recovery.
