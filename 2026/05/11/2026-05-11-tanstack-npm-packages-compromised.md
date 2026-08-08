# TanStack NPM Packages Compromised

- Score: 415 | [HN](https://news.ycombinator.com/item?id=48100706) | Link: https://github.com/TanStack/router/issues/7383

### TL;DR

TanStack npm releases were poisoned by a self-spreading supply-chain worm. Malicious versions added an optional Git dependency pointing to a hidden orphan commit; npm built it, ran its `prepare` script, then silently discarded the deliberately failed dependency. The payload stole cloud, npm, GitHub, Kubernetes, Vault, and SSH credentials, exfiltrated them over Session, and republished victims’ packages. The worm reached 200+ other packages and reportedly installed a token-revocation switch that deletes home directories. GitHub Actions OIDC publishing implicated compromised CI. HN urged exact pins, backups, manual gates, and registry-side second-factor approval.

### Comment pulse

- Trusted Publishing removes long-lived tokens but not workflow compromise — counterpoint: OIDC remains valuable when paired with manual approvals and registry-side promotion.
- npm’s handling of fork-reachable Git commits, lifecycle scripts, and optional dependency failures let the payload execute while appearing absent afterward.
- Revoking stolen tokens may trigger destructive persistence; responders prioritized forensic containment, offline backups, pinned safe versions, and coordinated credential rotation.

### LLM perspective

- View: Trusted identity proves who may publish, not artifact safety; release authorization needs an independent boundary.
- Impact: One poisoned maintainer can turn dependency installation into credential theft and recursively compromise unrelated ecosystems rapidly.
- Watch next: Full blast radius, safe-version restoration, npm/GitHub changes, provenance enforcement, lifecycle-script defaults, dead-man-switch validation, and staged-publish support.
