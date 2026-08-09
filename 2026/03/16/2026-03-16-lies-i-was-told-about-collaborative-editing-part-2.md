# Lies I was told about collaborative editing, Part 2: Why we don't use Yjs

- Score: 188 | [HN](https://news.ycombinator.com/item?id=47359712) | Link: https://www.moment.dev/blog/lies-i-was-told-pt-2

### TL;DR

Moment rejected Yjs for its ProseMirror editor, arguing that most products need an authority but not truly masterless peer-to-peer reconciliation. With `prosemirror-collab`, clients optimistically submit versioned steps, fetch missed changes, rebase, and retry in about 40 core lines. By contrast, current `y-prosemirror` replaces the document on each collaborative keystroke, disrupting 60-fps budgets, node identity, plugins, schemas, permissions, memory reclamation, and debugging. HN largely favored simpler server-ordered approaches or OT, but challenged whether integration-specific failures justify condemning Yjs or CRDTs broadly and noted production local-first systems need much more machinery.

### Comment pulse

- Authority simplifies correctness → ordered steps enable validation, permissions, idempotency, race tests, and bounded history without sacrificing offline edits.
- Masterless CRDT costs are structural → tombstones, schema ambiguity, and convergence-only guarantees complicate memory and diagnosis when no peer is authoritative.
- Scope drew pushback → critics blamed `y-prosemirror`, not Yjs itself — counterpoint: the author says Yjs architecture still fights centralized rich-text requirements.

### LLM perspective

- **View:** Choose synchronization from required user behavior and topology; masterlessness is an expensive feature, not a default quality badge.
- **Impact:** Rich-text teams can reduce latency and operational risk by centralizing ordering while retaining local optimistic editing.
- **Watch next:** Fine-grained `y-prosemirror` updates, 60-fps benchmarks, schema-upgrade tests, undo correctness, and mature OT or server-ordered libraries.
