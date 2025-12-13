# CM0 – A new Raspberry Pi you can't buy

- Score: 157 | [HN](https://news.ycombinator.com/item?id=46244922) | Link: https://www.jeffgeerling.com/blog/2025/cm0-new-raspberry-pi-you-cant-buy

### TL;DR
Raspberry Pi quietly has a new module, the CM0: essentially a Pi Zero 2 W with 512 MB RAM, WiFi, and slow eMMC, shrunk to a postage‑stamp compute module with castellated edges for easy soldering to OEM boards. Officially it’s China‑only and mainly available via EDAtec’s CM0NANO dev board, because it competes for scarce, discontinued LPDDR2 RAM that Raspberry Pi wants to reserve for the more popular Zero 2 W. HN readers debate availability workarounds and alternative platforms for cheap, open handheld devices.

---

### Comment pulse
- “China‑only” is porous → people report buying CM0 modules on AliExpress, though supply, authenticity, and long‑term availability remain uncertain.  
- Desire: ultra‑cheap, open, battery handheld → suggestions span Allwinner tablet SoCs, Pine64 gear, ESP32 display boards, or just a cheap Android phone with Termux.  
- Castellated vs board‑to‑board → castellations simplify SMT and fixtures, while traditional CM connectors are fragile, hard to automate, and bulky—counterpoint: they were originally sold as a key feature.

---

### LLM perspective
- View: CM0 is a clear signal RPi is prioritizing industrial/OEM use over hobbyists for some SKUs, especially under RAM supply constraints.  
- Impact: Chinese OEMs gain a very compact, solderable Linux module; global makers must stick with Zero 2/CM4/5 or gray‑market CM0.  
- Watch next: whether RPi releases a CM0‑like module on newer DRAM, and if open vendors (Pine64, ESP32 ecosystem) fill this “tiny Linux SOM” niche.
