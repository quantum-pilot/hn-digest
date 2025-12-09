# GitHub Actions has a package manager, and it might be the worst

- Score: 368 | [HN](https://news.ycombinator.com/item?id=46189692) | Link: https://nesbitt.io/2025/12/06/github-actions-package-manager.html

### TL;DR
The author argues GitHub Actions is effectively a package manager, but one missing every modern supply‑chain safeguard: no lockfile, no transitive pinning, no integrity hashes, no dependency tree visibility, and undocumented resolution semantics. Mutable tags mean workflows can change without code changes; composite actions can silently pull mutable transitive dependencies; reruns aren’t reproducible. Research shows widespread vulnerabilities, and “trusted publishing” now lets these weaknesses leak into language registries. HN commenters largely agree, lamenting poor investment, awkward SHA pinning, and GHA’s dominance despite better CI options.

---

### Comment pulse
- SHA pinning exists in docs → helps direct deps but breaks on transitive deps, creates manual update burden, and doesn’t guarantee stability—counterpoint: if you distrust GitHub, bigger issues loom.
- Ecosystem under‑maintained → core setup-* actions declining, GitHub prioritizing Azure migration and AI; users pushed toward forks and workarounds.
- Despite hate, everyone uses it → free, integrated, “good enough”; some teams proudly stick with Jenkins/Ansible or explore Woodpecker and other self‑hosted CI to avoid GHA’s constraints.

---

### LLM perspective
- View: Treat Actions configs as code plus unversioned dependencies; build internal policies for vendoring and auditing critical workflows.
- Impact: Security, DevOps, and release‑engineering teams using trusted publishing are most exposed to compromised actions or mutable tags.
- Watch next: Any lockfile/registry proposal from GitHub, stronger third‑party scanners, or alternative CI ecosystems that remain Actions‑compatible but add real package management.
