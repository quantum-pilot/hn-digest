# Making a micro Linux distro (2023)

- Score: 150 | [HN](https://news.ycombinator.com/item?id=45703556) | Link: https://popovicu.com/posts/making-a-micro-linux-distro/

### TL;DR

This beginner-oriented walkthrough builds a tiny RISC-V Linux system under QEMU to clarify the boundary between kernel and distribution. It cross-compiles Linux, observes the expected panic without a root filesystem, packages a static `/init` into a `newc` CPIO initramfs, and adds a toy shell through `fork` and `exec`. A `u-root` bonus creates a more functional Go-based userspace with common commands and networking. Along the way, the author explains process isolation, inherited file descriptors, PID 1, hardware abstraction and why package managers distinguish desktop distributions from monolithic embedded images.

### Comment pulse

- Practitioners praise initramfs as an elegant sequence of optionally compressed CPIO archives overlaid into a temporary filesystem.
- Readers share similar toy distributions and suggest real hardware, especially Raspberry Pi, as an educational next step.

### LLM perspective

- View: Constructing the smallest bootable system reveals Linux’s layers more effectively than memorizing distribution terminology.
- Impact: Kernel, initramfs and PID 1 become concrete responsibilities rather than an opaque boot sequence.
- Watch next: Device discovery, process supervision, persistent storage and updates expose where the toy becomes a maintained distribution.
