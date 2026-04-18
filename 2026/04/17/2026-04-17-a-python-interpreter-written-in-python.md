# A Python Interpreter Written in Python

- Score: 142 | [HN](https://news.ycombinator.com/item?id=47755261) | Link: https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html

### TL;DR
Byterun is a small Python bytecode interpreter written in Python, modeled on CPython’s core execution loop. The chapter walks from a toy three-op stack machine to real CPython bytecode: how code is compiled into bytecode, how instructions operate on a data stack, how control flow is implemented via jumps, and how frames, call stack, and block stack interact for function calls, loops, and exceptions. It then outlines Byterun’s design (VirtualMachine, Frame, Function, Block) and shows representative bytecode handlers as a readable guide to CPython internals and virtual machines in general.

---

### Comment pulse
- Interpreter-in-interpreter ≠ self-hosting compiler → no cached binary; feature-bootstrapping creates long CPython→interp→interp chains — counterpoint: once you emit native code, you can bootstrap similarly.
- Nice that it skips parsing → a bytecode-only VM fits in ~1.5k lines and mirrors CPython’s stack-based design, making internals approachable to non-C programmers.
- Article misstates Perl as “purely interpreted” → Perl also compiles to an AST and opcode tree and can run close to C speed.

---

### LLM perspective
- View: This is an excellent concrete bridge from high-level Python to how modern VMs and CPython itself actually execute code.
- Impact: Most useful for learners, debugger/tool authors, and people considering alternative Python runtimes or embedded VMs.
- Watch next: Compare Byterun behavior/perf to CPython on small programs; extend to new bytecodes; instrument it for tracing and visualization.
