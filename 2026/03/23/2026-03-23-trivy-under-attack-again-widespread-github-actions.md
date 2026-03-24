# Trivy under attack again: Widespread GitHub Actions tag compromise secrets

- Score: 144 | [HN](https://news.ycombinator.com/item?id=47475888) | Link: https://socket.dev/blog/trivy-under-attack-again-github-actions-compromise

### TL;DR
Attackers used a previously stolen Trivy credential to force‑update 75 of 76 tags in the official Trivy GitHub Action, turning long‑trusted version tags into delivery mechanisms for an infostealer. Any workflow using trivy-action by tag (except 0.35.0) silently executed malware before the real scan, which scraped runner memory, filesystems, and cloud/Kubernetes/crypto credentials, then exfiltrated them. The incident exposes design flaws in mutable Action tags, shows how “immutable” UI badges can mislead, and underscores CI scanners as high‑value supply‑chain targets.

---

### Comment pulse
- Immutable Actions by default → would block tag-poisoning, but commenters note the “paradox of pinning”: strict immutability conflicts with automatic security updates and developer convenience.  
- Token-rotation critique → people question how “non-atomic” secret rotation let attackers keep access, highlighting GitHub’s complex token types and awkward organization-level operations.  
- Security-tool risk → “scan everywhere” products expand attack surface; compromising one popular scanner yields huge downstream access.— counterpoint: still widely seen as necessary for visibility.

---

### LLM perspective
- View: Mutable tags plus overprivileged CI tokens create systemic risk; platform-level constraints, not just best-practice docs, are needed.  
- Impact: Affected orgs must assume credential theft, rotate CI-related secrets, and audit for tpcp-docs repos and network egress from runners.  
- Watch next: Immutable-by-default Actions, tighter runner permissions, and automated detection of tag rewrites or unsigned commits posing as old releases.
