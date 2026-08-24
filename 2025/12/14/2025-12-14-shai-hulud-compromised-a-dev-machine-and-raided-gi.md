# Shai-Hulud compromised a dev machine and raided GitHub org access: a post-mortem

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46262021) | Link: https://trigger.dev/blog/shai-hulud-postmortem

### TL;DR

A malicious npm dependency ran during pnpm install, used TruffleHog to steal a developer’s credentials, and enabled 17 hours of access before destruction. Trigger.dev reports 669 repository clones, 199 force-pushed branches across 16 repositories, and 42 closed pull requests. Published packages were unaffected; audits found no production-database or AWS access, while customer-repository access remained unproven but not fully excludable. Slack alerts enabled removal within four minutes and branch recovery within seven hours. Mitigations include script blocking, pnpm allowlists and release-age delays, OIDC publishing, universal branch protection, and tighter credential handling.

### Comment pulse

- Blame split between unsafe ecosystem defaults and teams choosing risky tooling; both sides supported blocking install scripts by default.
- One commenter urged assuming database compromise whenever access was possible; a counterpoint trusted AWS access logs after revocation.
- Readers questioned the repository count and whether endpoint detection was absent; others said company age can matter more than headcount.

### LLM perspective

- View: Decisive controls were blast-radius limits, visible audit signals, fast revocation, and recoverable references—not identifying one malicious package.
- Impact: A routine install exposed organization-wide credentials without infecting published packages, connecting developer endpoints to supply-chain and platform risk.
- Watch next: Customer-access logs, script-allowlist maintenance, credential rotation, protected-branch exceptions, and release-delay effectiveness.
