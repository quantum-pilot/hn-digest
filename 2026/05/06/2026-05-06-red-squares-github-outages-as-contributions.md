# Red Squares – GitHub outages as contributions

- Score: 732 | [HN](https://news.ycombinator.com/item?id=48034587) | Link: https://red-squares.cian.lol/

### TL;DR

Red Squares turns GitHub’s contribution calendar into an outage heatmap: red intensity represents incident duration, totaling 32.5 service-days across 167 affected dates in the prior year, with April 30, 2026 marked worst at one day. It aggregates reconstructed GitHub Status incidents while excluding maintenance and unrated events. HN readers enjoyed the satire but challenged the metric: separate component degradations, including third-party Copilot models, may be summed and presented like platform-wide downtime. Others reported frequent workflow disruption and argued a dominant, Microsoft-owned service should meet a higher reliability bar.

### Comment pulse

- Component incident-hours are not wall-clock site outages → summing categories can exceed a day and visually exaggerate user impact.
- GitHub packages external models inside Copilot → some assign it end-to-end responsibility — counterpoint: upstream model failures are not entirely controllable.
- Weekdays appear markedly worse than weekends → commenters suspect production load or change cadence, but the chart does not isolate causes.

### LLM perspective

- **View:** The visualization is effective advocacy but a weak availability measure unless severity and affected products remain explicit.
- **Impact:** GitHub-dependent teams need local workflows and deployment paths that tolerate control-plane degradation.
- **Watch next:** Service-weighted uptime, enterprise-versus-public comparisons, independent measurements, and incident-overlap methodology.
