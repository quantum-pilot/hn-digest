# I found 10k GitHub repositories distributing Trojan malware

- Score: 634 | [HN](https://news.ycombinator.com/item?id=48583928) | Link: https://orchidfiles.com/github-repositories-distributing-malware/

### TL;DR

A researcher found 10,000 non-fork GitHub repositories that clone newer projects’ names, descriptions, histories, and contributor attribution, then add Trojan-bearing ZIP links through repeatedly rewritten README commits. By filtering 16 million GH Archive push events over five days to 40,000 periodically updated repositories, a script found one quarter matching the pattern; some had persisted over a year before GitHub began deleting them after publication. HN users reported similar impersonation and suggested repeated pushes keep poisoned results fresh for search engines—and possibly dependency-seeking coding agents—though that targeting remains speculative.

### Comment pulse

- Search freshness may be the mechanism → recurring force-pushes can elevate malicious clones above originals for low-volume project names and tags.

- Impersonation damages maintainers directly → developers found their names attached to unknown projects, injected links, and third-party marketplaces they did not authorize.

- Repository legitimacy is insufficient assurance → copied history and plausible code can conceal credential-stealing plugins; commenters favored source review plus self-compilation.

### LLM perspective

- **View:** Behavior-level detection exposed a campaign whose individual archive URLs evaded naive scanning; repository context is the stronger signal.

- **Impact:** New-project maintainers, niche-search users, and automated coding systems face elevated supply-chain risk from high-ranking clones.

- **Watch next:** GitHub should publish detection coverage, takedown counts, archival scanning, force-push heuristics, and protections against copied contributor attribution.
