# Ripgrep is faster than grep, ag, git grep, ucg, pt, sift (2016)

- Score: 328 | [HN](https://news.ycombinator.com/item?id=47499245) | Link: https://burntsushi.net/ripgrep/

### TL;DR

Ripgrep combines code-search defaults—recursive traversal, ignore-file handling, and binary/hidden-file filtering—with a fast Rust regex engine and strong Unicode support. Its 2016 benchmark suite finds it competitive across Linux-tree searches and dominant on large single files, crediting literal extraction, SIMD search, work stealing, buffered I/O for many small files, and selective memory mapping for large ones. HN readers praise the article as an enduring implementation tutorial, while debating ignore-by-default semantics and whether indexed search or newer tools win at monorepo scale.

### Comment pulse

- Competing search-tool authors cooperatively adopting a shared `.ignore` convention remains a fondly remembered HN success.
- One reader reused rarest-byte scanning with SIMD case conversion and cut their own tool’s runtime by one-third.
- Indexes can beat repeated scans at huge scale — counterpoint: building and maintaining them can dominate ordinary repositories.

### LLM perspective

- **View:** The benchmark’s lasting value is its decomposition of costs, not the raw 2016 rankings.
- **Impact:** CLI and agent-search designers can choose traversal or indexing according to workload.
- **Watch next:** Re-run current versions on cold caches, network filesystems, containers, and real monorepos.
