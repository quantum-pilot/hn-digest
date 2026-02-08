# Hoot: Scheme on WebAssembly

- Score: 162 | [HN](https://news.ycombinator.com/item?id=46923254) | Link: https://www.spritely.institute/hoot/

## TL;DR
Hoot is a Scheme-to-WebAssembly toolchain built on GNU Guile that targets browsers with Wasm GC support. It provides a self-contained compiler plus a Wasm interpreter, so you can compile and test Scheme from the Guile REPL without extra dependencies. Hacker News discussion focuses less on Hoot’s specifics and more on the Guile vs. Racket ecosystem split, performance and tooling trade-offs, and renewed interest in compiling non-JS languages to WebAssembly for browser and edge environments.

---

## Comment pulse
- Scheme ecosystem split → ex-Racketers moving to Guile worries some; they see duplicated effort and miss Racket’s libraries, module system, and metaprogramming—counterpoint: Guile sometimes outperforms and starts faster.
- Tooling trade-offs → Racket praised for syntax-parse, #lang, and submodules; Guile praised for IO, fibers/futures, and Guix integration but needs better debugger and macro tools.
- WebAssembly interest → Hoot seen as proof the “compile to Wasm” idea lives on, giving people more options to avoid JavaScript in browser/edge code.

---

## LLM perspective
- View: Hoot validates Scheme as a serious WebAssembly target, especially where Wasm GC and REPL-driven workflows matter.
- Impact: Guile gains appeal for language hackers, educators, and Guix users wanting reproducible, browser-hosted Scheme systems.
- Watch next: Benchmarks vs. Racket-on-Wasm, Cloudflare/edge compatibility, and improvements to Guile’s debugging, macros, and module ergonomics.
