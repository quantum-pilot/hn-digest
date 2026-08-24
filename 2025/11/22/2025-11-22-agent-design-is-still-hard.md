# Agent design is still hard

- Score: 333 | [HN](https://news.ycombinator.com/item?id=46013935) | Link: https://lucumr.pocoo.org/2025/11/21/agents-are-hard/

### TL;DR

An experienced agent builder argues that today’s abstractions often conceal the model-specific behavior that determines reliability. Native provider SDKs preserve control over prompt caching, message branching, tool schemas, and context editing. Practical patterns include reinforcing objectives after tool calls, isolating repeated failures in subagents, sharing a virtual filesystem, and explicitly requesting final-output tools. Model choice should reflect loop performance, not token prices alone. The hardest unresolved problem is evaluation: reproducing failures requires observing the entire evolving agent context.

### Comment pulse

- Thin custom loops beat broad SDKs → model quirks dominate once an application exceeds demos — counterpoint: vendor-native agents may outperform bespoke systems.
- Waiting can be rational → fast-changing patterns create technical debt, while building now buys learning and control.

### LLM perspective

- View: Own the orchestration layer until provider behavior becomes genuinely interchangeable.
- Impact: More control improves reliability but transfers maintenance and evaluation costs to application teams.
- Watch next: Stable cache semantics, portable tool protocols, replayable traces, and context-aware evaluation harnesses.
