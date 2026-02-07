# C isn't a programming language anymore (2022)

- Score: 106 | [HN](https://news.ycombinator.com/item?id=46907350) | Link: https://faultlore.com/blah/c-isnt-a-language/

### TL;DR
The article argues C has effectively stopped being “just” a programming language and has become a de facto interoperability protocol and ABI for almost all systems software. Every new language must speak C’s ill‑specified headers, types, and calling conventions, across hundreds of platform-specific ABIs that are only described in prose PDFs and sometimes disagreed on by major compilers. Attempts to evolve C (for example, changing `intmax_t`) collide with this frozen ecosystem, making real change nearly impossible. HN debates C’s durability, design sins, and whether a dedicated, language-agnostic ABI would be better.

### Comment pulse
- C’s longevity → only C offers decades-long serviceability and stable tooling; other languages churn. — counterpoint: outside Unix/embedded, C is already displaced by higher-level ecosystems.  
- Critics of the post → tone is “whiny” and fluffy; defenders say it’s clearly about ABI/interop pain, not C-the-language, and human frustration is fair.  
- C design and ABI flaws → unspecified sizes, aliasing, array-to-pointer decay, weak stdlib; some want fixed-width types, others prefer intent-based types like `size_t`.

### LLM perspective
- View: Treat “C as protocol” as a constraint; build rigorous, machine-checkable ABI descriptions and generators instead of re-parsing C headers ad hoc.  
- Impact: Systems languages, OS vendors, and library authors gain safer FFI and clearer upgrade paths, but must accept slower evolution of C-level interfaces.  
- Watch next: Tools like ABI checkers, cross-compiler conformance suites, and subset-ABIs (e.g., restricted C dialects) gaining institutional backing from major platforms.
