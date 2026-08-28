# Uncertain<T>

- Score: 448 | [HN](https://news.ycombinator.com/item?id=45054703) | Link: https://nshipster.com/uncertainty/

### TL;DR

NSHipster ports the research idea `Uncertain<T>` to Swift, representing measurements as probability distributions rather than prematurely collapsing them into ordinary values or booleans. Operations build a computation graph; sampling occurs when a concrete probability or statistic is requested, with sequential testing controlling effort. Examples cover GPS proximity, speed, drag, latency, and expected slot-machine payout. The library supports several distributions and statistical operations, but sampling costs require profiling. The author recommends incremental adoption where real measurement noise already causes user-visible errors.

### Comment pulse

- Readers warned that GPS error is often non-circular, especially under multipath effects.
- Discussion explored covariance, particle filters, probabilistic programming, automatic differentiation, and related hardware research.
- One reader said reused leaf samples can preserve covariance within the library’s sampling model.

### LLM perspective

- View: Encoding uncertainty in types makes hidden modeling assumptions reviewable and composable.
- Impact: Better probability handling can prevent brittle thresholds and implausibly precise user-facing decisions.
- Watch next: Verify distribution fit, covariance behavior, calibration, and sampling cost against real sensor data.
