# Floppinux – An Embedded Linux on a Single Floppy, 2025 Edition

- Score: 231 | [HN](https://news.ycombinator.com/item?id=46866544) | Link: https://krzysztofjankowski.com/floppinux/floppinux-2025.html

### TL;DR
A detailed “Linux From Scratch on a floppy” workshop shows how to build Floppinux 0.3.1: a 1.44 MB, i486-compatible Linux that boots from a single floppy. It uses Linux 6.14.11 (last to support 486), BusyBox 1.36.1, a musl cross‑compiler, and syslinux, producing an initramfs-based system with vi, core utilities, a simple init script, and about 250 KiB of persistent space on the floppy. HN loves the nostalgia and craft, but notes real 32‑bit hardware and persistence reliability are tricky.

---

### Comment pulse
- Retro 32‑bit boxes are CPU-capable, but lack modern 32‑bit builds and GPU drivers; browser bloat dominates—counterpoint: current Debian i386 still runs decently on late-era hardware.  
- One 486 DX2 fails to boot Floppinux; analysis blames missing BIOS E820 memory map support in syslinux’s loader, suggesting compatibility gaps with genuinely old machines.  
- Clever FAT12 persistence via bind-mounting /home onto floppy data, but risks corruption on power loss; alternatives like log-structured or tar-append schemes are proposed.

---

### LLM perspective
- View: This is an exemplary, reproducible systems-level tutorial that demystifies kernels, initramfs, bootloaders, and size tradeoffs.  
- Impact: Most useful for learners, retrocomputing hobbyists, and embedded tinkerers, not for reviving arbitrary legacy PCs.  
- Watch next: Broaden hardware testing matrix, document BIOS constraints, and experiment with safer persistence layers within the 1.44 MB budget.
