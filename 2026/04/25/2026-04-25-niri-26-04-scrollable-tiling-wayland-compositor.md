# Niri 26.04: Scrollable-tiling Wayland compositor

- Score: 214 | [HN](https://news.ycombinator.com/item?id=47902416) | Link: https://github.com/niri-wm/niri/releases/tag/v26.04

### TL;DR
Niri 26.04, a scrollable-tiling Wayland compositor, ships its most requested feature: compositor-level blur via the `ext-background-effect` protocol, including an efficient “xray” mode and fine-grained window/layer/popup rules. The release also adds optional config includes, pointer warping for smoother horizontal scrolling, and substantial screencasting upgrades (cursor metadata, dynamic target tweaks, IPC and stop-cast actions, wlr-screencopy fixes). There are numerous animation, input, and IME fixes, plus new GPU profiling via Tracy to tune heavy effects like blur.

---

### Comment pulse
- Niri as daily driver → Multiple users report long-term switching from Windows/KDE/i3/sway, praising reduced layout micro‑management and great fit with ultrawide monitors.  
- Scrollable-tiling mental model → People move from per-app fullscreen workspaces to per-project workspaces, keeping “editor+browser+terminal” visible and pushing new windows right instead of reshaping layouts.  
- macOS ecosystem → OmniWM’s “Niri mode” gives Mac users similar scrollable-tiling; widely praised as usable daily—counterpoint: its demo video is off‑putting and undersells the tool.

---

### LLM perspective
- View → Niri is turning scrollable-tiling from an experiment into a coherent UX pattern, now polished enough for mainstream dev workflows.  
- Impact → Linux power users and eventually macOS (via OmniWM) get tiling benefits without constant manual layout curation.  
- Watch next → Wider `ext-background-effect` adoption, ext-image-copy-capture support, more bars/panels consuming Niri’s screencast IPC, and benchmarks on blur/xray performance.
