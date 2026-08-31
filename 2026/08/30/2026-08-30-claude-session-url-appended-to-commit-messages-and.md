# Claude Session URL appended to commit messages and PR descriptions by default

- Score: 204 | [HN](https://news.ycombinator.com/item?id=49498201) | Link: https://github.com/anthropics/claude-code/issues/66504

### TL;DR

A GitHub issue reports that Claude Code now appends a session URL to commit messages and pull-request descriptions by default, without an opt-in prompt or prominent onboarding notice. The reporter asks for explicit consent or a discoverable first-use opt-out, noting that an empty `attribution.commit` setting suppresses the addition but is hard to find. The supplied material establishes this as a user report and feature request, not an official product announcement. Discussion split between auditability benefits and concerns about advertising, durability, noise, and contextual accuracy.

### Comment pulse

- Supporters valued session links as provenance, while critics said commits should remain durable, self-contained records.
- Commenters offered configuration, environment-variable, and instruction-file workarounds, but disagreed whether defaults were sufficiently discoverable.
- Several argued a session may not accurately represent mixed human-agent work or explain the final change.

### LLM perspective

- View: Provenance is useful, but silently changing durable repository metadata is the wrong consent boundary.
- Impact: Automatic links can add audit context while creating noise, link-rot risk, and ambiguous authorship signals.
- Watch next: Whether attribution becomes opt-in, gains a first-run disclosure, or receives repository-level controls.
