# We should all be using dependency cooldowns

- Score: 257 | [HN](https://news.ycombinator.com/item?id=46005111) | Link: https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns

- TL;DR  
    - Dependency cooldowns mean intentionally delaying upgrades to new dependency releases by days/weeks, letting malicious or buggy versions be detected before adoption. The article argues this passive defense blocks most open‑source supply‑chain attacks with almost no cost, especially since many deployments are slow anyway. Tools like Dependabot/Renovate or future package‑manager features could encode cooldown rules, with urgent security advisories bypassing delays. HN debates how to balance cooldowns against zero‑day patching, organizational “zero‑CVE” mandates, dependency sprawl, and using SemVer to tune cooldown lengths.

- Comment pulse  
    - Cooldown-friendly ops → Many products release slowly; teams can monitor CVEs and rush only critical fixes—counterpoint: triage is costly and zero‑CVE policies force rapid upgrading.  
    - Slow, curated stacks → Debian‑style stable releases centralize dependency vetting and infrequent upgrades; fast‑moving ecosystems like Node lack comparable distro packaging, increasing churn and risk.  
    - Dependency hygiene → Some advocate fewer, focused dependencies and LTS libraries; others note social‑engineering risk dominates and AI makes in‑house replacements cheaper in many cases.

- LLM perspective  
    - View: Cooldowns encode “secure by default” updating, reducing exposure to freshly compromised releases without banning fast‑track patches when justified.  
    - Impact: Most valuable for ecosystems with huge transitive trees (npm, PyPI); smaller, distro‑curated stacks already gain similar protection.  
    - Watch next: Standardize package‑manager cooldown flags, CVE‑based overrides, and org policies that reward measured updates instead of naive zero‑CVE scorecards.
