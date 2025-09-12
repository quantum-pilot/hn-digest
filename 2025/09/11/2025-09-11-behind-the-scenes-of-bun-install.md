# Behind the scenes of Bun Install

- Score: 313 | [HN](https://news.ycombinator.com/item?id=45210850) | Link: https://bun.com/blog/behind-the-scenes-of-bun-install

- TL;DR
  - Bun Install treats package installation as a systems problem. Written in Zig, it minimizes syscalls and locks, caches manifests in a binary format, preallocates tarball decompression, uses OS-native file copying (APFS clonefile; Linux hardlinks/COW/sendfile), and exploits lock-free, multi-core work-stealing with per-thread memory pools and 64 concurrent downloads. Reported speedups: ~7× npm, ~4× pnpm, ~17× yarn; cached installs can land in single-digit milliseconds. HN praised the clarity, while nitpicking a few claims and noting occasional ecosystem incompatibilities.

- Comment pulse
  - Performance narrative is compelling, but factual quibbles: M4 Max ≠ 2009 Top500, and '95% I/O wait' misstates server utilization; weakens trust.
  - Hardlinks vs clonefile: hardlinks share inodes, edits affect all paths—counterpoint: node_modules is read-only post-install, so sharing rarely surprises and saves I/O.
  - Adoption notes: readers praise writing and speed; some hit ecosystem gaps (crypto, Playwright). Node now bundles servers/SQLite; alternatives like Hono cited.

- LLM perspective
  - View: Treating installs as kernel-optimized, cache-aware pipelines beats event-loop architectures where syscalls, locks, and parsing dominate.
  - Impact: Package managers, build tools, and registries will adopt native paths, SoA data, COW/hardlinks, and multi-core scheduling.
  - Watch next: Cross-OS COW standardization, reproducible/secure clone semantics, compatibility matrices, real-world CI benchmarks, and fallback behavior on networked filesystems.
