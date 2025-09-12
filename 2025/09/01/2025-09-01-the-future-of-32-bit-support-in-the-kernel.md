# The future of 32-bit support in the kernel

- Score: 263 | [HN](https://news.ycombinator.com/item?id=45095475) | Link: https://lwn.net/SubscriberLink/1035727/4837b0d3dccf1cbb/

- TL;DR
  - Linux’s 32-bit era is winding down. Arnd Bergmann proposes gradual removal: desktops/servers left years ago; embedded is shifting as armv8 boards surpass armv7. Expect armv7 support ~10 years; highmem removal ~2027, nommu ~2028. Prefer 32-bit user space on 64-bit kernels; cap practical 32-bit RAM support at ≤4GB; retire niche 32‑bit arches as RISC‑V replaces them. Year‑2038 is fixed in kernel/libs, but many packages lag. HN debates nommu’s purpose, big‑endian’s fade, and compatibility for orphaned 32‑bit apps.

- Comment pulse
  - Keep nommu for hackable simplicity → empowers open, comprehensible systems — counterpoint: RTOS suits nommu; cheap MMU chips and RISC‑V make Linux-on-nommu unnecessary.
  - Big‑endian is fading → most software assumes little‑endian; only s390x/Power and networking keep it around.
  - 32‑bit apps → Wine thunks 32‑bit Windows on 64‑bit; native Linux binaries need translators; in practice, route via Wine.

- LLM perspective
  - View: Trim 32‑bit kernels; run 32‑bit userland atop 64‑bit; remove highmem/SPARSEMEM; narrow archaic arch support.
  - Impact: Kernel MM maintainers, embedded vendors, distros, and emulator/Wine projects; fewer kernel paths, clearer maintenance budgets.
  - Watch next: Densemem landing, 4G/4G experiments, deprecation schedules for legacy syscalls/armv4/early v6, highmem removal patches, BE policy tied to IBM roadmaps.
