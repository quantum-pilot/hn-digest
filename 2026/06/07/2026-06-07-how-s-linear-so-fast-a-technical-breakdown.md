# How's Linear so fast? A technical breakdown

- Score: 258 | [HN](https://news.ycombinator.com/item?id=48437609) | Link: https://performance.dev/how-is-linear-so-fast-a-technical-breakdown

### TL;DR

An outside analysis attributes Linear’s speed to local-first architecture: IndexedDB and MobX serve UI reads, mutations render immediately then sync through a durable queue, and WebSocket deltas rerender only affected fields. First-load work combines modern-browser-only bundles, aggressive code splitting and preloading, service-worker caching, an inline shell, and rendering cached state before authentication completes. Keyboard shortcuts and brief GPU-friendly animations shorten perceived interaction time. HN challenged the tradeoff: optimistic interfaces can display uncommitted state, hide failed synchronization, and complicate conflicts; daily users also reported slow search and clunky navigation.

### Comment pulse

- Local-first may be unnecessary here → issue tracking shards naturally, and rare concurrent writes could favor simpler synchronous consistency.
- Optimistic writes suit reversible collaboration → counterpoint: closed tabs, important transactions, and hard conflicts make apparent success without confirmation dangerous.
- Fast primitives do not guarantee usable workflows → commenters reported slow search, noisy Pulse, clunky navigation, and dependence on favorites.

### LLM perspective

- **View:** Perceived speed and confirmed durability are separate product properties; interfaces should optimize both without visually conflating them.
- **Impact:** Teams adopting local-first need visible sync state, durable queues, retry guarantees, conflict semantics, and recovery tooling.
- **Watch next:** Benchmark cold load, offline recovery, failed mutations, multi-client convergence, search latency, and memory across workspace sizes.
