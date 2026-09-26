# Plan mode is dead

- Score: 318 | [HN](https://news.ycombinator.com/item?id=49840054) | Link: https://www.aymannadeem.com/artificial/intelligence,/developer/tools/2026/09/24/plan-mode-is-dead.html

### TL;DR

After building Nuanced around persistent AI-generated plans, the author concludes that planning remains essential but a large plan artifact is the wrong interface. Better models need fewer explicit instructions, users resist long generated specifications, and separating planning from implementation interrupts the natural loop of acting, inspecting, clarifying, and revising. The unresolved problem is human orientation: as many agents change a system, tools must surface the few decisions requiring attention and preserve understanding without demanding that people read every conversation or code change.

### Comment pulse

- Some experienced users also abandoned plan mode → they say stronger models support interactive, iterative planning inside ordinary conversation.
- Others rely on explicit plans → reviewing architecture before implementation catches underspecified intent and prevents expensive wrong turns.
- Understanding is visibly eroding → commenters fear faster output masks codebase debt and declining developer ownership.

### LLM perspective

- View: The essay rejects mandatory plan documents, not deliberate planning or human responsibility.
- Impact: Collapsing modes can reduce workflow friction while making orientation and review tooling more important.
- Watch next: Interfaces must preserve decisions, expose ambiguity, and request attention without producing another unread specification.
