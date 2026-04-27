# Statecharts: hierarchical state machines

- Score: 270 | [HN](https://news.ycombinator.com/item?id=47908833) | Link: https://statecharts.dev/

### TL;DR
Statecharts extend basic state machines with hierarchy, parallelism, and well-defined semantics (via SCXML), tackling state explosion and making complex event-driven behavior easier to understand, change, and test. They can serve as both design diagrams and executable “single sources of truth,” though tooling, complexity, and type-safety remain challenges. HN discussion adds real-world stories from UI, animation, finance, and workflow systems, plus nuanced concerns about determinism and history features, and calls for tighter integration with durable execution engines.

---

### Comment pulse
- Practitioners report strong results using libraries like XState and Fulcro’s statecharts for front-end components and animations, cleaning up complex UI behavior dramatically.
- History pseudostates introduce hidden internal state, weakening the “pure function of inputs” story and demanding dedicated tests—counterpoint: that hidden pointer is just normal machine state.
- Commenters apply hierarchical state machines to blockchains and financial networks, and want statecharts married to Temporal-style workflow engines with durable, inspectable visual models.

---

### LLM perspective
- View: Use statecharts sparingly but decisively for tangled event-driven flows, not CRUD; they shine where “what happens next?” is ambiguous.
- Impact: Frontends, orchestrators, and distributed protocols gain clearer specs, fewer edge-case bugs, and diagrams non-engineers can reason about.
- Watch next: Strongly typed statechart DSLs, SCXML-compatible runtimes, and first-class integrations with workflow/durable-execution platforms and tracing/monitoring stacks.
