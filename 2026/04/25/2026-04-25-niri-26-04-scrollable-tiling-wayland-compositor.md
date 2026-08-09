# Niri 26.04: Scrollable-tiling Wayland compositor

- Score: 214 | [HN](https://news.ycombinator.com/item?id=47902416) | Link: https://github.com/niri-wm/niri/releases/tag/v26.04

### TL;DR

Niri 26.04 expands the scrollable-tiling Wayland compositor with long-requested blur, using efficient cached “xray” wallpaper blur by default and regular live-background blur when configured. Screencasting gains cursor metadata, delayed dynamic targets, status IPC, and force-stop controls; optional config includes, edge-to-edge pointer warping, IME pop-up fixes, and extensive input and rendering repairs also land. A push-based render-list refactor removes temporary allocations and measured 2–3× faster construction, reaching 8× on an old Eee PC. HN users praised the horizontal-strip model for reducing layout management and keeping task-related windows spatially adjacent.

### Comment pulse

- Traditional tilers can force pre-organization when a fourth window appears; Niri lets new windows extend right without shrinking existing ones.
- Users commonly retain workspaces per project while scrolling among editors, terminals, references, and transient tools within each.
- Mac users pointed to OmniWM’s Niri-like mode — counterpoint: commenters found its presentation weak despite usable daily behavior.

### LLM perspective

- Benchmark blur’s GPU time, power, and frame pacing across integrated, discrete, multi-GPU, and animated-wallpaper setups.
- Cast IPC enables visible recording indicators; shell adoption can turn the capability into a practical privacy safeguard.
- Optional includes improve immutable and private configurations while preserving validation when present files are malformed.
