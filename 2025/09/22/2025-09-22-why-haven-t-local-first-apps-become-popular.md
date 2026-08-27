# Why haven't local-first apps become popular?

- Score: 273 | [HN](https://news.ycombinator.com/item?id=45333021) | Link: https://marcobambini.substack.com/p/why-local-first-apps-havent-become

### TL;DR

The author says local-first apps remain uncommon because offline edits turn ordinary software into distributed systems: devices must order changes, resolve conflicts, and converge without constant coordination. Their proposed SQLite-Sync extension records column changes as timestamped messages, using hybrid logical clocks and last-write-wins CRDT behavior across platforms. HN commenters argue this understates the hardest problem—mapping conflicting user intentions into acceptable business outcomes—and suggest many products could capture most offline benefits through file synchronization, caching, autosave, versioning, and simpler dirty-state handling.

### Comment pulse

- CRDTs do not infer intent → deterministic convergence can still produce a result neither collaborator expects.
- Simpler patterns cover many cases → synced folders and background reloads may suffice without simultaneous editing.
- Incentives also matter → some readers blame cloud control and data collection, not engineering difficulty alone.

### LLM perspective

- View: Local-first adoption depends on product-specific conflict semantics more than generic synchronization machinery.
- Impact: Teams can gain resilience incrementally before committing every data model to CRDT complexity.
- Watch next: Usability studies, conflict-recovery interfaces, production failure reports, and narrower offline architectures.
