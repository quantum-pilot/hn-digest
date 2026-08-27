# Go has added Valgrind support

- Score: 456 | [HN](https://news.ycombinator.com/item?id=45344708) | Link: https://go-review.googlesource.com/c/go/+/674077

### TL;DR

Go’s runtime gained build-tag-gated Valgrind annotations describing heap arenas, spans, objects, and stacks, allowing binaries to run without many spurious memory errors. The implementation emits client-request instructions through assembly rather than vendoring headers or using cgo. It remains experimental and slow: garbage collection is especially costly, async preemption should be disabled, and leak checking is not yet reliable. The author says the immediate goal is testing whether cryptographic code behaves in constant time, with runtime-memory diagnostics as a possible broader benefit.

### Comment pulse

- Valgrind enables unusual testing → initialization tracking can reveal secret-dependent behavior that noisy timing measurements may miss.
- Runtime integration is incomplete → missing annotations and heavy overhead limit current leak and concurrency diagnosis.
- Minimal assembly pleased readers → it avoids cgo and external headers while preserving a bootstrappable toolchain.

### LLM perspective

- View: Experimental instrumentation is valuable when it targets properties ordinary Go tests cannot observe directly.
- Impact: Crypto and runtime developers gain another diagnostic path, but application teams should expect slow, specialized runs.
- Watch next: Track annotation coverage, false-warning reductions, leak-check support, and reproducible constant-time test cases.
