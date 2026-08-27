# Thoughts on Go vs. Rust vs. Zig

- Score: 151 | [HN](https://news.ycombinator.com/item?id=46153466) | Link: https://sinclairtarget.com/blog/2025/08/thoughts-on-go-vs.-rust-vs.-zig/

### TL;DR

Sinclair Target compares programming languages by values rather than feature checklists. Go chooses minimalism, stability, readability, garbage collection, and corporate collaboration, accepting boilerplate. Rust accepts conceptual density to provide memory and thread safety with high performance and expressive compile-time guarantees. Zig emphasizes explicit allocation, data-oriented design, runtime safety checks, and programmer control, but remains immature and sparsely documented. Commenters corrected specific Rust claims and debated error handling, memory exhaustion, undefined behavior, and whether Zig’s pragmatic checks can match Rust’s stronger guarantees.

### Comment pulse

- Rust advocates said mutable globals are easy when synchronization or `unsafe` accurately expresses the desired guarantees.
- Zig users valued explicit allocation failure and bounded resource planning, especially for embedded systems.
- Go’s verbosity split readers between contextual, visible errors and needless repetition that richer types could prevent.

### LLM perspective

- View: Language choice is a choice about where complexity belongs: runtime, compiler, codebase, or programmer.
- Impact: Teams should match those values to failure costs, staffing, maintenance, and resource constraints.
- Watch next: Compare equivalent production services on onboarding, defect rates, latency, memory, and long-term change cost.
