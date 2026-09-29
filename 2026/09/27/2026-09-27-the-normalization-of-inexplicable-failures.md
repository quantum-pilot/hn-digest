# The Normalization of Inexplicable Failures

- Score: 276 | [HN](https://news.ycombinator.com/item?id=49867486) | Link: https://www.ihatethefuture.com/2026/09/the-normalization-of-inexplicable.html

### TL;DR

The author argues that probabilistic AI features risk normalizing failures that neither users nor builders investigate. Using Jev’s typed outputs and confidence scores as an example, he says responsible deployment still requires calibrated probabilities, domain-specific loss models, ground truth, evaluations, and accountable owners—the expensive work teams may skip while shipping. HN largely agrees that unexplained failure is corrosive, but some distinguish carefully tested agent-assisted development from careless use and note that unreliable software, opaque cloud outages, and commercial incentives long predate LLMs.

### Comment pulse

- Reliability depends on engineering discipline → tests, reproducible builds, monitoring, and rapid fixes can contain agent mistakes — counterpoint: market incentives often favor speed.
- Infrastructure magnifies tolerated uncertainty → flaky libraries, compilers, or financial systems impose costs on every downstream user.
- Confidence is not a universal grade → thresholds require measured calibration and domain-specific consequences, not intuitive percentages.

### LLM perspective

- View: Explainability matters less than preserving a traceable contract from failure to evidence, diagnosis, and accountable ownership.
- Impact: Teams adopting probabilistic components inherit evaluation and observability obligations that simple API integration conceals.
- Watch next: Demand calibration curves, abstention behavior, incident taxonomies, reproducible test sets, and error budgets tied to user harm.
