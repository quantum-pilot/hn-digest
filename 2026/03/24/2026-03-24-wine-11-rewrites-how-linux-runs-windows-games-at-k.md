# Wine 11 rewrites how Linux runs Windows games at kernel with massive speed gains

- Score: 602 | [HN](https://news.ycombinator.com/item?id=47507150) | Link: https://www.xda-developers.com/wine-11-rewrites-linux-runs-windows-games-speed-gains/

### TL;DR
Wine 11 is a major step for running Windows software on Linux, especially games. Its new NTSYNC kernel driver gives Linux native-like support for Windows synchronization primitives, removing the old wineserver bottleneck and fixing long‑standing stutter issues; worst‑offending titles can see huge FPS gains, though users already on fsync mostly get modest boosts. A completed WoW64 layer removes 32‑bit multilib hassles (even enabling many 16‑bit apps), while a maturing Wayland driver and numerous graphics, input, and ARM fixes round it out. Commenters highlight the immense, often thankless reverse‑engineering effort and Valve’s substantial funding role.

---

### Comment pulse
- Wine as heroic plumbing → decades of meticulous conformance tests, edge‑case hunting, and cross‑pollination with ReactOS; surprising that games now often work better than complex Office apps.  
- NTSYNC hype calibrated → big FPS jumps are vs vanilla Wine; fsync users usually see single‑digit gains — counterpoint: NTSYNC finally brings correctness and mainline-kernel support.  
- Funding and ecosystem → many Wine devs are paid via CodeWeavers’ Proton contract with Valve, making Windows‑to‑Linux migration and gaming far more realistic for ordinary users.

---

### LLM perspective
- View: This release reduces “Linux tax” for gaming enough that dual‑booting Windows becomes optional for many, not mandatory.  
- Impact: Native Linux ports may decline as publishers see Proton/Wine as “good enough,” shifting effort to anti‑cheat and DRM compatibility.  
- Watch next: Real‑world benches on big multiplayer titles, SteamOS/Proton rebases, and when major LTS distros ship NTSYNC-enabled kernels by default.
