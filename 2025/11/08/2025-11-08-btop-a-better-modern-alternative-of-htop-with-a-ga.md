# Btop: A better modern alternative of htop with a gamified interface

- Score: 185 | [HN](https://news.ycombinator.com/item?id=45856987) | Link: https://github.com/aristocratos/btop

TL;DR
btop is a cross‑platform, C++ terminal resource monitor with mouse support, themes, and a game‑inspired menu, covering CPU, memory, disks, network, and processes. Recent releases add Linux GPU monitoring (NVIDIA, AMD via ROCm SMI, basic Intel iGPU) and broader BSD support, plus static Linux binaries. It’s highly configurable, though Intel GPU and CPU wattage require setcap/setuid. HN debates the “gamified” framing, shares mixed reports on a memory‑leak issue and config‑file churn, while some praise its intuitive TUI interaction.

Comment pulse
- Title choice criticized → HN guidelines favor original; repo says “game‑inspired,” not “gamified.”
- Reports of severe memory leaks after days of uptime → issue #912 flagged — counterpoint: others report long, stable runs.
- Inline config writes clutter version‑controlled dotfiles → every tweak updates config — counterpoint: htop behaves similarly.

LLM perspective
- View: btop offers a polished TUI with GPU stats and strong ergonomics; “gamified” is a mislabel.
- Impact: Useful for ops/desktops needing quick diagnosis; attractive to users who prefer mouseable TUIs.
- Watch next: Confirm fixes for leak #912, broaden GPU metrics, ship distro builds with GPU enabled by default.
