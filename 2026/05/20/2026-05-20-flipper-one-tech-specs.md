# Flipper One Tech Specs

- Score: 208 | [HN](https://news.ycombinator.com/item?id=48212046) | Link: https://docs.flipper.net/one/general/tech-specs

## TL;DR
Flipper One is a much more powerful, Linux-based handheld tool than the Flipper Zero: Rockchip RK3576 (4×A72 + 4×A53), 8 GB LPDDR5, 64 GB UFS, dual gigabit Ethernet, HDMI 2.1, Wi‑Fi 6/BT 5.2, big battery, GPIO, and an M.2 Key‑B slot for expansion (e.g., SDR, cellular). In return, it drops built‑in sub‑GHz, NFC, RFID, and IR in favor of modular radios and compliance. The low‑res grayscale MCU‑driven screen is intentional for power savings and robustness.

---

## Comment pulse
- This isn’t a Flipper Zero v2 but a pocket Linux box → huge CPU/RAM, M.2, Ethernet; great for hacking and infra tasks, less for instant RF tricks.

- Display choice questioned → fancy enclosure but tiny 6‑bit LCD; MCU owns it for watchdog and low‑power modes — counterpoint: serious UIs can go over HDMI/DisplayPort.

- Missing radios worry people → no native NFC/RFID/sub‑GHz; M.2 meant for SDR and cellular while dodging regulatory gray zones and shifting responsibility to user.

---

## LLM perspective
- View: This is essentially a rugged, battery-powered cyberdeck with opinionated UI, not a direct replacement for Flipper Zero’s “toy‑like” radio tricks.

- Impact: Most value for red-teamers, network engineers, and tinkerers wanting an always‑on Linux probe with clean expansion paths.

- Watch next: Which M.2 SDR/cellular modules get official support, real-world battery/runtime benchmarks, and whether software makes it more than a drawer gadget.
