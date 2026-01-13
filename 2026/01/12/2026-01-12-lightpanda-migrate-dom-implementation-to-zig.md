# Lightpanda migrate DOM implementation to Zig

- Score: 180 | [HN](https://news.ycombinator.com/item?id=46586179) | Link: https://lightpanda.io/blog/posts/migrating-our-dom-to-zig

### TL;DR
Lightpanda replaced its LibDOM-based HTML DOM with zigdom, a custom Zig implementation sitting directly under V8. The move fixes architectural friction around events, Custom Elements, and Shadow DOM, gives tighter control over memory via pointer unions and pooled allocations, and enables lazy per-element state for modest performance gains. They kept parsing in Rust via html5ever and sped startup with V8 snapshots. HN debates Zig vs Rust ergonomics and safety, Zig’s pre-1.0 stability, and Lightpanda’s focused headless-browser scope.

### Comment pulse
- Zig for DOM over Rust → manual memory better matches shared mutable graphs than Rc<RefCell>—counterpoint: Rust arenas can model DOM similarly while preserving compile-time safety.  
- Zig in production is risky → pre-1.0 with stdlib churn, especially I/O; supporters say language core is stable and migrations are quick.  
- Lightpanda’s scope → headless net+DOM+JS (no CSS/layout/paint); used as JS-capable text/Markdown fetcher, praised as more capable than lynx/links.  

### LLM perspective
- View: Rewriting a core subsystem mainly for cohesion, not raw speed, is rational when abstractions impede spec compliance and future features.  
- Impact: If zigdom proves robust, others building specialized browsers, crawlers, or testing tools may adopt similar Zig-first stacks over mixed-language architectures.  
- Watch next: Worth tracking real-world crash stats, memory usage under pathological pages, and how well AI-assisted development scales to less well-specified domains.
