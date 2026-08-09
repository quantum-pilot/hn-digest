# A Python Interpreter Written in Python

- Score: 142 | [HN](https://news.ycombinator.com/item?id=47755261) | Link: https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html

### TL;DR

Byterun is a compact Python bytecode interpreter written in Python to expose CPython’s core execution model without its parser, compiler, object runtime, optimizations, or speed. Starting from a three-instruction stack machine, the chapter builds toward real bytecode dispatch, jumps, frames, separate data and block stacks, function calls, exceptions, and named operations. Hacker News praised the explanation for making call stacks concrete, while noting that “500 lines” covers only the interpreter layer and debating whether a Python-hosted interpreter can bootstrap like a self-hosted compiler.

### Comment pulse

- The project demystifies stack execution for readers avoiding CPython’s C — counterpoint: its parser, compiler, and runtime remain borrowed from the host.
- A self-hosted compiler caches each bootstrap generation as a binary; a circular interpreter retains a runtime dependency unless it also emits native code.
- The Python-versus-Perl framing drew correction: Perl also transforms source through AST and opcode stages before execution.

### LLM perspective

- **View:** Byterun succeeds as an executable mental model, not an independent Python implementation or performance competitor.
- **Impact:** Readers can connect source constructs to bytecode, frame state, and stack transitions before confronting CPython’s optimized C.
- **Watch next:** Version compatibility, unsupported opcodes, generator behavior, exception fidelity, actual line count, and experiments extending the instruction set.
