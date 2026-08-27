# Same-day upstream Linux support for Snapdragon 8 Elite Gen 5

- Score: 309 | [HN](https://news.ycombinator.com/item?id=46070668) | Link: https://www.qualcomm.com/developer/blog/2025/10/same-day-snapdragon-8-elite-gen-5-upstream-linux-support

### TL;DR

Qualcomm posted initial Snapdragon 8 Elite Gen 5 Linux patches for review within a day of announcing the chip, alongside a public branch and Debian 13 boot instructions. Proposed support spans CPU power management, clocks, storage, USB, PCIe, connectivity, cryptography, DSPs, video, audio, camera, and display components. This is upstream intent, not completed mainline support: display and GPU device-tree patches were not yet on the mailing lists, and graphics used a separately downloadable user-mode driver and firmware. Device-specific integration also remains substantial.

### Comment pulse

- Developers welcomed the timing but cited older vendor kernels, proprietary boot chains, missing documentation, and incomplete mainlining.
- Some argued durable business incentives would support open-source work better than a temporary change in corporate attitude.

### LLM perspective

- View: Early patch publication is valuable, but acceptance and maintainability are the meaningful milestones.
- Impact: Mainline-first enablement can shorten product upgrades and reduce dependence on abandoned vendor kernels.
- Watch next: Patch acceptance, open graphics coverage, device trees, boot-chain constraints, and support for prior generations.
