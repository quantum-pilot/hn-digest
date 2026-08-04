# Potential session/cache leakage between workspace instances or consumer accounts

- Score: 267 | [HN](https://news.ycombinator.com/item?id=48785485) | Link: https://github.com/anthropics/claude-code/issues/74066

### TL;DR

A Claude Code user reported Enterprise ZDR sessions suddenly referencing an unrelated Minecraft temple, with no matching local transcript source beyond the anomalous exchange and an incidental minecraft.py filename. The user later reported another unrelated-context response in Claude Mobile, both involving Sonnet 5 after apparent cache misses. Anthropic said it was confident the behavior was hallucination but was investigating. HN debated hallucination, local context bleed, empty-context generation, and infrastructure response swapping, emphasizing that outsiders cannot distinguish these causes and that routing errors could still expose enterprise data.

### Comment pulse

- Prior incidents strengthen routing theory → a commenter described gateways shifting each response to the next caller after mishandling HTTP 100 states.
- ZDR semantics face scrutiny → data can escape during in-flight misdelivery even if providers retain nothing.
- Diagnosis remains contested → some cited random empty-prompt generations — counterpoint: repeated cache-miss timing made server-side faults harder to dismiss.

### LLM perspective

- **View:** The security problem includes observability: users lack evidence to separate model failure from data-boundary failure.
- **Impact:** Enterprise customers need incident-grade provenance for every retrieved context block and routed response.
- **Watch next:** Anthropic’s investigation should publish root cause, affected scope, and controls preventing recurrence.
