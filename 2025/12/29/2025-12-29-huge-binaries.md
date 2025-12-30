# Huge Binaries

- Score: 187 | [HN](https://news.ycombinator.com/item?id=46417791) | Link: https://fzakaria.com/2025/12/28/huge-binaries

### TL;DR
The post explains how enormous statically linked binaries at big companies can literally outgrow x86‑64’s default “small” code model. Direct `CALL` instructions use 32‑bit signed relative offsets, so any jump must be within ±2 GiB of the call site. When monolithic services with vast codebases and static linking push functions beyond that distance, linkers emit relocation overflow errors. Switching to `-mcmodel=large` fixes it via 64‑bit absolute calls, but bloats instructions, increases register pressure, and risks performance regressions—prompting a search for better strategies.

---

### Comment pulse
- Huge, static monoliths slow builds and deploys; infra keeps scaling instead of enforcing size limits. — counterpoint: some large, data-heavy pipelines benefit from single binaries.
- Engineers argue 2 GiB `.text` is avoidable with LTO, `--gc-sections`, and split DWARF; hitting it signals missing dead-code elimination.
- Others report 25 GB stripped binaries and real >2 GiB `.text` at FAANG, emphasizing that “problems at scale” are often dismissed until they’re painful.

---

### LLM perspective
- View: Treat code size and layout as performance-critical resources, not afterthoughts, especially in monolithic, statically linked deployments.
- Impact: Large orgs, compiler/linker authors, and build-system teams must coordinate on code models, LTO, and smarter partitioning.
- Watch next: Hybrid code models with selective far-calls, profile-guided layout beyond BOLT, and organizational limits on binary and symbol sizes.
