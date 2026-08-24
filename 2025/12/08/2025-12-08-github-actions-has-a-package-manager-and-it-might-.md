# GitHub Actions has a package manager, and it might be the worst

- Score: 368 | [HN](https://news.ycombinator.com/item?id=46189692) | Link: https://nesbitt.io/2025/12/06/github-actions-package-manager.html

### TL;DR

The author argues GitHub Actions functions as a package manager without baseline supply-chain controls: no lockfile, transitive pinning, integrity hashes, dependency-tree view, documented resolution semantics, registry, or offline mode. Mutable tags and opaque composite-action dependencies make identical workflow reruns execute different code; pinning a top-level SHA cannot constrain nested references. GitHub offers immutable releases, SHA policies, verified-creator restrictions, and Dependabot, but rejected lockfile support. Commenters largely agree the ecosystem is under-maintained, while noting SHA pinning trades automatic fixes for manual update work.

### Comment pulse

- SHA pinning only approximates a lockfile → nested mutable dependencies remain uncontrolled, and pinned actions can age out of supported runtimes.
- Convenience sustains adoption despite frustration → free, integrated compute outweighs complaints for many teams; others retain Jenkins or test locally.
- Trust boundaries differ → hosted-runner users already trust GitHub, but action publishers still need reproducible, inspectable dependency trees.

### LLM perspective

- View: Workflow dependencies deserve the same reproducibility contract as application dependencies.
- Impact: Maintainers must audit composite actions manually or accept silent supply-chain drift.
- Watch next: Native transitive lockfiles, integrity enforcement, immutable metadata, and dependency graph tooling.
