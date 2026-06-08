# How's Linear so fast? A technical breakdown

- Score: 258 | [HN](https://news.ycombinator.com/item?id=48437609) | Link: https://performance.dev/how-is-linear-so-fast-a-technical-breakdown

## TL;DR

Linear feels “instant” because it treats the browser as the primary database and the server as a sync target. UI reads and writes go to an in‑memory MobX graph backed by IndexedDB; mutations apply locally and sync over WebSocket in the background. Initial load is sped up with aggressive code-size reductions, per-package code splitting, modulepreload, and a service worker that precaches the whole app. Design reinforces speed via keyboard-first interaction and carefully constrained, very short animations.

---

## Comment pulse

- Local-first here feels unnecessary → backend for an issue tracker could already be sub‑10 ms; local DB adds complexity and potential inconsistency — counterpoint: user-perceived latency is dominated by network, not DB.

- Optimistic UI is risky → users may think changes are committed when they’re not, and conflict resolution/offline recovery is hard for many domains.

- UX not universally praised → some daily users report slow search, noisy Pulse, and difficulty navigating, saying early Trello felt smoother despite Linear’s touted speed.

---

## LLM perspective

- View: Linear shows that a clean, local-first architecture plus many small optimizations can outperform heavier “modern” stacks.

- Impact: Best suited to productivity tools where tabs stay open and eventual consistency is acceptable; not ideal for critical transactions.

- Watch next: More off-the-shelf local-first/sync tooling, better conflict patterns, and benchmarks comparing local-first vs traditional SPA + fast APIs.
