# GitHub confirms breach of 3,800 repos via malicious VSCode extension

- Score: 451 | [HN](https://news.ycombinator.com/item?id=48207660) | Link: https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/

### TL;DR
GitHub says an employee’s device was compromised via a trojanized Visual Studio Code extension, allowing attackers to copy roughly 3,800 internal repositories. The malicious extension has been removed from the VS Code Marketplace, and GitHub claims no evidence (so far) of customer data exposure beyond those internal repos. Hacker group TeamPCP is trying to sell the stolen source code for at least $50,000, continuing its pattern of software supply-chain attacks through developer tooling and extension/package ecosystems.

---

### Comment pulse
- Microsoft owns VS Code, npm, GitHub, NuGet → yet cross-product security and vetting remain fragmented and weak—counterpoint: aggressive cleanup risks false positives and developer backlash.  
- Extension ecosystems are “designed-in” risk → unvetted third‑party code equals technical debt; secure orgs should favor minimal, audited tools and internal mirrors for plugins and packages.  
- Customers with private repos on GitHub → expect clear notification if affected; source exposure enables targeted exploits and long‑tail supply‑chain compromises.

---

### LLM perspective
- View: Treat editor extensions and dev tools as untrusted code; security baselines should explicitly cover IDEs, CLIs, and plugins.  
- Impact: Enterprises relying on hosted repos must re-evaluate vendor trust, internal SBOMs, and controls on what developers can install.  
- Watch next: Tighter marketplace vetting, corporate policies for “allow‑listed” extensions, and industry standards for extension signing and behavioral attestation.
