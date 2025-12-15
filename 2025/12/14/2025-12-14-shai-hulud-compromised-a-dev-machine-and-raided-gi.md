# Shai-Hulud compromised a dev machine and raided GitHub org access: a post-mortem

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46262021) | Link: https://trigger.dev/blog/shai-hulud-postmortem

### TL;DR
Trigger.dev was hit by the Shai-Hulud 2.0 npm supply-chain worm when a developer ran `pnpm install` on a side project. The malware used a preinstall script plus TruffleHog to steal GitHub and cloud credentials, then spent 17 hours cloning 669 repos before a 10‑minute automated vandalism spree of force-pushes and PR closures. No npm packages or production infrastructure were modified, and branches were restored within hours. They’ve since disabled npm scripts, adopted pnpm 10 safeguards, OIDC-based npm publishing, full branch protection, and tighter credential handling.

---

### Comment pulse
- Responsibility debate: some blame the npm ecosystem’s arbitrary install scripts; others argue choosing such tools is itself bad security practice—counterpoint: this happened on a dev box, not prod.
- “Not compromised” is contested: critics say any possible DB/AWS access equals breach; defenders lean on detailed audit logs showing only expected read operations.
- Many welcome pnpm’s move to block scripts by default, while others question 600+ repos and the apparent absence of EDR on developer machines.

---

### LLM perspective
- View: Supply-chain worms now assume dev machines, not prod, are the weakest link; install-time code execution is the core flaw.
- Impact: Teams relying on npm/pnpm/yarn must revisit defaults, CI publishing, and where secrets and SSO tokens are stored or cached.
- Watch next: Broader ecosystem shifts to script-blocking defaults, minimum-release-age, and OIDC-only publishing across package managers and clouds.
