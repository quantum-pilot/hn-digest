# SectorC: A C Compiler in 512 bytes

- Score: 161 | [HN](https://news.ycombinator.com/item?id=46925741) | Link: https://xorvoid.com/sectorc.html

### TL;DR

SectorC packs an x86-16 compiler into a 512-byte boot sector. It accepts a valid C subset with globals, functions, recursion, nested if/while blocks, pointers, comments, fourteen binary operators, and machine-code escapes; examples draw VGA graphics and play PC speaker. Compression tricks make spaces delimit “mega-tokens,” reuse atoi for token and identifier hashing, map variables into a 64K segment, and minimize control flow through fall-through and tail jumps. Commenters admired the hashing and bootstrap potential while stressing that most valid C remains unsupported and error checking requires a linter.

### Comment pulse

- Token hashing impressed readers because one 16-bit calculation classifies numbers and keywords while turning identifiers directly into pseudo-symbol-table addresses.
- Comparisons with a 100,000-line AI-built compiler amused commenters—counterpoint: that system reportedly targets multiple architectures and Linux, making size alone meaningless.
- Minimal binaries evoked boot-sector nostalgia and suggested auditable bootstrap chains from hand-verifiable machine code toward larger compilers.

### LLM perspective

- View: The achievement is constraint-driven language design and code compression, not standards compliance or production compiler completeness.
- Impact: Compiler learners gain a compact executable model; bootstrap researchers gain techniques for shrinking the first trusted binary.
- Watch next: Remaining-byte experiments, collision behavior, generated-code correctness, linter coverage, reproducible builds, bootstrap demonstrations, and ports to constrained targets.
