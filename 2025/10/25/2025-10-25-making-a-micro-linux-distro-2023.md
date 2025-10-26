# Making a micro Linux distro (2023)

- Score: 150 | [HN](https://news.ycombinator.com/item?id=45703556) | Link: https://popovicu.com/posts/making-a-micro-linux-distro/

- TL;DR
  - Tutorial builds a tiny Linux “distro” from scratch on QEMU’s RISC‑V: compile kernel, craft an initramfs (cpio), write a static /init in C, spawn a toy Go shell, then switch to u-root for usable tools and basic networking (virtio, DHCP, wget). Along the way it explains kernel vs distro, init’s role, and fork/exec. HN adds practical tips: initramfs can be layered by concatenated cpio archives; QEMU now supports uftrace for debugging; for speed, use Buildroot or target Raspberry Pi.

- Comment pulse
  - Initramfs layering: concatenated, optionally compressed cpio archives overlay in order → kernel unpacks to tmpfs and executes /init.
  - Debugging: recent QEMU enables uftrace on major architectures → trace early userland and syscalls to answer “how do I debug this?”
  - Bootstrap options: Buildroot speeds results; others build toy init/shell, target RPi or graphics — counterpoint: hand-rolling teaches fundamentals meta-builders hide.

- LLM perspective
  - View: Clear, reproducible path from kernel to userland with initramfs; good demo of fork/exec and u-root’s busybox-like tooling.
  - Impact: Helps embedded and RISC‑V learners prototype minimal systems; encourages static binaries and predictable boot flows.
  - Watch next: Automate builds, add uftrace benchmarks, integrate networking tests, and try on Raspberry Pi and real hardware.
