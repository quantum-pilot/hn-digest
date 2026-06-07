# Python JIT project was asked to pause development

- Score: 140 | [HN](https://news.ycombinator.com/item?id=48425982) | Link: https://discuss.python.org/t/an-announcement-from-the-steering-council-regarding-the-jit-project/107638

### TL;DR
The Python Steering Council has told CPython’s experimental JIT team to stop adding new JIT features to the main branch until a Standards Track PEP is written, discussed, and accepted, or the JIT is removed. The PEP must define long‑term maintenance, tooling/debugger guarantees, performance targets, and how it relates to other JITs. Core devs worry a moratorium and six‑month window will stall momentum, while others see this as overdue governance after years of ad‑hoc experimentation.

---

### Comment pulse
- This is a poison pill to kill the JIT → broad infra requirements + six‑month “resolved” deadline invite bikeshedding and failure — counterpoint: large, permanent features must prove maintainability first.  
- JIT payoff seems small → current gains (~15%) may not justify complexity vs PyPy or Ruby YJIT; some feel rug‑pulled just as it beat the interpreter.  
- It’s a feature freeze, not a ban → only new JIT features are blocked in main; work can continue in forks, but contributors fear painful rebases and lost volunteers.

---

### LLM perspective
- View: This is CPython tightening governance: demanding explicit contracts for runtime‑level changes after past “YOLO” merges.  
- Impact: JIT contributors face uncertainty; distributors, tool authors, and performance‑sensitive users may finally get clear guarantees or a reset.  
- Watch next: The JIT PEP’s performance bar, tooling guarantees, and decision on “one JIT vs JIT infrastructure” will determine whether code stays or moves out-of-tree.
