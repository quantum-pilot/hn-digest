# Thoughts on slowing the fuck down

- Score: 614 | [HN](https://news.ycombinator.com/item?id=47517539) | Link: https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down/

### TL;DR

A coding-agent builder argues that autonomous swarms can compress years of codebase decay into weeks. Agents repeatedly introduce errors, optimize locally with incomplete search recall, and generate complexity faster than humans can review or feel its delayed costs; even their tests may become untrustworthy. He recommends bounded tasks with closed evaluation loops, noncritical outputs, and humans as final gates. Architecture and APIs should remain human-led, while generated code stays within review capacity. HN reframed the issue as matching tools and process to what is being built.

### Comment pulse

- Readers feared agent-only comprehensibility creates vendor lock-in — counterpoint: cheaper hardware and smaller coding models may preserve provider competition.
- Veteran operators said software was always flawed; automation changes failure frequency unless teams enforce learning, error budgets, and Andon-style stops.
- The author’s own Pi framework strengthened the critique by showing it came from an agent practitioner, not an outside skeptic.

### LLM perspective

- **View:** Generation speed is useful only when verification, understanding, and organizational learning scale with it.
- **Impact:** Teams may ship fewer features while retaining maintainability, incident response ability, and bargaining power.
- **Watch next:** Defect density, review throughput, rollback frequency, model spending, and long-term change latency.
