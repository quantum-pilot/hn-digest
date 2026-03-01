# Woxi: Wolfram Mathematica Reimplementation in Rust

- Score: 225 | [HN](https://news.ycombinator.com/item?id=47155526) | Link: https://github.com/ad-si/Woxi

### TL;DR
Woxi is an AGPL-licensed Rust interpreter for a substantial subset of the Wolfram Language, aimed at fast CLI scripting and notebook use. It ships a Jupyter kernel, a browser-only JupyterLite demo with graphics, and a growing library of >900 functions, tested against WolframScript for behavioral parity. HN discussion focuses less on current features and more on architecture (tiny core with rules vs Rust-implemented primitives), skepticism about ever reaching Mathematica’s polish and performance, and its role as an open, potentially compatible alternative.

---

### Comment pulse
- Core design debate → Some argue all math should be term-rewriting rules in Woxi itself for maintainability and correctness—counterpoint: that seems unbearably slow and anti-Rust’s performance ethos.  
- Utility vs polish → Critics doubt a clone can match Mathematica’s decades of refinement; supporters see value as an open, scriptable WL kernel and for running legacy code.  
- Risks and comparisons → Questions about symbolic correctness, legal/clean-room status, and how it stacks up against Mathics, Rubi, Julia/Jupyter; interest that much code seems LLM-assisted.

---

### LLM perspective
- View: Targeting CLI and notebook compatibility first is pragmatic; a full Mathematica replacement is a multi‑year, community‑scale effort.  
- Impact: Most useful for researchers, educators, and tooling authors needing a free WL kernel or reproducible symbolic backend.  
- Watch next: Concrete math benchmarks vs Mathematica, Rubi compatibility, and clarification of legal stance and architecture direction (Rust vs in-language rules).
