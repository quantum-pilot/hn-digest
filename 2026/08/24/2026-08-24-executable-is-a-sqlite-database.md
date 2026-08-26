# Executable Is a SQLite Database

- Score: 542 | [HN](https://news.ycombinator.com/item?id=49415271) | Link: https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database

### TL;DR

SELF is a working prototype that stores executable metadata, loadable segments, symbols, dependencies, and even whole userland closures in SQLite. Linux binfmt_misc invokes an ELF interpreter that queries the database, maps segments, relocates symbols, and starts the program. Conventional inspection and patching become SQL queries or transactions. Stripped files approach ELF size, but startup pays roughly 5 milliseconds plus copying that prevents shared text pages. Commenters welcomed queryable binaries and packaging possibilities while debating database terminology, runtime modification, and checksum security.

### Comment pulse

- SQL replaces bespoke binary surgery → symbols, imports, stripping, preload changes, and dependency resolution become indexed queries or atomic updates.
- Database closures deduplicate naturally → 723 executables and 400 libraries occupied 611.9 MiB, below their 644.4 MiB ELF sources.
- Modifiability enables plugins and hot relinking → commenters saw unusual flexibility — counterpoint: mutable executables complicate checksum-based security.

### LLM perspective

- View: SELF trades kernel-native simplicity for schema evolution, transactional tooling, and package-level composition.
- Impact: Tool authors could reuse SQLite, while runtimes absorb latency and memory-sharing costs.
- Watch next: Loader completeness, mmap alternatives, reproducible signatures, direct linker output, cross-platform support.
