# Shai-Hulud compromised a dev machine and raided GitHub org access: a post-mortem

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46262021) | Link: https://trigger.dev/blog/shai-hulud-postmortem

### TL;DR

An engineer's `pnpm install` executed a compromised dependency's preinstall script, which used TruffleHog to steal credentials. An attacker then spent 17 hours cloning 669 repositories before force-pushing 199 branches across 16 repositories and closing 42 pull requests. Trigger.dev revoked access within four minutes of detection and restored branches within seven hours; branch protection blocked four pushes. Published packages and production systems showed no unauthorized access, though a discarded GitHub App key created residual uncertainty about customer repositories.

### Comment pulse

- Debate splits between blaming silent install scripts and treating dependency ecosystems themselves as an accepted security risk.
- Readers question the “not compromised” wording, plaintext-accessible credentials, absent endpoint telemetry, and organizations accumulating hundreds of repositories.

### LLM perspective

- View: Fast response limited destruction, but dormant credential access made prevention and auditability the decisive controls.
- Impact: JavaScript teams should minimize developer secrets, default-deny lifecycle scripts, and protect every meaningful branch.
- Watch next: Verify customer-access logs, endpoint-detection coverage, OIDC publishing, package-age delays, and build-script allowlists.
