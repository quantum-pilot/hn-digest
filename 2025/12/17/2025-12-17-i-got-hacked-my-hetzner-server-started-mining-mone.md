# I got hacked: My Hetzner server started mining Monero

- Score: 160 | [HN](https://news.ycombinator.com/item?id=46305585) | Link: https://blog.jakesaunders.dev/my-server-started-mining-monero-this-morning/

### TL;DR

A Hetzner abuse notice led the author to a compromised Umami analytics container running Monero miners and network scans for roughly ten days. The author attributes entry to a patched Next.js vulnerability embedded in Umami’s stack, despite not knowingly using Next.js. Because the container ran unprivileged as a non-root user with no host mounts, removing it ended the observed processes. The incident prompted firewall, SSH, monitoring, update, and container audits, though commenters caution that Docker isolation is not an absolute security boundary.

### Comment pulse

- Commenters recommend CPU, memory, and read-only limits, plus outbound controls and provider-side firewalls.
- Several dispute that a simple filesystem check proves no escape, while agreeing the configuration reduced risk.

### LLM perspective

- View: Transitive application stacks turn “unused” frameworks into operational dependencies requiring active vulnerability tracking.
- Impact: Least privilege and absent mounts sharply limited the observed blast radius, but did not prove complete containment.
- Watch next: Audit secrets, egress, Docker exposure, and persistence indicators before treating container deletion as closure.
