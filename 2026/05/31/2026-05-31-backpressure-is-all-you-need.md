# Backpressure is all you need

- Score: 132 | [HN](https://news.ycombinator.com/item?id=48345090) | Link: https://www.lucasfcosta.com/blog/backpressure-is-all-you-need

### TL;DR

Lucas Costa proposes surrounding coding agents with layered automated gates so humans review only mature changes. Each iteration must pass types, lint, tests, verification scripts, benchmarks, and agent review; later phases add real browser/API checks, visual comparison, whole-change review, and PR monitoring, with plan review before implementation. He packages the workflow as a configurable Claude skill. HN agreed such feedback loops enable longer autonomous runs, but called the idea established, questioned token cost and agent reliability, and argued these are validation gates or throttles—not backpressure tied to reviewer capacity.

### Comment pulse

- Structured orchestration already works → teams report large productivity gains from automated environments, tests, integration runs, and end-user checks — counterpoint: token costs can explode.
- The metaphor is technically wrong → proposed checks reject bad output but do not measure downstream reviewer capacity or signal producers to adjust throughput.
- Deterministic criteria deserve deterministic enforcement → hooks can block failing states reliably, avoiding an LLM forgetting instructions or rewriting tests to manufacture success.

### LLM perspective

- **View:** The durable pattern is closed-loop control: generate, measure against executable criteria, correct, then escalate only ambiguous decisions.
- **Impact:** Engineering shifts toward building testable environments and machine-readable acceptance contracts; weak specifications become the dominant bottleneck.
- **Watch next:** Cost per accepted change, false-green rates, test tampering, premature stops, and comparisons between hooks, skills, and outer loops.
