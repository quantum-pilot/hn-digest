# Axios compromised on NPM – Malicious versions drop remote access trojan

- Score: 1757 | [HN](https://news.ycombinator.com/item?id=47582220) | Link: https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan

## TL;DR

Two malicious axios versions (1.14.1, 0.30.4) were pushed to npm via a hijacked maintainer account. They added a fake dependency, `plain-crypto-js@4.2.1`, whose `postinstall` script dropped a cross‑platform RAT, contacted C2 `sfrclak.com`, then wiped its own traces by replacing `package.json` with a benign stub. Any system that installed these versions should be treated as compromised. Mitigations discussed: pinning versions, `--ignore-scripts`, minimum release age, CI/network sandboxing, and reducing unnecessary dependencies like axios where fetch is available.

---

## Comment pulse

- Fewer deps / “batteries included” → attack surface shrinks, especially for core tasks (HTTP, crypto) that attract attackers — counterpoint: stdlibs lag and still need ecosystems.  
- Operational mitigations → `ignore-scripts`, minimum release age, pnpm/bun script approval help postinstall attacks — counterpoint: piling more tools atop npm’s model is itself a risk.  
- Supply-chain hygiene → use Trusted Publishing, cooldowns, and sandboxes (bwrap, firejail, containers) to limit blast radius, but account takeovers and `require()`-time attacks still bypass some layers.

---

## LLM perspective

- View: This attack shows how a single phantom dependency and `postinstall` hook can weaponize a top‑10 package without touching its code.  
- Impact: Raises bar for npm hygiene; expect more orgs to mandate `ignore-scripts` in CI, min-release-age, 2FA, and OIDC-only publishing.  
- Watch next: Registry policies for big packages (multi‑maintainer approvals, artifact attestation) and built‑in sandboxing of lifecycle scripts in mainstream package managers.
