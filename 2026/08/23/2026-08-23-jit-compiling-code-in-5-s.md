# JIT Compiling Code in 5μs

- Score: 152 | [HN](https://news.ycombinator.com/item?id=49406387) | Link: https://malisper.me/jit-compiling-code-in-5-us/

### TL;DR

The author presents a copy-and-patch JIT for a toy ARM64 regex engine supporting literals, concatenation, and repetition. It emits machine code by filling instruction stencils, places it in executable memory, and runs within a Rust wrapper. Across supplied inputs, generated matchers were roughly 12–20 times faster than the interpreter and near handwritten performance; pgrust separately claims about five-microsecond query compilation. AI helped with unfamiliar assembly details. Commenters accepted the technique as genuine non-optimizing JIT compilation but challenged claims that JITs are rare and noted established fast frameworks and optimization tradeoffs.

### Comment pulse

- Copy-and-patch is legitimate JIT compilation → producing runtime machine code does not require LLVM or optimization passes.
- Specialized stencils minimize latency → counterpoint: absent register allocation and broader optimization can reduce generated-code quality.
- The ecosystem is not JIT-scarce → commenters cited language runtimes, PCRE2, Cranelift, GNU Lightning, MIR, SLJIT, and AsmJit.

### LLM perspective

- View: The example demonstrates a narrow latency-throughput tradeoff; it does not establish production readiness or general database superiority.
- Impact: Small systems can specialize hot paths cheaply, provided maintainers accept architecture-specific unsafe code and validation burden.
- Watch next: Measure compilation and execution separately across realistic SQL, architectures, code sizes, security constraints, and established lightweight JITs.
