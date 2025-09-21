# Is Zig's new writer unsafe?

- Score: 123 | [HN](https://news.ycombinator.com/item?id=45313597) | Link: https://www.openmymind.net/Is-Zigs-New-Io-Unsafe/

TL;DR
- The post argues Zig’s new IO can misbehave when a Writer’s buffer is smaller than what a Reader expects (e.g., zstd decompress), causing debug assertions or release hangs. Because Reader/Writer types can be dynamic or input-dependent, authors can’t reliably pick or document a buffer size, making generic piping fragile. HN leans toward “likely a bug or contract gap,” not inherent unsafety; calls for clearer negotiation/documentation. Side threads cover Zig’s value proposition and criticism of Andrew Kelley’s response elsewhere.

Comment pulse
- File a bug, not a blog post → lacks minimal reproduction, context, and proposed fix; feels like title-driven upvotes.
- Probably a bug, not systemic → but how should callers choose buffer size when Reader/Writer are dynamic? — counterpoint: smells like a contract-design gap.
- Zig positioning debate → proponents cite comptime, explicit control, tooling, C interop; critics note safety gaps and creator’s dismissive replies on Lobsters.

LLM perspective
- View: Missing negotiation of buffer granularity between stream endpoints; implicit assumptions cause UB across implementations.
- Impact: Affects codec/IO libraries and app glue code; discourages generic composition and erodes confidence in the new IO API.
- Watch next: Add trait-method to declare required chunk size, or a runtime handshake and adapter; ship tests preventing hangs on mismatch.
