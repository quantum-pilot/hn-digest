# Trivy under attack again: Widespread GitHub Actions tag compromise secrets

- Score: 144 | [HN](https://news.ycombinator.com/item?id=47475888) | Link: https://socket.dev/blog/trivy-under-attack-again-github-actions-compromise

### TL;DR

Attackers used residual credentials from an earlier Trivy breach to force-move 75 of 76 `trivy-action` version tags onto spoofed commits whose `entrypoint.sh` stole CI secrets before running the legitimate scanner. More than 10,000 workflows reference the action; the payload scraped runner memory and filesystem credentials, encrypted them, and exfiltrated via a typosquat or a victim-owned public repository. Compromised Docker images were later identified too. HN discussion asks GitHub to enforce immutable Actions, while noting the pinning paradox: fixed hashes block tampering but also block automatic security updates.

### Comment pulse

- A non-atomic credential rotation may have exposed newly issued secrets, extending the earlier compromise instead of closing it.
- Security tools running broadly in CI create unusually attractive blast radii when their own release process fails.
- Git tags are mutable by design; changing that model for Actions would disrupt workflows, but commenters argue migration should begin.

### LLM perspective

- **View:** Treat every workflow executing a poisoned tag during exposure as compromised, not merely suspicious.
- **Impact:** Rotate reachable cloud, SSH, registry, database, Kubernetes, and package credentials; audit for fallback repositories.
- **Watch next:** Maintainer findings, tag restoration, GitHub controls, rotation timeline, and downstream breach disclosures.
