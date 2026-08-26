# JavaScript engines zoo – Compare every JavaScript engine

- Score: 165 | [HN](https://news.ycombinator.com/item?id=46486978) | Link: https://zoo.js.org/

### TL;DR

The JavaScript Engines Zoo catalogs dozens of active, historical, embedded, experimental, and metacircular engines across C, C++, Rust, Java, Go, C#, and other languages. It compares benchmark scores, binary size, source lines, JIT support, ECMAScript coverage, maintenance dates, licenses, platforms, organizations, and contributors. V8 and JavaScriptCore lead its aggregate benchmark table, while smaller engines optimize for embedding, mobile, microcontrollers, WebAssembly, or language interoperability. Commenters treated results cautiously, focusing on sandbox security, surprising solo implementations, Hermes without JIT, and whether browser users notice speed differences.

### Comment pulse

- Running hostile JavaScript needs layered isolation because no complex engine can guarantee freedom from exploitable escape bugs.
- Brimstone’s one-contributor implementation and broad standards coverage impressed readers, though the table alone cannot establish production readiness.
- Benchmark gaps looked dramatic—counterpoint: many users choose browsers for stability, extensions, or compatibility rather than current engine throughput.

### LLM perspective

- View: The catalog is most valuable as an ecosystem map; a single score cannot normalize radically different targets and constraints.
- Impact: Embedders can shortlist engines by footprint, compliance, host language, maintenance, licensing, and threat model before benchmarking locally.
- Watch next: Publish reproducible hardware, flags, JIT modes, memory results, security assumptions, and workload-specific comparisons.
