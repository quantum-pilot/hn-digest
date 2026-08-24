# Revisiting "Let's Build a Compiler"

- Score: 250 | [HN](https://news.ycombinator.com/item?id=46214693) | Link: https://eli.thegreenplace.net/2025/revisiting-lets-build-a-compiler/

### TL;DR

Eli Bendersky revived Jack Crenshaw’s 1988–95 compiler tutorial by translating its Pascal and Motorola 68000 examples to Python and WebAssembly, with generated programs tested through Wasmtime. The series remains unusually approachable because it builds executable slices early with hand-written recursive descent and syntax-directed code generation. HN readers admired that vertical progression and decomposition into primitives, while noting its natural ceiling: once types, optimization and richer analysis arrive, an AST or intermediate representation becomes the cleaner architecture.

### Comment pulse

- Executable slices motivate learners → each lesson produces visible behavior instead of postponing code generation behind theory.
- Single-pass simplicity has limits → IR unlocks global optimization, while function-level passes offer a practical middle ground.
- Recursive descent wins affection → commenters value readable control flow over generator-first pedagogy.

### LLM perspective

- View: The tutorial’s sequencing matters more than its vintage backend.
- Impact: Beginners reach working compilers before abstraction fatigue.
- Watch next: A modern AST transition with typed analysis and optimization.
