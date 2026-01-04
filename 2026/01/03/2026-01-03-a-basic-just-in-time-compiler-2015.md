# A Basic Just-In-Time Compiler (2015)

- Score: 98 | [HN](https://news.ycombinator.com/item?id=46471712) | Link: https://nullprogram.com/blog/2015/03/19/

### TL;DR
The article walks through building a tiny x86‑64 “JIT” that turns a simple recurrence relation (like `+2 *3 -5`) into native machine code at runtime. It covers allocating executable memory with `mmap`/`VirtualAlloc`, flipping permissions with `mprotect`/`VirtualProtect` under W^X, basic calling conventions on System V vs Windows, and getting opcodes by assembling and disassembling small snippets. HN discussion focuses on what “JIT” really means and on math/OS details around the example.

---

### Comment pulse
- “This isn’t really a JIT” → It emits a fixed pattern of code with tiny variability, more like dynamic codegen than compiling an input language.  
- Alternative takes → Any runtime-generated executable memory qualifies as JIT; tiered interpretation isn’t essential—counterpoint: that definition becomes too broad.  
- Math angle → Given only `+ - * /` operations, every program is a linear recurrence with a closed form, useful for jumping directly to large indices.

---

### LLM perspective
- View: Treat this as an approachable primer in executable memory, calling conventions, and code emission, not as a production-style optimizing JIT.  
- Impact: Helpful for systems/VM implementers, exploit mitigations learners, and anyone needing to embed small dynamic code fragments.  
- Watch next: Add branches and an IR, compare against LLVM or libtcc for speed, and explore portable JIT APIs (e.g., Wasm, libjit-style).
