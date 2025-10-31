# NPM flooded with malicious packages downloaded more than 86k times

- Score: 127 | [HN](https://news.ycombinator.com/item?id=45755027) | Link: https://arstechnica.com/security/2025/10/npm-flooded-with-malicious-packages-downloaded-more-than-86000-times/

- TL;DR
    - Koi found “PhantomRaven,” an NPM malware campaign abusing Remote Dynamic Dependencies: install-time code fetches from untrusted URLs that evade static analysis by declaring “0 dependencies.” 126 packages saw 86k+ installs since August; payloads are served fresh (even over HTTP), enabling targeting and delayed activation to steal credentials and CI/CD secrets. HN debates NPM’s install scripts executing code, legit native-build needs, and mitigations: pnpm disabling scripts by default, containerized installs, and conservative dependency hygiene.

- Comment pulse
    - Install scripts risky → pre/postinstall run arbitrary commands, fetch remote code; native-build use cases expand attack surface; pnpm v10 disables scripts by default.
    - Sandbox npm → run installs inside containers/VMs to isolate env vars and files—counterpoint: you still execute the code; native deps complicate on macOS.
    - Practical hygiene → prefer popular, older releases; pin versions and verify checksums; wait weeks before adopting; review commits; consider OS package repos.

- LLM perspective
    - View: Attackers weaponized chatbot-suggested, non-existent package names to seed malware—developers copy-pasting from LLMs compounds supply-chain risk.
    - Impact: Expect registries and tooling to block remote dynamic dependencies, require HTTPS, and default-disable install scripts with explicit allowlists.
    - Watch next: Look for NPM policy changes, pnpm adoption metrics, SBOM+checksums enforcement, Sigstore attestations, and detection benchmarks for network-time dependency fetching.
