# The future of version control

- Score: 370 | [HN](https://news.ycombinator.com/item?id=47478401) | Link: https://bramcohen.com/p/manyana

### TL;DR

Bram Cohen’s Manyana is a roughly 470-line Python demonstration of CRDT-based version control for individual files. Its weave retains every line and its add/remove history, allowing deterministic, order-independent merges without common-ancestor reconstruction. Overlapping edits are still flagged, but the merged state exists instead of blocking the workflow, and markers describe each side’s actual operation. Cohen also sketches history-preserving rebase through a primary-ancestor annotation. Cherry-picking and local undo remain unimplemented, so the project is a design argument and UX experiment rather than a usable Git replacement.

### Comment pulse

- Skeptics say better merge displays already exist through Git’s diff3 modes and graphical tools, making a new storage model unnecessary.
- Others dispute “never failing” merges — counterpoint: supporters stress unresolved conflicts can be preserved and reviewed without halting state convergence.
- Pijul, Darcs, Codeville, and Jujutsu repeatedly surfaced as prior art or alternative approaches.

### LLM perspective

- **View:** The interesting claim is compositional history, not merely prettier conflict markers.
- **Impact:** Nonblocking conflicts could suit agent-heavy workflows where large, concurrent changes make traditional rebases costly.
- **Watch next:** Demonstrations of semantic conflicts, repository-scale performance, renames, binaries, cherry-picking, and intuitive rollback.
