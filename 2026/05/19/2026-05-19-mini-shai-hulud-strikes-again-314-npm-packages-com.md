# Mini Shai-Hulud Strikes Again: 314 npm Packages Compromised

- Score: 362 | [HN](https://news.ycombinator.com/item?id=48189368) | Link: https://safedep.io/mini-shai-hulud-strikes-again-314-npm-packages-compromised/

- TL;DR  
    - An npm maintainer account “atool” was hijacked and 637 malicious versions were pushed across 317 packages (incl. size-sensor, echarts-for-react, many @antv libs). Each added a Bun-based preinstall malware plus an optional GitHub-hosted payload via “imposter” commits in antvis/G2. The toolkit steals cloud, CI, GitHub, npm and password-manager credentials, abuses OIDC and Sigstore, and persists via GitHub Actions, VS Code/Claude hooks, systemd/LaunchAgents, and a GitHub-commit C2 channel. HN debates disabling npm lifecycle scripts, freezing dependencies, and npm’s systemic risks.

- Comment pulse  
    - Lifecycle scripts must be off by default → they’re ubiquitous RCE vectors; only few packages need them, and per-dependency opt‑in or sandboxing is feasible.  
    - npm is troubled → frequent supply-chain worms, Microsoft ownership, weak defaults; others see fewer incidents. — counterpoint: scale and popularity, not design, may explain frequency.  
    - Freeze frontend deps or add a 30‑day seasoning window → reduces exposure to fresh malware, but clashes with compliance pressure to patch every low‑risk CVE.

- LLM perspective  
    - View: Package management now equals remote code execution management, especially with AI devtools auto‑installing dependencies without user awareness.  
    - Impact: Security teams should gate npm installs via proxies, cooldown windows, and default‑off scripts, not rely on lockfiles and vulnerability scanning.  
    - Watch next: Track adoption of npm RFC 868, Sigstore verification policies, and IDE settings that decouple language servers from unsandboxed package installation.
