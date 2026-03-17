# Lies I was told about collaborative editing, Part 2: Why we don't use Yjs

- Score: 188 | [HN](https://news.ycombinator.com/item?id=47359712) | Link: https://www.moment.dev/blog/lies-i-was-told-pt-2

### TL;DR
The author argues that, unless you truly need *masterless* peer‑to‑peer collaboration, Yjs‑style CRDTs are the wrong tool for rich‑text editors. A simple ProseMirror-based, server‑authority protocol (roughly 40 lines around `prosemirror-collab`) delivers optimistic updates, offline editing, provenance, and local‑first behavior with far less complexity. They detail serious issues with Yjs: `y-prosemirror` rebuilding the whole document every keystroke, difficulty meeting 60 fps, brittle schema upgrades, awkward permissions, tombstones/memory trade‑offs, and much harder debugging. The core advice: design from UX, not from the algorithm.

---

### Comment pulse
- Centralized-but-local-first approaches are gaining traction → libraries like DocNode/DocSync offer OT/step-based syncing without CRDT tombstones, vector clocks, or masterless topologies.
- Some practitioners say “just use OT” → mature, server-friendly, easier to debug than CRDTs—counterpoint: author notes OT correctness and editor-state mapping are still tricky.
- Critiques of Yjs span theory and integration → from allegedly flawed proofs to `y-prosemirror`’s full-document replacement—counterpoint: some argue the article conflates Yjs with its ProseMirror binding.

---

### LLM perspective
- View: Most real apps already depend on central services; CRDTs mainly add protocol complexity without proportional user-visible benefit.
- Impact: Framework authors and SaaS editors may pivot toward simpler authority-based protocols with well-defined schemas and permissions.
- Watch next: Benchmarks comparing Yjs, OT, and ProseMirror-collab at scale; new “local-first but centralized” sync stacks maturing into standard libraries.
