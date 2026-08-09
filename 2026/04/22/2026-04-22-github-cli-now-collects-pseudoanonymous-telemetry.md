# GitHub CLI now collects pseudoanonymous telemetry

- Score: 396 | [HN](https://news.ycombinator.com/item?id=47862331) | Link: https://cli.github.com/telemetry

### TL;DR

GitHub CLI now sends pseudonymous command-usage telemetry by default to guide feature prioritization. Example events include command and flag names, a persistent device ID, invocation ID, timestamp, OS, architecture, version, TTY status, and agent information—not arguments shown in the example. Users can inspect would-be payloads with `GH_TELEMETRY=log` and disable collection through CLI config, `GH_TELEMETRY=false`, or `DO_NOT_TRACK`; extension telemetry is separate. Commenters split over whether behavioral analytics improve developer tooling or constitute unnecessary surveillance, especially given timestamps, identifiers, and automated environments.

### Comment pulse

- Analytics advocates said observed use reveals abandoned or confusing features that direct feedback and developer intuition miss.
- Privacy critics accepted aggregate counts — counterpoint: stable identifiers plus timestamps may enable behavioral re-identification beyond stated product goals.
- CI and bastion users care about deterministic network behavior; optional analytics should never create hidden outbound dependencies or failures.

### LLM perspective

- Publish a versioned event schema, retention period, aggregation policy, and proof that command arguments never enter telemetry.
- Use randomized or rotating identifiers when longitudinal device tracking is unnecessary for the stated questions.
- Make first-run consent and enterprise-wide policy controls as prominent as opt-out documentation.
