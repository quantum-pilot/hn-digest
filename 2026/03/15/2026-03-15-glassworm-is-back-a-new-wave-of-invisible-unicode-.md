# Glassworm Is Back: A New Wave of Invisible Unicode Attacks Hits Repositories

- Score: 205 | [HN](https://news.ycombinator.com/item?id=47387047) | Link: https://www.aikido.dev/blog/glassworm-returns-unicode-attack-github-npm-vscode

### TL;DR
Aikido reports a new Glassworm campaign hiding JavaScript malware inside “empty” template strings using invisible Unicode code points, decoded and executed via `eval()`. At least 150+ GitHub repositories and several npm packages and a VS Code extension were silently compromised in early March 2026. Attackers likely use LLMs to generate realistic cover commits (docs tweaks, refactors) so reviews miss the payload. Defenders need automated Unicode-aware scanning and stricter policies, not just eyeballing code, sparking debate on GitHub’s responsibility and maintainers’ diligence.

---

### Comment pulse
- Git hosting should scan for non-standard zero-width characters like they do secrets → invisible attacks violate platform’s obligation to make PR risk visible to maintainers.  
- GitHub advertises Unicode warnings but they miss these cases → bug-bounty report was validated yet deemed low priority, undermining confidence in current protections.  
- Some blame maintainers for merging `eval` + opaque transforms; others note force-push hijacks, volunteer overload, and advocate ASCII-only codebases with hooks to shrink attack surface.

---

### LLM perspective
- View: LLMs mainly amplify old tricks—obfuscation and `eval`—by scaling tailored, believable commits across many projects.  
- Impact: Any ecosystem with open contributions and JavaScript build chains is now a realistic target for automated supply-chain poisoning.  
- Watch next: Native IDE/review support to visualize/control Unicode, repo-level ASCII policies, and benchmarkable Unicode-masked malware detections in CI.
