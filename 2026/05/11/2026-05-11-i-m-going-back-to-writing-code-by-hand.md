# I'm going back to writing code by hand

- Score: 911 | [HN](https://news.ycombinator.com/item?id=48090029) | Link: https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/

### TL;DR

After 234 commits and 30 weekends building k10s through Claude sessions, the author is archiving the Go version and rewriting it in Rust. Early velocity hid a 1,690-line god object, 500-line update loop, view-state leakage, conflicting keybindings, positional data, unsafe background mutation, and scope creep from a GPU dashboard into a k9s clone. He will still use AI, but first hand-design architecture, ownership, types, concurrency, and scope. Commenters agreed human judgment remains essential when requirements invalidate design invariants, though some succeed with small modules, tight boundaries, tests, and exhaustive review.

### Comment pulse

- Architecture files cannot replace judgment: when a new feature clashes with an invariant, agents often contort rather than reconsider the design.
- “Comprehension debt” grows when generated code feels understood momentarily but fails to build the durable mental model gained through manual implementation.
- Advocates reported strong results on mechanical migrations and debugging — counterpoint: they require known goals, modular boundaries, fast tests, and active supervision.

### LLM perspective

- View: Generation amplifies the architecture already present; absent intentional structure, local successes compound global incoherence.
- Impact: Developers trade typing time for design, review, and mental-model maintenance rather than leaving the loop.
- Watch next: Rust rewrite structure, feature cuts, defect rate, development pace, code volume, and whether written invariants survive change.
