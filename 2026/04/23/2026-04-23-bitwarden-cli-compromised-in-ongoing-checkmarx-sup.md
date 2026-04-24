# Bitwarden CLI compromised in ongoing Checkmarx supply chain campaign

- Score: 611 | [HN](https://news.ycombinator.com/item?id=47876043) | Link: https://socket.dev/blog/bitwarden-cli-compromised

- TL;DR  
Bitwarden’s npm-distributed CLI package `@bitwarden/cli@2026.4.0` was backdoored via a compromised GitHub Actions workflow, as part of the Checkmarx-style supply‑chain campaign. The injected `bw1.js` payload runs via Bun, scrapes GitHub Actions memory and config files for GitHub, cloud, npm, SSH, and MCP/Claude credentials, then exfiltrates via `audit.checkmarx.cx` and staged GitHub repos with Dune‑themed names and “LongLiveTheResistanceAgainstMachines” markers. Only the npm CLI build is affected; users should treat this as CI credential compromise, rotate secrets, and hunt for the published IOCs.

- Comment pulse  
  - Use cooldowns / minimum-release-age on package managers → slows adoption of freshly published malware. — counterpoint: registries should enforce quarantine plus automated scanning server-side.  
  - Pin dependencies for critical systems → avoids silently pulling poisoned updates via semver ranges; rely on explicit human approval for upgrades. — counterpoint: strict pinning can delay security fixes.  
  - Reduce dependence on npm and deep trees → prefer ecosystems with richer stdlibs or Rust/.NET-style stacks to shrink the trusted-author surface.

- LLM perspective  
  - View: CI pipelines and package registries are now prime targets; “build provenance” is as critical as code review.  
  - Impact: Teams using Bitwarden CLI in CI must assume leaked tokens, rebuild secrets, and verify no malicious repos/workflows were created.  
  - Watch next: Registry-level cooldowns, provenance metadata, and AI-assisted diff scanning for new releases and workflows becoming default hardening measures.
