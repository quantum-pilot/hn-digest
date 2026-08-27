# Huge Binaries

- Score: 187 | [HN](https://news.ycombinator.com/item?id=46417791) | Link: https://fzakaria.com/2025/12/28/huge-binaries

### TL;DR

Massive statically linked x86-64 programs can exceed the roughly ±2 GiB reach of ordinary 32-bit relative calls, producing relocation overflows when code targets are too distant. Compiling with the large code model replaces compact five-byte calls with 12-byte absolute-address sequences, increasing instruction size and register pressure. HN questioned whether multi-gigabyte text sections signal architectural or dead-code problems, while practitioners described real 25 GB stripped binaries and suggested layout optimization, split debug data, LTO, garbage collection, or smaller deployable components.

### Comment pulse

- Huge executables look pathological → critics favor service decomposition or packaged multi-file artifacts over continuously scaling build infrastructure.
- Toolchain cleanup can help → split DWARF, LTO, function sections, and dead-code elimination may remove avoidable bulk.
- Scale can still be legitimate → data-processing binaries reportedly reached 25 GB stripped, where splitting work might cost more than locality saves.

### LLM perspective

- View: The relocation limit turns code size from storage inconvenience into an architectural and instruction-generation constraint.
- Impact: Large monorepos need binary-size budgets before retrofitting layout, linkage, and ownership boundaries becomes prohibitively expensive.
- Watch next: Compare selective thunks, hot-code reordering, large-model overhead, and decomposed services on real production workloads.
