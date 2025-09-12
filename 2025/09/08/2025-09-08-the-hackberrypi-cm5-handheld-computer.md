# The HackberryPi CM5 handheld computer

- Score: 243 | [HN](https://news.ycombinator.com/item?id=45172058) | Link: https://github.com/ZitaoTech/HackberryPiCM5

- TL;DR
  - The HackberryPi CM5 is a DIY handheld Linux PC built on Raspberry Pi Compute Module 5 with a reused BlackBerry keyboard. It offers a 4" 720×720 touchscreen, aluminum body, NVMe 2242, HDMI, dual USB 3.0, 5000 mAh battery (≈3–5 h), Bluetooth-paired internal speakers, and external-antenna support. HN appreciates the craftsmanship but questions Bluetooth-only audio and CM5’s lack of milliwatt deep sleep for true portability; some suggest RK3588-based designs. Clockwork uConsole appears as an alternative, amid “cool-but-drawer-bound” skepticism.

- Comment pulse
  - Bluetooth-only speakers are cursed → PWM/I2S give simpler, lower-latency audio; pairing adds failure modes — counterpoint: single BT interface prevents conflicts and matches headphone workflow.
  - CM5 lacks deep sleep → standby draw too high for pocketable uptime; RK3588 reportedly supports milliwatt sleep, making it better for handhelds.
  - Consider uConsole instead → modular, usable as a remote-terminal; trade-offs: long wait times, divisive keyboard, Radxa CM5 option lacks onboard Wi‑Fi/audio.

- LLM perspective
  - View: Clever CM5 integration and BlackBerry keyboard reuse; portability constrained by power management and a 4-inch UI.
  - Impact: Best for tinkering, field diagnostics, or secure terminals to servers; not a general-purpose mobile daily driver.
  - Watch next: Publish idle/sleep currents, audio latency comparisons (BT vs I2S), antenna performance; prototype RK3588 variant to test perf/watt and suspend.
