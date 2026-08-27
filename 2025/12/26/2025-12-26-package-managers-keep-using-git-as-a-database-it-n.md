# Package managers keep using Git as a database, it never works out

- Score: 766 | [HN](https://news.ycombinator.com/item?id=46391514) | Link: https://nesbitt.io/2025/12/24/package-managers-keep-using-git-as-a-database.html

### TL;DR

Git makes an appealing package registry because it supplies free hosting, history, review, and distribution, but full-repository synchronization scales poorly for point metadata queries. Cargo, Homebrew, CocoaPods, and Go ultimately added sparse HTTP, JSON, CDNs, or proxies after users and CI absorbed large downloads and slow delta processing; vcpkg remains constrained by historical tree hashes. HN readers agree clients need efficient intermediate layers, while disputing whether Git is inherently wrong or simply a pragmatic bootstrap whose migration cost must be planned.

### Comment pulse

- User time becomes an externality → free GitHub hosting shifts bandwidth and latency costs onto every installation and CI run.
- The examples conflate architectures → registry indexing and package-source retrieval can use Git independently.
- Git remains tempting early → new managers avoid operating global infrastructure, then transition when demand justifies it.

### LLM perspective

- View: Git can remain the editorial ledger while an HTTP projection serves clients efficiently.
- Impact: Separating authoring from delivery preserves pull-request workflows without forcing users to clone registry history.
- Watch next: New registries should define migration hooks, immutable checksums, mirrors, and on-demand metadata before scale arrives.
