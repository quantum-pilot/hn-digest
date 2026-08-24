# Floppinux – An Embedded Linux on a Single Floppy, 2025 Edition

- Score: 231 | [HN](https://news.ycombinator.com/item?id=46866544) | Link: https://krzysztofjankowski.com/floppinux/floppinux-2025.html

### TL;DR

Floppinux 0.3.1 is a build-it-yourself Linux distribution that fits kernel, BusyBox tools, Vi, shell scripting, and persistent files onto one 1.44 MB floppy. It uses Linux 6.14.11, the last series supporting i486, targets a 486DX with 20 MB RAM, and leaves 253 KiB free. The tutorial covers cross-compilation, tiny kernel configuration, initramfs, Syslinux, QEMU, and writing physical media. Commenters celebrated the constraint-driven lesson but found practical weaknesses: obsolete application and video support, a real-486 boot failure likely involving old BIOS memory maps, and corruption-prone FAT persistence.

### Comment pulse

- Size comes from ruthless scope → 881 KiB kernel and 137 KiB compressed tools provide only terminal, file operations, Vi, and scripting.
- Real hardware exposes hidden assumptions → one 486DX2 failed despite adequate RAM, with investigation pointing toward absent E820 BIOS support.
- Writable floppy is clever → binding FAT-backed data into home preserves files — counterpoint: slow, non-journaled writes make abrupt shutdown risky.

### LLM perspective

- View: This is an excellent embedded-Linux workshop and compatibility experiment, not a credible route to modern productivity on old PCs.
- Impact: Learners see every boot layer; vintage users gain a tiny terminal but inherit fragile media and narrow hardware support.
- Watch next: Confirmed 486 boot fix, E820 fallback, persistence hardening, reproducible builds, image-size changes, drivers, and tests on period hardware.
