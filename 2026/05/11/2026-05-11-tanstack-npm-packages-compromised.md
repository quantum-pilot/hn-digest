# TanStack NPM Packages Compromised

- Score: 415 | [HN](https://news.ycombinator.com/item?id=48100706) | Link: https://github.com/TanStack/router/issues/7383

- TL;DR  
  - Several @tanstack/router npm packages were backdoored via a self-spreading “mini-shai-hulud” worm. The attacker slipped an optionalDependencies git reference to a malicious orphan commit; npm then ran an obfuscated prepare script that stole cloud/GitHub/npm credentials, exfiltrated them over an encrypted file-drop network, and auto-republished victims’ packages with the same payload, hitting 200+ packages across the ecosystem. Publishes came through GitHub Actions trusted publishing, implying CI/OIDC compromise. Malware also installed a destructive GitHub-token monitor on some hosts, raising alarms about postinstall scripts, npm’s trust model, and GitHub’s fork handling.

- Comment pulse  
  - Dead-man-switch malware escalates stakes → revoking stolen GitHub tokens can trigger rm -rf ~, so backups and recovery plans become non-optional.  
  - Trusted Publishing reduces token leakage, not CI compromise → attackers in your pipeline can still publish; commenters want registry-side 2FA gates on releases.  
  - npm lifecycle scripts stay risky → worm rode git deps to orphan commits; GitHub’s fork object sharing is seen as amplifying supply-chain impact.

- LLM perspective  
  - View: Supply-chain worms that autonomously republish compromised packages mark a shift from targeted backdoors to ecosystem-wide, fast-moving outbreaks.  
  - Impact: Maintainers, CI providers, and registries must coordinate on stronger publish workflows: manual approvals, hardware-backed 2FA, and least-privilege build environments.  
  - Watch next: npm limits on install scripts and release gating, plus GitHub changes to isolation, Actions permissions, and OIDC scope.
