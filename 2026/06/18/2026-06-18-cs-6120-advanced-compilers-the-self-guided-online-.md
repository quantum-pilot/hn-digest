# CS 6120: Advanced Compilers: The Self-Guided Online Course (2020)

- Score: 281 | [HN](https://news.ycombinator.com/item?id=48583606) | Link: https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/

### TL;DR
Cornell’s CS 6120 is a free, self-guided, PhD-level course on optimizing compilers, published with videos, notes, and implementation tasks. It uses LLVM plus a teaching IR (Bril) to cover intermediate representations, classic optimizations, SSA, alias analysis, profiling, JITs, garbage collection, parallelism, and verification. The Hacker News discussion praises the material but debates the emphasis on trace-based dynamic compilation and the “advanced” label, arguing that much of what’s taught here is often missing from typical “intro compiler” courses.

---

### Comment pulse
- Trace compilation is overemphasized → many see it as a dead end; industrial practice leans on type feedback, speculation, deoptimization, and tiered compilation — counterpoint: LuaJIT, JAX, and torch.compile still use tracing effectively.
- “Advanced” label questioned → topics like SSA, data flow, DCE are foundational; at Cornell, they’re the second course, focused on optimization and backends, after a separate parsing/codegen class.
- Typical resources stop at frontends → many hobbyists and books barely cover backends; this course fills that gap with serious treatment of optimization and runtime systems.

---

### LLM perspective
- View: This is a rare, coherent, research-oriented backend curriculum made fully public, bridging the gap between textbooks and production compilers.
- Impact: Most useful for grad students, language implementers, and serious hobbyists wanting to move beyond parsing into real-world optimization and JIT design.
- Watch next: Compare with current industrial JITs (V8, JVM, PyTorch, JAX) and update materials around modern tiering, deoptimization, and hardware-specific optimization.
