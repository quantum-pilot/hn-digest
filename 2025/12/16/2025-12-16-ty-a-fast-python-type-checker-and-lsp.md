# Ty: A fast Python type checker and LSP

- Score: 209 | [HN](https://news.ycombinator.com/item?id=46294289) | Link: https://astral.sh/blog/ty

### TL;DR
Astral (makers of Ruff and uv) released the beta of **ty**, a Rust-based Python type checker and language server focused on extreme speed and incremental updates. Benchmarks show 10–60x faster cold runs than mypy/Pyright and orders-of-magnitude faster feedback in large projects. ty adds a richer type system (e.g., intersections), pragmatic inference to reduce unnecessary annotations, and Rust-style, multi-file diagnostics. HN discussion centers on comparing it with Pyright/Pyrefly, early UX quirks, and hopes Astral can monetize sustainably.

---

### Comment pulse
- Tool choice is shifting: many use Pyright (or BasedPyright) and mypy together; ty’s speed and pragmatism tempt consolidation—counterpoint: spec-conformance tables don’t reflect real-world usefulness.  
- Early testers report smooth LSP behavior and much faster feedback, but note overly verbose type displays and some editor-compatibility issues (e.g., Cursor extension install failure).  
- Users praise Astral’s ecosystem contributions and ty’s “don’t force annotations” stance, but explicitly worry about future monetization or potential ecosystem rugpulls.

---

### LLM perspective
- View: ty’s incremental, semantic engine positions it as a backbone for richer Python tooling beyond type checking.  
- Impact: large codebases, editors, and CI pipelines gain faster feedback loops and fewer spurious typing complaints.  
- Watch next: stability on diverse real-world repos, third‑party library support, and any paid offerings that might reshape adoption incentives.
