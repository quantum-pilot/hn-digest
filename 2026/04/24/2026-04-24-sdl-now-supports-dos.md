# SDL Now Supports DOS

- Score: 213 | [HN](https://news.ycombinator.com/item?id=47892291) | Link: https://github.com/libsdl-org/SDL/pull/15377

### TL;DR
SDL 3 has gained a full MS‑DOS (DJGPP) backend, adding modern SDL APIs on top of classic DOS hardware: VGA/VESA video (including banked/framebuffer modes, page‑flipping and vsync), Sound Blaster 1.x–16 audio, keyboard/mouse/joystick input, timers, and a cooperative threading layer. Audio recording and dynamic library loading are omitted for now. The PR was heavily tested in DOSBox and some real hardware, sparked nostalgia, and prompted Hacker News discussion about pre‑OS gaming (e.g., UEFI targets), SDL’s portability, and “SDL inside DOSBox inside SDL” recursion.

### Comment pulse
- Pre‑OS dream → People fantasize about SDL for UEFI so machines boot straight into a game menu, echoing bootable Amiga-era titles.
- Portability humor → Commenters joke about SDL apps on DOSBox built with SDL, plus absurd nested stacks (DOSBox in Linux in VMware in macOS).
- Maintenance lens → Inclusion of a DOS port seen as acceptable because it’s self‑contained and backed by engaged contributors likely to maintain it.

### LLM perspective
- View: This DOS backend turns SDL into a high-level, cross‑platform facade even for retro x86 machines and accurate emulators.
- Impact: Retro game devs and preservation projects can target one API across Windows, consoles, and now vintage DOS boxes.
- Watch next: Real-hardware benchmarks, sound/graphics quirks (e.g., flaky VESA implementations), and possible sibling backends for BIOS/UEFI environments.
