# sp.h: Fixing C by giving it a high quality, ultra portable standard library

- Score: 183 | [HN](https://news.ycombinator.com/item?id=48207043) | Link: https://spader.zone/sp/

### TL;DR
sp.h is a 15k-line, single-header C99 library that tries to “fix C” by replacing libc with a small, syscall-oriented standard library. It treats heap allocation as explicit policy (user‑supplied allocators), rejects null-terminated strings in favor of pointer+length types, bans hidden globals, and emphasizes explicit error handling. The library aims to be highly portable across mainstream OSes and compilers, but deliberately ignores obscure architectures and micro-optimizations. HN discussion centers on what “extremely portable” really means, string/array design, and whether this is just a new language.

---

### Comment pulse
- Portability claims questioned → supports major OSes/ABIs but skips obscure arches; some argue C’s remaining growth is on microcontrollers—counterpoint: “extremely portable” needn’t mean “supports every DSP.”  
- Data model debate → strong support for pointer+length for strings/arrays; concerns about POSIX `const char*` interop; WTF-8/16 attribution clarified; C99 compound literals-as-lvalues noted.  
- Scope and philosophy → some say sp.h effectively defines a new language and C should be abandoned; others critique unclear examples and reliance on pthreads vs lower-level primitives.

---

### LLM perspective
- View: This is essentially a curated “modern C dialect” runtime that trades compatibility for cleaner primitives.  
- Impact: Best fit for new tools/daemons needing cross-platform C but not bound to libc or legacy APIs.  
- Watch next: Real-world adoption, porting stories (especially Windows/WASM), and how well it coexists with existing POSIX-heavy libraries.
