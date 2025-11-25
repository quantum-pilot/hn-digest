# Shai-Hulud Returns: Over 300 NPM Packages Infected

- Score: 826 | [HN](https://news.ycombinator.com/item?id=46032539) | Link: https://helixguard.ai/blog/malicious-sha1hulud-2025-11-24

TL;DR
- Attackers hijacked the NPM supply chain by pushing new versions that pretend to add Bun, adding a preinstall script that runs a 10MB obfuscated bun_environment.js. It scans for secrets with TruffleHog, exfiltrates via a self-registered GitHub Actions runner "SHA1HULUD," then republishes tainted packages using stolen tokens, seeding tens of thousands of GitHub repos. NPM artifacts diverged from GitHub sources, suggesting compromised publisher access rather than source repos. Victims (e.g., PostHog) rotated keys and republished. HN discussion centers on PNPM prompts, release cooldowns, scoped/OIDC keys, Vault, and pinning.

Comment pulse
- Adopt PNPM and cooldowns → prompts for lifecycle scripts, age-gates releases, and avoids auto-updates via lockfiles; reduces blast radius — counterpoint: slows fixes and discovery.
- Lock down publishing → scoped, IP-bound, or OIDC-issued tokens; no local keys; alarms for releases without matching CI runs mitigate account takeovers.
- Prefer deterministic installs and fewer dependencies → npm ci, hard pins, or alternative registries; the risk stems from packaging norms across ecosystems, not Node alone.

LLM perspective
- View: This is a worm using CI as an exfil channel; package-registry trust boundaries failed at token hygiene.
- Impact: Orgs with npm publishing rights are exposed; SDK vendors’ clients risk secret leakage during installs or CI runs.
- Watch next: NPM/PNPM hardening, forced script consent, registry-side anomaly detection, revocation tooling, and vendor post‑mortems with IOCs and package lists.
