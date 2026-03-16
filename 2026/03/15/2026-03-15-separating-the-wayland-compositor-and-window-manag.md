# Separating the Wayland compositor and window manager

- Score: 197 | [HN](https://news.ycombinator.com/item?id=47388137) | Link: https://isaacfreund.com/blog/river-window-management/

### TL;DR
River 0.4.0 introduces a clean split between Wayland compositor and window manager via the stable river-window-management-v1 protocol. River keeps the display server + compositor monolithic for low latency, but moves all window management policy (layouts, keybindings, decorations) into a separate process driven by a formal state machine with “manage” and “render” sequences to maintain frame-perfect updates. HN commenters see this as restoring X11-like WM pluggability, easing WM development, and addressing a long-standing Wayland architectural weakness.

---

### Comment pulse
- Decoupled WM is hailed as the missing piece in Wayland → restores X11-style WM diversity and experimentation without rewriting a compositor each time.  
- Existing users report River already strong; separation lets them build personal WMs, avoid Hyprland limitations, and switch among River, Niri, etc.  
- Some recall Wayland’s original goal of syncing WM+compositor → protocol reassures by preserving frame perfection and avoiding extra roundtrips—counterpoint: remote/rotation bugs still fuel skepticism.

---

### LLM perspective
- View: This protocol essentially standardizes a “WM as client” model for Wayland, making serious WM hacking accessible again.  
- Impact: Tiling/stacking WM authors, niche workflows, and high-level-language ecosystems gain without harming compositor latency.  
- Watch next: Adoption by other compositors, protocol extensions for exotic UIs (VR, effects), and concrete latency/robustness benchmarks vs classic monolithic designs.
