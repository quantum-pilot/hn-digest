# C89cc.sh – standalone C89/ELF64 compiler in pure portable shell

- Score: 191 | [HN](https://news.ycombinator.com/item?id=47598413) | Link: https://gist.github.com/alganet/2b89c4368f8d23d033961d8a3deb5c19

### TL;DR

A single shell script implements a C89 parser and compiler that reads C from standard input and emits an executable x86-64 ELF file, even with PATH emptied. It relies on shell built-ins, supports several common shells, and includes a miniature libc; much of its mechanical parser and emitter is BNF-generated from modular shell sources. HN treated it chiefly as an impressive systems experiment and possible human-verifiable bootstrap artifact. The author says the modules have comprehensive tests, but documentation is incomplete and it is not production-ready.

### Comment pulse

- Bootstrapping advocates see a path from a preexisting shell to C using inspectable artifacts—counterpoint: shells themselves generally require compiled foundations.
- Critics requested a repository, documentation, and public tests; the author says tests exist across the underlying modules.
- Shared-hosting veterans note that a compiler requiring only shell built-ins weakens the protection gained by omitting compiler binaries.

### LLM perspective

- **View:** This is strongest as an executable demonstration of shell expressiveness, not a practical replacement for established toolchains.
- **Impact:** Reproducible-build and bootstrap researchers gain another unusually small trust path to inspect.
- **Watch next:** Published conformance tests, supported C89 subset, cross-shell portability results, reproducible output, and performance measurements.
