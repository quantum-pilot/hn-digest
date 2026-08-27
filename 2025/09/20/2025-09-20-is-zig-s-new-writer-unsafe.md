# Is Zig's new writer unsafe?

- Score: 123 | [HN](https://news.ycombinator.com/item?id=45313597) | Link: https://www.openmymind.net/Is-Zigs-New-Io-Unsafe/

### TL;DR

The author questions Zig’s new I/O interfaces after a generic function streaming a `Reader` into a buffered `Writer` fails when the writer buffer is too small for a zstd decompressor. Debug mode asserts, release mode loops indefinitely, and some inputs work, making misconfiguration conditional and hard to discover. The deeper concern is composability: callers may not know a wrapped reader’s hidden buffer requirement. HN commenters dispute whether this is undefined behavior, an ordinary bug, or merely unsafe interface design.

### Comment pulse

- The abstraction appears underspecified → generic consumers cannot reliably choose a buffer size when reader requirements are hidden through composition.
- Scope remains contested → some readers see one implementation bug rather than a general safety failure.
- Communication drew criticism → discussion faults both the blog’s limited context and the Zig creator’s dismissive response elsewhere.

### LLM perspective

- View: A documented precondition still fails composability when intermediate abstractions cannot propagate or query it.
- Impact: Library authors may inherit input-dependent hangs from components whose concrete reader type is unknown.
- Watch next: A minimal issue reproduction, explicit buffer negotiation, release-mode behavior, and revised I/O documentation.
