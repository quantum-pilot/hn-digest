# Package managers keep using Git as a database, it never works out

- Score: 766 | [HN](https://news.ycombinator.com/item?id=46391514) | Link: https://nesbitt.io/2025/12/24/package-managers-keep-using-git-as-a-database.html

## TL;DR
Many package managers initially store their package index in a Git repo because it’s free, familiar, and comes with history and PR workflows. As ecosystems grow, cloning and delta resolution become unbearably slow, especially in CI, and can even strain GitHub itself. Rust’s Cargo, Homebrew, CocoaPods, Nixpkgs, and Go modules all had to bolt on HTTP/CDN-based sparse metadata services or proxies. The root issue: Git and filesystems are optimized for source trees, not fast, constrained metadata queries.

## Comment pulse
- Git-as-registry shifts costs to users and GitHub: slow updates, huge downloads, CI waste—counterpoint: some consumer products already track and optimize user-facing latency heavily.
- Commenters note maintainers pick Git for free hosting and simplicity; debate whether “do easy thing, fix later” is pragmatic bootstrap or unethical debt.
- Some argue the article conflates using Git for metadata with fetching source via Git; suggest object access plus HTTP caches instead of working trees.

## LLM perspective
- View: Treat Git as an append-only publication log; front it with purpose-built HTTP or database services for discovery and installs.
- Impact: Designing for sparse, per-package metadata queries early reduces CI time, bandwidth, and operational surprises as ecosystems and fork networks grow.
- Watch next: Document migration playbooks from Git registries to HTTP/CDN-backed indices, including checksum schemes, mirrors, and governance for community-run infrastructure.
