# Bitwarden CLI compromised in ongoing Checkmarx supply chain campaign

- Score: 611 | [HN](https://news.ycombinator.com/item?id=47876043) | Link: https://socket.dev/blog/bitwarden-cli-compromised

### TL;DR

Socket reports `@bitwarden/cli` 2026.4.0 was poisoned through Bitwarden’s GitHub Actions pipeline in the broader Checkmarx-linked campaign; other Bitwarden distributions were reportedly unaffected. Its `bw1.js` payload harvested GitHub, npm, cloud, SSH, environment, and Claude/MCP secrets, exfiltrated encrypted data, persisted through shell profiles, and propagated by republishing writable packages or injecting workflows. Affected users should remove it, rotate exposed credentials, and audit runners, repositories, publishes, cloud logs, and indicators. Readers debated whether downstream users should delay packages themselves or registries should quarantine and scan fresh releases.

### Comment pulse

- A seven-day package-age delay would have avoided this release, though universal delays could reduce the early installs that expose attacks.
- Lockfiles do not prevent risk when intentionally refreshed; automatic upgrades also deliver legitimate security fixes, so pinning trades speed for control.
- Switching ecosystems reduces some dependency exposure — counterpoint: Rust projects can still inherit large third-party trees.

### LLM perspective

- Registries should expose provenance attestations and default-deny releases whose workflow identity differs from prior trusted versions.
- CI runners need ephemeral credentials, minimal scopes, isolated homes, and egress controls to limit one poisoned build.
- Watch for confirmed exposure counts, Bitwarden’s root-cause report, fixed releases, and authoritative remediation scope.
