# Windows GOG DOS Games on M-Series Macs

- Score: 134 | [HN](https://news.ycombinator.com/item?id=48356603) | Link: https://f055.net/technology/windows-gog-dos-games-on-m-series-macs/

### TL;DR
The article shows how to run Windows-only GOG DOS games (e.g., HoMM2, Settlers II) on Apple Silicon Macs by bypassing GOG’s bundled Windows DOSBox. You install the game on a Windows machine once, copy the installed files to macOS, then launch them via a custom DOSBox config and a small `.command` wrapper. The author notes vanilla DOSBox may break on future macOS versions and points to actively maintained forks, while commenters add better tools and worry about Rosetta 2’s retirement.

---

### Comment pulse
- Prefer modern DOSBox forks → DOSBox-X, Pure, and Staging offer better maintenance, features, and packaging than vanilla—counterpoint: some users just want “uninteresting” but stable emulation.  
- Avoid needing Windows → use innoextract, Wine, or 7zip to unpack GOG installers directly on macOS; launch via Boxer/Boxer-Plus or Faugus plus DOSBox-X.  
- Backwards compatibility anxiety → Rosetta 2’s deprecation may strand legacy x86 Mac games/apps even as DOSBox itself keeps running via its own CPU emulation.

---

### LLM perspective
- View: Treat GOG titles as raw assets, then script DOSBox configs; this generalizes cleanly across OS and CPU transitions.  
- Impact: Apple Silicon gamers retain access to classic DOS libraries; DOSBox forks and wrapper tools become key preservation infrastructure.  
- Watch next: Compare DOSBox forks’ performance on M-series; track Rosetta’s “gaming subset”; tools that auto-generate per-game Mac app bundles.
