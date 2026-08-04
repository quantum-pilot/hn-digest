# I turned a $80 RK3562 Android tablet into a Debian Linux workstation

- Score: 223 | [HN](https://news.ycombinator.com/item?id=48168668) | Link: https://github.com/tech4bot/rk3562deb

### TL;DR

rkdebian turns the Doogee U10’s RK3562 hardware into a reversible Debian 12 system: boot from SD without unlocking the bootloader or modifying Android on eMMC. The reverse-engineered image supports display, touch, Wi-Fi, Bluetooth, audio, battery, USB OTG, and one NPU core; GPU acceleration and camera color remain partial. Local W8A8 tests reached 4.92 generated tokens/s with Qwen3-0.6B versus 2.18 for Qwen2.5-1.5B. Discussion centered on whether 4 GB remains useful and whether AI can make unsupported-device ports economical.

### Comment pulse

- Four gigabytes constrains browsers, Electron, YouTube, and Unity — counterpoint: others reported capable desktops, servers, media playback, and emulation without memory trouble.
- AI could make neglected hardware ports worthwhile, but practitioners demanded downstream sources, incremental changes, patch review, C knowledge, and engineering judgment.
- Availability concerns seemed premature: commenters quickly found $73–$80 listings, though attention-driven demand could still raise prices or reduce stock.

### LLM perspective

- View: The project’s real achievement is hardware enablement breadth, not raw workstation performance or its modest local-model throughput.
- Impact: Repeatable build targets and OTA packages can shift one-off reverse engineering into maintainable community support.
- Watch next: Track camera calibration, Panfrost completeness, battery-gauge reliability, and independent reproduction on additional U10 units.
