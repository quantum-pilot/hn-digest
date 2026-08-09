# Wine 11 rewrites how Linux runs Windows games at kernel with massive speed gains

- Score: 602 | [HN](https://news.ycombinator.com/item?id=47507150) | Link: https://www.xda-developers.com/wine-11-rewrites-linux-runs-windows-games-speed-gains/

### TL;DR

Wine 11 adds NTSYNC, a mainline-kernel driver that implements Windows-style mutexes, semaphores, events, and waits without wineserver round trips. It also completes unified WoW64 support, reducing 32-bit library hassles, and improves Wayland, graphics, media, input, Bluetooth, and game compatibility. Headline benchmarks show enormous gains over vanilla Wine, but HN commenters stress that most Linux gamers already use fsync, making typical NTSYNC improvements modest and occasionally negative. The discussion nevertheless praises Wine’s painstaking compatibility work and Valve-backed CodeWeavers investment.

### Comment pulse

- Cross-platform conformance tests and ReactOS knowledge-sharing help Wine reproduce decades of documented and undocumented Windows behavior.
- Business migration remains constrained because modern Office applications lag game compatibility.
- Some dispute fsync terminology: `futex_waitv` entered Linux 5.16 — counterpoint: upstream Wine’s original fsync path still differed.

### LLM perspective

- **View:** NTSYNC’s biggest win is correct upstream semantics with easier deployment, not universal multi-fold frame rates.
- **Impact:** Distributions and Proton can standardize synchronization while shedding patches and multilib complexity.
- **Watch next:** Official Proton adoption and fsync-controlled frametime tests across CPU-bound games and kernels.
