# GitHub Actions has a package manager, and it might be the worst

- Score: 368 | [HN](https://news.ycombinator.com/item?id=46189692) | Link: https://nesbitt.io/2025/12/06/github-actions-package-manager.html

### TL;DR

The author argues that GitHub Actions’ `uses:` mechanism functions like an informal package manager while lacking normal supply-chain controls: lockfiles, transitive pinning, integrity hashes, dependency graphs, defined resolution, offline operation, and isolation. Mutable tags can change between runs, and pinning top-level actions to SHAs does not freeze dependencies inside composite actions. GitHub offers policies, immutable releases, Dependabot, verified creators, vendoring, and external scanners, but the piece considers them incomplete—especially because Actions’ OIDC trusted publishing can place downstream package registries behind workflow security.

### Comment pulse

- SHA pinning improves reproducibility but trades automatic fixes for deliberate update work and still misses transitive actions.
- Some argue GitHub-hosted runners already imply broad trust in GitHub; third-party action mutability remains a separate risk.
- Convenience and free compute explain adoption despite recurring maintenance and ecosystem complaints.

### LLM perspective

- View: Treating workflow actions as dependencies exposes controls the platform currently leaves implicit.
- Impact: A compromised transitive action can cross from CI into trusted registry publication.
- Watch next: Native lockfiles, recursive resolution, integrity metadata, and usable automated update policy.
