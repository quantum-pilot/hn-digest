# If you're going to vibe code, why not do it in C?

- Score: 281 | [HN](https://news.ycombinator.com/item?id=46207505) | Link: https://stephenramsay.net/posts/vibe-coding.html

### TL;DR

The essay asks whether code generated without close human reading should abandon human-oriented languages for C, assembly, or a future “vibe-oriented” language that pairs executable output with natural-language intent. The author believes vibe coding works but diminishes understanding and pleasure, suggesting human ergonomics may become unnecessary. HN strongly disputed the premise: models reproduce C memory errors, while Rust’s compiler, types, lifetimes, and package tooling provide automatic feedback. Commenters also argued requirements and maintainability remain human problems even when generation is automated.

### Comment pulse

- Machine generation does not erase human review → maintainers still need readable diffs, local reasoning, debugging, and ownership.
- Guardrails benefit models as well as people → Rust catches memory and concurrency mistakes that plausible-looking C can conceal.
- Requirements remain the binding constraint → vague stakeholder intent cannot be repaired merely by lowering source code toward the machine.

### LLM perspective

- View: An AI-oriented language should maximize verifiable feedback and traceability, not minimize human-readable abstraction.
- Impact: Compiler-enforced contracts may matter more as generated code volume outpaces manual inspection capacity.
- Watch next: Compare defect rates and review effort across C, Rust, Python, and specification-heavy generated workflows.
