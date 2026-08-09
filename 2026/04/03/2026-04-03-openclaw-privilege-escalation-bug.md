# OpenClaw privilege-escalation bug

- Score: 218 | [HN](https://news.ycombinator.com/item?id=47628608) | Link: https://nvd.nist.gov/vuln/detail/CVE-2026-33579

### TL;DR

OpenClaw versions before 2026.3.28 contain CVE-2026-33579, a scope-validation failure in `/pair approve`. The plugin omitted caller scopes when invoking the core approval check, which failed open; a client already able to send commands with pairing/write privileges could approve a pending device request seeking `operator.admin`. The creator emphasized this was neither Telegram-specific nor a one-message remote takeover, and called practical risk low for single-user assistants. HN disputed unverified claims about publicly exposed, unauthenticated instances and recommended isolating coding agents under limited OS accounts or VMs.

### Comment pulse

- An earlier fix protected the gateway RPC path but missed the shared plugin handler, leaving authorized command senders a scope-ceiling bypass.
- Exposure estimates drew skepticism because commenters could not verify the claimed 135,000 public instances or alleged 63–65% without authentication.
- Limited macOS users preserve normal home directories while restricting secrets — counterpoint: separate Linux or macOS VMs provide stronger boundaries.

### LLM perspective

- **View:** This is an authorization-boundary failure, materially different from unauthenticated remote code execution.
- **Impact:** Shared or internet-exposed deployments face greater risk than tightly controlled, single-user installations.
- **Watch next:** Upgrade adoption, audit coverage across alternate command paths, confirmed exposure measurements, and tests that reject missing authorization context.
