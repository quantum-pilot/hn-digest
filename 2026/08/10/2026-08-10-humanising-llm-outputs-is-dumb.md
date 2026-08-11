# Humanising LLM Outputs Is Dumb

- Score: 140 | [HN](https://news.ycombinator.com/item?id=49243474) | Link: https://kuber.studio/blog/Reflections/Humanising-LLM-Outputs-is-Actually-Dumb

### TL;DR

The essay argues that telling agents to be terse, friendly, or use Simplified Technical English mixes presentation constraints into reasoning and can silently discard evidence. It proposes preserving structured, machine-facing state—test counts, failures, causes, reproductions, confidence, and provenance—through agent handoffs, then rendering accessible prose only at the human boundary. HN readers agreed that repeated summaries can hide uncertainty, but disputed whether style necessarily causes loss. Many need terseness or plain language to review work at all, and one noted Claude output styles generally do not apply to independent subagents.

### Comment pulse

- Dense LLM jargon can itself prevent oversight; retaining raw output does not eliminate the need for an understandable intermediate view.
- Style constraints are lossy — counterpoint: commenters argued complete detail and simpler language can coexist if explicitly requested.
- Preferences differ: some want impersonal engineering prose, while others find playful or empathetic tone easier and more humane.

### LLM perspective

- **View:** Separate execution records from presentation, but design both as first-class outputs rather than treating prose as cosmetic.
- **Impact:** Agents retain auditability; users receive accessible summaries without sacrificing exact failures, uncertainty, or provenance.
- **Watch next:** Typed handoff schemas, raw-artifact retention, configurable renderers, compression evaluations, and subagent-style propagation.
