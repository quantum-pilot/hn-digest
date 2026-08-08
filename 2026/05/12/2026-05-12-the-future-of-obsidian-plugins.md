# The Future of Obsidian Plugins

- Score: 282 | [HN](https://news.ycombinator.com/item?id=48109970) | Link: https://obsidian.md/blog/future-of-plugins/

### TL;DR

Obsidian launched a Community directory and developer dashboard for over 4,000 projects and 120 million downloads. Search, project pages, payment labels, profiles, and GitHub-based submissions replace the old flow. Every release now receives automated policy, quality, vulnerability, and malware checks; 2,300 queued submissions were processed, while humans will focus on popular, featured, or flagged projects. Scorecards, capability disclosures, verified authors, team allowlists, and private distribution are planned or expanding. HN welcomed relief from the manual-review bottleneck but doubted scanners alone can secure unrestricted Electron plugins, favoring sandboxing and enforceable permissions.

### Comment pulse

- Developers celebrated clearing 2,300 submissions after manual reviews had stalled under AI-assisted plugin growth and a seven-person team.
- Automated scans expose dependencies, CVEs, domains, and scope changes — counterpoint: false positives and obfuscated malicious updates still require expert review.
- Sandboxing and runtime permissions drew strong support because plugins can access files and network; phased API changes must preserve legacy compatibility.

### LLM perspective

- View: Continuous scanning improves visibility and queue throughput, but security needs layered enforcement rather than treating a scorecard as certification.
- Impact: Plugin authors receive faster feedback and discovery; users and enterprises gain clearer risk signals and centralized distribution controls.
- Watch next: Capability enforcement, sandbox boundaries, disclosure accuracy, false-positive rates, malicious update simulations, legacy deprecation dates, and reviewer escalation criteria.
