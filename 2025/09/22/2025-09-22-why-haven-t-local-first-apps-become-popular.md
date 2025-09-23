# Why haven't local-first apps become popular?

- Score: 273 | [HN](https://news.ycombinator.com/item?id=45333021) | Link: https://marcobambini.substack.com/p/why-local-first-apps-havent-become

- TL;DR
  Local‑first remains niche because sync is a distributed-systems problem. The article proposes HLCs to order changes without a central clock and CRDTs (often LWW) to converge state, implemented as a small SQLite extension that stores per‑field change messages and achieves deterministic, cross‑platform sync. HN pushes back: many apps can ride simple file‑sync/autosave/versioning and better caching; CRDT data modeling and replay are hard and can violate user semantics; truly conflicting edits still need human or app‑specific merges; incentives favor server‑first control.

- Comment pulse
  - File sync + autosave/versioning suffices → most users don’t edit concurrently; app watches synced folder and reloads on change — counterpoint: breaks with simultaneous edits.
  - CRDTs are hard to model and operate → matching user/business semantics across types is complex; operation logs and state reconstruction add runtime and maintenance overhead.
  - Cache more, phone home less → correct Cache-Control and local tile/media caching cover most offline UX; companies prefer server‑first for telemetry, control, and lock‑in.

- LLM perspective
  - View: Start with caching and simple sync; layer CRDTs only where concurrent edits materially matter; add guided, domain-specific merge UIs.
  - Impact: Better performance for most apps; fewer backend calls; collaborative editors still need rigorous testing and specialized data structures.
  - Watch next: Real-world case studies of SQLite-Sync; latency/consistency benchmarks vs Automerge/Yjs; UX patterns for conflict prompts and partial merges.
