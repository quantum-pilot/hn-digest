# Can LLMs model real-world systems in TLA+?

- Score: 117 | [HN](https://news.ycombinator.com/item?id=48065254) | Link: https://www.sigops.org/2026/can-llms-model-real-world-systems-in-tla/

## TL;DR

SysMoBench tests whether LLMs can genuinely model concrete systems in TLA+, instead of regurgitating textbook protocols. Across 11 real-world concurrent and distributed systems, frontier models nearly nail syntax and basic model-checker execution, but average only ~40–50% on trace conformance and safety/liveness invariants. Two recurring errors dominate: allowing states that implementations never reach and omitting states they routinely enter, often from using generic formalization templates that ignore real data structures and multi-step flows. A per-action “Transition Validation” method exposes these gaps; specialized agents like Specula currently outperform raw LLM prompting.

## Comment pulse

- Practitioners: LLMs help draft models, but struggle most with correct safety/liveness properties and state-space control; many still hand-write core specs, then use LLMs iteratively.  
- Readers question “looks passable” specs: if experts can’t easily validate a Monopoly model, how realistic is widespread formal verification—counterpoint: modeling errors, not logic, dominate bugs.  
- Some prefer proof assistants (Lean, Verus) that tie specs to executable code, avoiding model–implementation drift; others defend TLA+ for readable refinements and system-level focus.  

## LLM perspective

- Benchmarking conformance, not just syntax, should become standard for “LLM for formal methods” claims; otherwise we overestimate real modeling ability.  
- Near-term, human-led modeling plus LLM assistants/agents will beat raw models for safety-critical protocols, especially complex distributed storage and consensus.  
- Key advances to watch: automated trace generation, improved state abstraction, and reusable harnesses so new systems can be benchmarked cheaply.
