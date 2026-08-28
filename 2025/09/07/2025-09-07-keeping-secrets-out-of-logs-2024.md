# Keeping secrets out of logs (2024)

- Score: 249 | [HN](https://news.ycombinator.com/item?id=45160774) | Link: https://allan.reyes.sh/posts/keeping-secrets-out-of-logs/

### TL;DR

Keeping secrets out of logs has no single fix because sensitive data arrives through direct logging, oversized objects, configuration, embedded values, telemetry, and user input. The author proposes layered controls: centralized structured logging, data minimization and redaction, secret-aware domain types, read-once wrappers, taint analysis, safe formatters, tests, scanners, preprocessors, and trained people. Teams should map data flows, enforce controls at chokepoints, add downstream detection, and maintain an incident playbook for restriction, cleanup, recovery, and prevention.

### Comment pulse

- Readers praised the taxonomy and practical decomposition even when questioning individual techniques.
- Discussion stressed secrets embedded inside uncontrolled strings, stack traces, responses, and serialized objects as the hardest case.

### LLM perspective

- View: Treating logging as a governed data pipeline is more durable than relying on developer memory or regex alone.
- Impact: Layered prevention and detection reduce both leak probability and the time required to locate exposure.
- Watch next: Coverage gaps, side-channel log paths, scanner sampling bias, and secrets persisting in indexes or downstream stores.
