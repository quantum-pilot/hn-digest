# Package managers keep using Git as a database, it never works out

- Score: 653 | [HN](https://news.ycombinator.com/item?id=46391514) | Link: https://nesbitt.io/2025/12/24/package-managers-keep-using-git-as-a-database.html

- TL;DR  
Many package managers initially used a single git repo as their package index because GitHub is free, familiar, and has built‑in reviews. At scale, this approach collapses: huge repos, delta resolution, shallow‑clone hacks, CI timeouts, and even GitHub infrastructure strain. Systems like Cargo, Homebrew, CocoaPods, Nix, and Go have all migrated toward HTTP APIs, CDNs, and databases for fast, partial metadata lookups, leaving git only as a publishing or coordination mechanism. vcpkg remains painfully stuck.

- Comment pulse  
  - GitHub’s free hosting and PR UX encourage git registries → maintainers ignore user bandwidth/time externalities — counterpoint: some teams track latency and optimize it.  
  - For new package managers, a proper registry seems unaffordable → git becomes the shortcut; critics label this unethical “fuck around and find out” tech debt.  
  - Some argue git can back an index if clients use HTTP caches/sparse access → others insist git is always a poor database and supply‑chain liability.

- LLM perspective  
  - View: Git is fine as authoritative source-of-truth; the mistake is forcing every client to speak git instead of HTTP.  
  - Impact: Better designs separate concerns: git for human collaboration, append‑only DB or blob store for machine queries, aggressively cached behind CDNs.  
  - Watch next: Expect new package managers to start on git for bootstrapping, but plan migration paths to HTTP/DB‑backed indexes from day one.
