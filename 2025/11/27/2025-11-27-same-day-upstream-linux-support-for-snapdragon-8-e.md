# Same-day upstream Linux support for Snapdragon 8 Elite Gen 5

- Score: 309 | [HN](https://news.ycombinator.com/item?id=46070668) | Link: https://www.qualcomm.com/developer/blog/2025/10/same-day-snapdragon-8-elite-gen-5-upstream-linux-support

### TL;DR

Qualcomm posted Linux patches and a bootable Debian path within a day of announcing its new mobile SoC. The proposed support spans Oryon CPU power management, storage, USB, PCIe, Wi-Fi, Bluetooth, crypto, audio, camera, video, and other controllers; display and GPU device-tree patches were still absent from mailing lists, while Vulkan required a proprietary user-mode package. Commenters welcomed earlier upstream engagement but stressed that submission is not mainlining, device trees remain product-specific, and closed boot chains, firmware, documentation, and older-chip support still limit usable systems.

### Comment pulse

- Same-day review is meaningful groundwork → hardware vendors reduce downstream-kernel debt when drivers enter community review before products proliferate.
- Upstream availability is incomplete → display and GPU pieces remain pending, and consumer devices still need board-specific device trees.
- Openness claims face skepticism → public kernel code helps — counterpoint: proprietary boot, hypervisor, firmware, and userspace layers retain vendor control.

### LLM perspective

- View: Early patch publication improves the starting line, but long-term maintenance and merge quality determine real support.
- Impact: Device makers could shorten Linux enablement while users remain dependent on OEM boot policies and complete board integration.
- Watch next: Mainline acceptance, review revisions, display and GPU submissions, firmware licensing, retail devices, and prior-generation backports.
