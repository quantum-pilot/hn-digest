# Linux on the Fujitsu Lifebook U729

- Score: 159 | [HN](https://news.ycombinator.com/item?id=45937989) | Link: https://borretti.me/article/linux-on-the-fujitsu-lifebook-u729

TL;DR
- Author put NixOS on a refurbished Fujitsu Lifebook U729 (16GB/512GB, ~1.1 kg) bought for 250 AUD; everything worked OOTB. Only obstacle: Secure Boot toggle was locked. Fix: temporarily install Windows 11, apply Fujitsu drivers via Windows Update, then run DeskUpdate to upgrade BIOS (2.17→2.31), which surfaced the disable option. Also disabled Absolute Persistence in BIOS. HN: refurb enterprise laptops offer great value but mind BIOS/firmware quirks; AMD ThinkPads often outshine recent Intel; OLED/color and general Linux papercuts persist.

Comment pulse
- Used enterprise laptops are great value; check for locked BIOS and firmware update paths (some require Windows), and research repairability/OEM parts policies.
- AMD ThinkPads praised for battery/perf; recent Intel models flagged for throttling accelerometers, soldered Wi‑Fi, buggy touchpads — counterpoint: Asahi Linux on M‑series may beat both.
- Linux experience: Some report polished setups (NixOS/Hyprland), others hit "paper cuts"; OLED color issues need ICC/shader tweaks; Intel MacBook Airs work but with quirks.

LLM perspective
- View: Firmware gating features behind OEM tools complicates Linux installs; BIOS updates can unlock Secure Boot toggles and disable corporate persistence.
- Impact: Refurb buyers should expect a Windows detour for updates; choose models supported by fwupd/LVFS to avoid vendor utilities.
- Watch next: Before buying, verify BIOS version, Absolute toggle, and Linux support; live‑USB test suspend, touchpad, webcam, OLED color.
