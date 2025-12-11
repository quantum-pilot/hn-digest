# Revisiting "Let's Build a Compiler"

- Score: 250 | [HN](https://news.ycombinator.com/item?id=46214693) | Link: https://eli.thegreenplace.net/2025/revisiting-lets-build-a-compiler/

### TL;DR
Eli Bendersky revisits Jack Crenshaw’s classic “Let’s Build a Compiler” by reimplementing its Pascal/68000 tutorial compiler in Python targeting WebAssembly. He explains why the 1988–1995 series still resonates: building a hand-written recursive‑descent parser stepwise and generating real code from the start demystifies compilers more than theory‑heavy courses. Bendersky also critiques its syntax-directed, single-pass style, arguing that once types enter, you really want an AST/IR and separate passes. HN comments expand on pedagogy, parsing styles, and optimization tradeoffs.

---

### Comment pulse
- Early end-to-end codegen beats front-end theory → a tiny working compiler, then gradual enrichment, teaches language features better—counterpoint: formal theory remains crucial for production-grade compilers.  
- Recursive-descent parsing shines pedagogically and practically → exposes problem “primitives”, stays flexible, easy for LLMs to emit; table-driven generators now mainly for niche DSLs.  
- Syntax-directed single-pass compilation simplifies toy compilers → fine with define-before-use, but blocks IR optimizations and deeper type checks; dual-pass per-function designs balance speed and quality.  

---

### LLM perspective
- View: Porting classic tutorials to modern stacks and targets extends their lifespan and makes foundational ideas accessible to newer generations.  
- Impact: Beginners can now build compilers in Python/WASM, skipping obsolete toolchains yet still experiencing the full pipeline from syntax to execution.  
- Watch next: Natural follow-up: a second-stage tutorial introducing ASTs, IRs, and basic optimizations, reusing the same KISS language as baseline.
