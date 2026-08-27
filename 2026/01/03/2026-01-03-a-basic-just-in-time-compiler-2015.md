# A Basic Just-In-Time Compiler (2015)

- Score: 98 | [HN](https://news.ycombinator.com/item?id=46471712) | Link: https://nullprogram.com/blog/2015/03/19/

### TL;DR

The tutorial turns a tiny arithmetic recurrence language into x86-64 machine code, placing instructions in writable memory, switching pages to executable under W^X, respecting platform calling conventions, and invoking the result through a C function pointer. It deliberately avoids branches, stacks, and sophisticated optimization, making code generation nearly one-to-one. HN discussion focuses less on implementation than terminology: some call it a dynamic code emitter or on-the-fly compilation, while others accept any runtime-generated executable code as JIT compilation.

### Comment pulse

- The JIT label is contested → critics see templated emission, while defenders define JIT by runtime-created machine code.
- The exercise favors mechanics over performance → its constrained recurrence language also admits a closed-form solution.
- Platform details matter → executable-page protections, ABIs, and page-size assumptions expose the nonportable core of native generation.

### LLM perspective

- View: Its pedagogical value comes from making executable-memory and ABI boundaries tangible, not compiler sophistication.
- Impact: Systems learners gain a compact bridge from byte encoding to callable native functions.
- Watch next: Add branching, intermediates, signed division correctness, bounds checks, and instruction-cache handling across architectures.
