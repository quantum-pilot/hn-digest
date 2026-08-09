# Claude Code is locking people out for hours

- Score: 215 | [HN](https://news.ycombinator.com/item?id=47676521) | Link: https://github.com/anthropics/claude-code/issues/44257

### TL;DR

The linked GitHub issue reports Claude Code login failing with an OAuth timeout on Windows; the HN title escalates that narrow report into users being “locked out for hours.” The discussion broadens the problem to dependency risk in subscription-based coding tools: outages, opaque usage limits, and possible capacity pressure can interrupt work without a predictable fallback. API billing offers an alternative, but commenters noted its cost can be volatile enough to erase productivity gains. Claims about shared compute pools or degraded models remain speculation, not established causes.

### Comment pulse

- Some developers now face employer pressure to use agents despite outages and weak contingency planning.
- Others report transformative productivity, making occasional disruption tolerable — counterpoint: workflow dependence raises the cost of every outage.
- Status-page watchers perceive more incidents and less diagnostic detail as adoption grows.

### LLM perspective

- **View:** The verified issue is narrower than the headline; the larger reliability concern is nevertheless credible.
- **Impact:** Agent-dependent teams need provider-independent checkpoints, local tools, and explicit degraded-mode workflows.
- **Watch next:** Anthropic’s root-cause report, Windows-specific OAuth fixes, outage frequency, and clearer quota telemetry.
