# Malicious versions of Nx and some supporting plugins were published

- Score: 443 | [HN](https://news.ycombinator.com/item?id=45034496) | Link: https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c

- TL;DR
  - Attackers abused a flawed GitHub Actions workflow in Nx (bash injection + pull_request_target) to exfiltrate an npm token and publish malicious nx and plugin releases. Their postinstall scanned for plaintext secrets and pushed encoded loot to s1ngularity-repository repos under victims’ GitHub accounts; shells were booby‑trapped to prompt sudo shutdown. Nx Console for VSCode auto‑installed nx@latest, widening exposure. Nrwl pulled releases, rotated secrets, and moved to Trusted Publishers. HN debates: disable install scripts/sandbox installs, cut dependencies or vet them, and demand ecosystem-level signing/MFA and better OS isolation.

- Comment pulse
  - Disable npm lifecycle scripts; sandbox installers → blocks postinstall malware; use ignore-scripts, bubblewrap/Docker, or pnpm whitelisting — counterpoint: runtime scripts can still execute malicious code.
  - Shrink dependency surface or vet transitive trees → fewer unreviewed updates; simple features can be in-house; cargo-vet-style attestations help at scale.
  - Ecosystem fixes needed → signing, MFA, heuristics, ephemeral tokens, Trusted Publishers; also isolate dev work in VMs/containers to limit blast radius.

- LLM perspective
  - View: CI workflows are powerful attack surfaces; avoid pull_request_target, sanitize inputs, and gate secrets by environment and branch.
  - Impact: Expect orgs to tighten IDE extensions and agent permissions; default-deny auto-installs, no auto-updates with credentials, stronger token lifetimes.
  - Watch next: Adoption of npm Trusted Publishers, provenance/signing, and GitHub policy changes on GITHUB_TOKEN scopes; vendor advisories for VSCode extensions.
