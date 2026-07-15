# Measuring Input Latency on Linux: X11 vs. Wayland, VRR, and DXVK

- Score: 337 | [HN](https://news.ycombinator.com/item?id=48909424) | Link: https://marco-nett.de/blog/measuring-input-latency-on-linux-x11-vs-wayland-vrr-dxvk/

### TL;DR
The author built a “click-to-photon” device (USB mouse emulator + light sensor) to measure true end-to-end gaming latency on Linux. On a 500 Hz QD‑OLED with an RTX 4070 and Diabotical via Proton/DXVK, native X11 and native Wayland are effectively tied: X11 is only 0.14–0.22 ms faster. The big levers are VRR (0.26–0.45 ms faster, less jitter), the DXVK low-latency fork (up to −0.84 ms uncapped), and avoiding XWayland, which adds ~3 ms and dominates other effects.

---

### Comment pulse
- Linux is great for this kind of deep measurement → open stack, data can feed upstream improvements — counterpoint: desktop complexity, theming, and UX regressions frustrate users.
- Measured differences (except XWayland) are sub‑millisecond → many doubt humans can feel them; real pain likely on slower displays or poorly tuned stacks.
- Perceived “Wayland slowness” likely from XWayland and compositor differences → need tests across more compositors, refresh rates, and real-world fluctuating workloads.

---

### LLM perspective
- View: Treat “Wayland feels off” as a measurement problem; this kind of hardware-based benchmarking should become standard in gaming discussions.
- Impact: Competitive gamers, Proton/DXVK maintainers, and compositor authors get concrete targets: kill XWayland lag, optimize VRR paths, refine frame pacing.
- Watch next: Repeat tests at 60–240 Hz, on AMD + Intel GPUs, across GNOME/Hyprland/Gamescope, and under fluctuating in-game workloads.
