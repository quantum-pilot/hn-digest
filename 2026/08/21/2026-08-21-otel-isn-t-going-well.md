# OTel isn’t going well

- Score: 195 | [HN](https://news.ycombinator.com/item?id=49391553) | Link: https://matduggan.com/otel-isnt-going-well-and-i-made-a-spreadsheet-about-it/

### TL;DR

The author argues OpenTelemetry’s unfinished feel comes from a collision of stability promises, cross-language scope, and too few maintainers. A self-described hacky 24-month GitHub analysis finds many SDKs dominated by one or two mergers, while Go and .NET look healthier and Prometheus and Envoy have broader benches. Long semantic-convention debates appear less responsible than scarce reviewers and public-API gates. Proposed remedies include a usable 12-month beta tier, honest language maintenance levels, funded independent maintainers, and tolerance for communicated breaking changes. Commenters added performance, abstraction, and end-to-end complexity complaints.

### Comment pulse

- Automatic instrumentation helps initially, but users described high overhead and rigid abstractions that fail durable or unusual execution models.
- Teams wanted self-hosted “open Datadog”; replies listed existing stacks but acknowledged scaling and multiple query languages add friction.
- One annotation for logs, metrics, and traces appealed—counterpoint: their semantics, costs, storage, and processing differ fundamentally.

### LLM perspective

- View: Maintainer concentration explains slow stabilization, but repository activity cannot explain every runtime or API complaint.
- Impact: Smaller teams and weaker language ecosystems face the sharpest cost of vendor-neutral observability.
- Watch next: Funding, published maintenance tiers, beta adoption, SDK overhead benchmarks, and simpler collector distributions.
