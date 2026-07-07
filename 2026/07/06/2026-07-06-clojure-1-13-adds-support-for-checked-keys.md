# Clojure 1.13 adds support for checked keys

- Score: 191 | [HN](https://news.ycombinator.com/item?id=48767211) | Link: https://clojure.org/news/2026/07/02/clojure-1-13-alpha1

### TL;DR
Clojure 1.13 adds “checked keys”: an opt‑in way for map access and destructuring to assert that certain keys are present, throwing clear errors when they’re missing. This tightens a long‑standing pain point of Clojure’s nil‑punning map lookups, where missing keys silently return `nil` and failures surface far from the cause. HN discussion centers on trade‑offs between pragmatism and correctness, how this compares to specs/schemas, and whether it aligns with Clojure’s philosophy of small, opt‑in core features.  
*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Missing-key defaults cause rare but severe bugs → runtime checks near the call site are worth a tiny loss of convenience.
- This could be done with assertions or schemas → having lightweight, inline checks in core improves documentation and error locality — counterpoint: some doubt it meets the bar for a core feature.
- Feature fits Clojure’s philosophy → opt‑in, no breaking changes, and codifies a common pattern; complements, not replaces, spec/Malli and optional static typing.

---

### LLM perspective
- View: Checked keys formalize a widespread idiom, reducing “mystery nils” without abandoning dynamic flexibility.
- Impact: Library authors, API boundaries, and data-heavy services gain clearer contracts and faster debugging.
- Watch next: ClojureScript parity, tooling support (REPL messages, linters), and patterns combining checked keys with spec/Malli.
