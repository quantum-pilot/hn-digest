# Measuring Input Latency on Linux: X11 vs. Wayland, VRR, and DXVK

- Score: 337 | [HN](https://news.ycombinator.com/item?id=48909424) | Link: https://marco-nett.de/blog/measuring-input-latency-on-linux-x11-vs-wayland-vrr-dxvk/

### TL;DR

A homemade click-to-photon meter used a 1,000 Hz USB mouse emulator and photodiode to test Diabotical on KDE, NVIDIA, and a 500 Hz display. Across eight capped CPU-bound cases, native X11 beat native Wayland by only 0.14–0.22 ms; VRR saved 0.26–0.45 ms and reduced jitter. DXVK’s low-latency fork saved about 0.20 ms capped and 0.84 ms uncapped, while XWayland added up to 3.13 ms. HN praised measurement over folklore but cautioned that one compositor, extreme refresh rate, static scenes, and best-case conditions limit generalization to slower or real-world setups.

### Comment pulse

- Native Wayland was not the main culprit → XWayland’s compatibility path dominated measured overhead, potentially explaining older reports that Wayland feels slow.
- Refresh rate shapes interpretation → 500 Hz compresses frame-sized penalties — counterpoint: lower-rate displays may magnify VRR, pacing, or one-frame delays.
- Objective latency and subjective feel serve different questions → instrumentation diagnoses causes and competitive effects, while controlled tests may miss common degraded states.

### LLM perspective

- **View:** Optimization folklore needs end-to-end testing because individually plausible tweaks can be negligible, context-dependent, or harmful.
- **Impact:** Gamers can prioritize native display paths and VRR before chasing smaller differences among compositors, kernels, and frame pacers.
- **Watch next:** Tests at 60–240 Hz, other compositors/GPUs, GPU-bound scenes, streaming, multiple monitors, frame-time disturbances, and blind perception.
