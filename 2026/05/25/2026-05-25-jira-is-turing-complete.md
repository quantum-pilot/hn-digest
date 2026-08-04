# Jira Is Turing-Complete

- Score: 291 | [HN](https://news.ycombinator.com/item?id=48263253) | Link: https://seriot.ch/computation/jira.html

### TL;DR

The article proves Jira Automation can emulate a two-counter Minsky machine: linked Bug and Task counts are registers, an Epic’s status is the program counter, and rules implement increment, decrement, branching, and transitions. A trace adds 2+3; a three-register variant emits Fibonacci numbers, although Jira Cloud’s 10-step chain cap requires manual retriggering. HN mostly turned the result into jokes, while practitioners described a split: APIs, scripts, and LLMs can automate workflows, but bespoke fields, brittle configuration, slow UI, and undocumented behavior make integration painful.

### Comment pulse

- Jira becomes leverage when automated → release hooks, changelogs, issue transitions, and audit trails can eliminate manual status work for controlled instances.
- API work is configuration-dependent → legacy migrations, undocumented magic values, custom-field coupling, and UI/API mismatches make each instance uniquely brittle.
- LLMs can absorb Jira ceremony → MCP tooling creates, decomposes, and links issues — counterpoint: generated text may worsen an already slow product.

### LLM perspective

- **View:** Turing completeness says what can be expressed under ideal resources, not that Jira is a sensible general-purpose runtime.
- **Impact:** Automation teams can model workflows as state machines, but should isolate business logic from tenant-specific Jira schema.
- **Watch next:** Test portability across Jira Cloud and Data Center, including quotas, recursion limits, failure recovery, and API consistency.
