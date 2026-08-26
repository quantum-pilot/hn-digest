# Lightpanda migrate DOM implementation to Zig

- Score: 180 | [HN](https://news.ycombinator.com/item?id=46586179) | Link: https://lightpanda.io/blog/posts/migrating-our-dom-to-zig

### TL;DR

Lightpanda replaced LibDOM with zigdom, an in-house Zig DOM eliminating friction among V8, events, Custom Elements, Shadow DOM, and memory management. Pointer-based tagged unions, combined allocations, and lazy property storage underpin it; html5ever handles parsing and V8 snapshots reduce startup work. Performance improved by single-digit percentages, but cohesion and extensibility were the main gains. Claude helped implement it, though reviewing large changes was difficult. HN debated Zig versus Rust for mutable DOM graphs, pre-1.0 production risk, and Lightpanda’s script-only tradeoffs.

### Comment pulse

- Zig models graph relationships directly → supporters prefer manual arenas over Rust ownership friction — counterpoint: weaker guarantees permit use-after-free errors.
- Pre-1.0 Zig worries production users → repeated standard-library changes impose migrations, though practitioners report manageable upgrade costs.
- Lightpanda is deliberately incomplete → executing JavaScript without style, layout, or painting enables speed but limits screenshot-dependent debugging.

### LLM perspective

- View: Replacing LibDOM is an organizational architecture choice more than a benchmark-driven rewrite.
- Impact: One cohesive implementation should accelerate compatibility work while concentrating memory-safety responsibility inside Lightpanda’s team.
- Watch next: Track web-platform conformance, memory failures, Zig upgrade costs, startup benchmarks, and support for layout-dependent pages.
