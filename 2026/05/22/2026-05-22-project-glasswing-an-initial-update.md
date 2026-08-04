# Project Glasswing: An Initial Update

- Score: 268 | [HN](https://news.ycombinator.com/item?id=48240419) | Link: https://www.anthropic.com/research/glasswing-initial-update

### TL;DR

Anthropic says Claude Mythos Preview and roughly 50 Project Glasswing partners found more than 10,000 high- or critical-severity vulnerabilities in one month. Across over 1,000 open-source projects, 1,752 flagged high/critical issues were assessed: 90.6% were real and 62.4% retained high/critical severity. Discovery now outpaces human verification, disclosure, patching, and deployment; only 75 of 530 reported high/critical bugs are patched. HN users reported strong results from AI scanners, but debated whether Mythos is a true leap, marketing, or a complement to existing static analysis.

### Comment pulse

- Continuous AI scanning feels production-ready to some teams → commenters reported roughly 90% accuracy, useful low-severity leads, and narrowly targeted fixes under 10 lines.

- Mythos’s advantage remains disputed → external evaluations suggest a step change — counterpoint: curl’s maintainer saw little improvement over prior analysis tools.

- Use layers, not replacements → linters catch cheap common flaws; AI may add business-logic, reachability, exploit, and false-positive triage capabilities.

### LLM perspective

- **View:** High precision on preselected serious findings matters, but end-to-end benefit depends on denominator, scan cost, and comparison baselines.

- **Impact:** Open-source maintainers face more credible reports and pressure, while attackers benefit from the same shrinking exploit-development costs.

- **Watch next:** Track patch completion, disclosure backlogs, independently reproduced benchmarks, report cost, maintainer burden, and safeguards before Mythos-class release.
