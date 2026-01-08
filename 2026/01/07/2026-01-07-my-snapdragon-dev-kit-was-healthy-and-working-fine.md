# My Snapdragon Dev Kit was healthy and working fine until a Windows update failed

- Score: 201 | [HN](https://news.ycombinator.com/item?id=46521860) | Link: https://jasoneckert.github.io/myblog/how-microsoft-killed-my-snapdragon-devkit/

## TL;DR
A Snapdragon X Elite Windows-on-ARM dev kit that had run flawlessly for over a year was effectively bricked after a Windows 11 security update (KB5068861) repeatedly failed, rolled back, and left the machine in an unstable boot state. Reinstall attempts now fail before completing, and even the UEFI menu is mostly unusable, with no vendor firmware-recovery path available because Qualcomm discontinued and unsupported the kit. Hacker News debates whether this is bad hardware, a botched firmware/update interaction, or the predictable risk of buying niche dev hardware.

---

## Comment pulse
- It’s almost certainly hardware (RAM, controller, etc.) → random freezes in UEFI and varying boot failure points look like flaky components, not deterministic firmware corruption — counterpoint: failure aligned exactly with the update.
- Software/firmware still suspect → KB5068861 includes UEFI patches; Windows Update has a history of bricking machines via bad BIOS/firmware and broken rollback sequences.
- Lesson about dev kits and support → Qualcomm’s ARM dev kits are seen as poorly documented, recalled, and Linux-hostile, contrasted with Nvidia Jetson’s clearer, longer-term Ubuntu support.

---

## LLM perspective
- View: Treat dev boards as experimental gear; without documented firmware recovery, any update touching low-level code is a calculated risk.
- Impact: Independent developers and small shops are most exposed; they lack fleet-scale recovery tools and vendor escalation channels.
- Watch next: Track whether OEM Snapdragon PCs ship open firmware flash tools and whether Microsoft de-couples firmware updates from routine Windows Update.
