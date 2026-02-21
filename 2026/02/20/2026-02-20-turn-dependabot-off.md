# Turn Dependabot Off

- Score: 194 | [HN](https://news.ycombinator.com/item?id=47094192) | Link: https://words.filippo.io/dependabot/

### TL;DR
Dependabot’s security alerts generate huge noise, especially in Go: they flag modules even when vulnerable symbols are unreachable, and push pointless upgrades. Using a recent edwards25519 bug, the author shows Dependabot opened thousands of PRs for code that never calls the affected method, even mis-scoring severity and compatibility. Instead, they recommend disabling Dependabot alerts, running govulncheck in CI for reachability-based vuln detection, and separately running daily tests against latest dependencies to surface breaking changes without constant dependency churn or alert fatigue.

---

### Comment pulse
- ReDoS alerts dominate npm Dependabot noise, often for client-only or devDependencies; many want environment-aware or dependency-scope-aware scanners — counterpoint: some argue DoS shouldn’t be treated as “security” at all.  
- Go users praise govulncheck and custom GitHub Actions that annotate PRs when vulnerable calls are added, while letting Dependabot handle only routine JS dep bumps with auto-merge.  
- Tool builders pitch smarter agents (e.g., fossabot) that use static analysis and grouped upgrades; others wish Dependabot were less email/PR-heavy and more on-demand via UI configuration.

---

### LLM perspective
- View: The core issue is not automation, but low-fidelity vulnerability matching that ignores package and symbol reachability.  
- Impact: Teams using Go, JavaScript, and similar ecosystems can markedly reduce security toil by adopting reachability-aware scanners and stricter Dependabot settings.  
- Watch next: Broader ecosystem support for symbol-level databases (like Go’s), better CI integrations, and opinionated defaults that mute non-exploitable or environment-irrelevant vulns.
