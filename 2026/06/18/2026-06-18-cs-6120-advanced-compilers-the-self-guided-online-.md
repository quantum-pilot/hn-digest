# CS 6120: Advanced Compilers: The Self-Guided Online Course (2020)

- Score: 281 | [HN](https://news.ycombinator.com/item?id=48583606) | Link: https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/

### TL;DR

Cornell’s self-guided CS 6120 packages a PhD-level optimizing-compilers course into 14 lessons with videos, notes, research papers, and open-ended implementation work using LLVM and the educational Bril IR. It moves from representation, local and global data-flow analysis, SSA, and loop optimization through alias analysis, memory management, JITs, parallelism, and fast compilation. There are no deadlines, grades, live Zulip participation, or prescribed final project. HN readers clarified that its advanced label means optimization beyond an introductory compiler-construction course, while debating whether trace compilation is obsolete or still valuable in specialized systems.

### Comment pulse

- Trace compilation remains contentious → mainstream JavaScript engines abandoned it — counterpoint: LuaJIT, JAX, and PyTorch show it remains effective in narrower domains.
- Advanced refers to backend optimization depth → Cornell’s first course covers the minimum compiler pipeline; this one studies analyses and transformations beyond construction.
- Industrial context would strengthen dynamic-compilers coverage → type feedback, speculation, deoptimization, tiering, and compilation latency matter more broadly than tracing alone.

### LLM perspective

- **View:** The curriculum’s strength is coupling foundational optimization theory with paper reading and code, turning vocabulary into experimentally testable understanding.
- **Impact:** Self-learners gain backend depth often omitted from interpreter books; practicing engineers get a structured route into compiler research.
- **Watch next:** Add industrial case studies, reproducible benchmarks, project exemplars, and guidance on choosing tracing, tiering, AOT, or hybrid compilation.
