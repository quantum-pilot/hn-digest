# Malicious litellm_init.pth in litellm 1.82.8 PyPI package – credential stealer

- Score: 717 | [HN](https://news.ycombinator.com/item?id=47501729) | Link: https://github.com/BerriAI/litellm/issues/24512

### TL;DR

LiteLLM maintainers reported malicious litellm_init.pth credential-stealing code in PyPI releases 1.82.7 and 1.82.8, apparently connected to compromised Trivy tooling in their CI/CD and wider TeamPCP activity. PyPI quarantined downloads before both versions were deleted; GitHub, Docker, CircleCI, and PyPI keys were deleted, and maintainer accounts changed. The proxy Docker image was reportedly unaffected because its requirements were pinned. The investigation remained active, so these are provisional maintainer findings. HN treats the incident as evidence that developer dependencies need default isolation, egress controls, and credential boundaries.

### Comment pulse

- A compromised dependency can expose developer credentials → defense-in-depth should assume any dependency may be hostile.
- Sandboxed development needs VM or container isolation, allowlisted egress, seccomp-style controls, and usable violation reporting.
- Maintainer transparency drew praise — counterpoint: commenters ask why known Trivy compromise risk did not trigger earlier credential rotation.

### LLM perspective

- **View:** Deleting releases contains distribution, but exposed credentials and downstream installations require separate incident response.
- **Impact:** Users of two PyPI versions may need inventory, secret rotation, and forensic review; pinned proxy images reportedly escape exposure.
- **Watch next:** Maintainer postmortem, compromise window, package hashes, exfiltration indicators, affected download counts, account audit, and hardened release controls.
