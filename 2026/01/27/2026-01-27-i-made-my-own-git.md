# I made my own Git

- Score: 318 | [HN](https://news.ycombinator.com/item?id=46778341) | Link: https://tonystr.net/blog/git_immitation

### TL;DR

To demystify Git, the author built a small Rust version-control system called tvc. It stores file, tree, and commit objects by SHA-256 content hash, compresses them with zstd, links each commit to its parent through HEAD, and can reconstruct a snapshot into a chosen directory. The exercise showed Git’s core as a content-addressed key-value store; parsing the author’s ad hoc formats proved hardest. HN discussion expanded into merge behavior, conflict memory, educational implementations, and concerns about public code being scraped for model training.

### Comment pulse

- Reimplementation made internals tangible → readers recommended other bottom-up Git guides and build-your-own exercises for the same learning payoff.
- Merge semantics sparked debate → commenters valued preserved history and conflict reuse, while noting Git’s rerere may require explicit enablement.
- Unexpected pre-publication clones raised training concerns → the author suspected bots without proof and disclosed limited LLM-assisted research.

### LLM perspective

- View: A deliberately incomplete clone teaches object-model invariants better than memorizing porcelain commands.
- Impact: Developers gain debugging confidence, while format shortcuts illustrate why mature version-control systems invest heavily in compatibility and parsing.
- Watch next: Author identity handling, branch and merge support, robust serialization, corruption checks, and tests for checkout safety.
