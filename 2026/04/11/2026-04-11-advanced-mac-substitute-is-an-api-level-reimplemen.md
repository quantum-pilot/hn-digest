# Advanced Mac Substitute is an API-level reimplementation of 1980s-era Mac OS

- Score: 178 | [HN](https://news.ycombinator.com/item?id=47731506) | Link: https://www.v68k.org/advanced-mac-substitute/

### TL;DR

Advanced Mac Substitute reimplements the 1980s Macintosh operating-system API so 68K applications run without Apple ROMs or system software. It emulates only the 680x0 CPU, starts directly inside an application, and separates a POSIX-compatible backend from bitmapped frontends for SDL2, macOS, X11, Linux framebuffer, and VNC. Current compatibility covers core monochrome graphics, text, windows, controls, menus, and dialogs, enough for MacPaint and several classic games. Commenters admired the compatibility challenge, saw preservation and modern-integration potential, and suggested optional period-accurate disk delays and sounds.

### Comment pulse

- Readers were surprised binary API compatibility works at all — counterpoint: many classic applications did depend on undocumented layout, timing, or behavior.
- An emulator developer wanted the lightweight environment on tiny machines with modern file sharing, avoiding ROM patching and hardware detection.
- Nostalgia extended to mechanical friction: optional floppy delays, swapping rituals, and drive noises could recreate the original experience.

### LLM perspective

- **View:** Replacing the OS API can preserve applications more cleanly than reproducing every historical machine and proprietary system image.
- **Impact:** Old productivity software and games gain portable, direct launch with host-backed documents and preferences.
- **Watch next:** Application compatibility breadth, quirk handling, native window integration, filesystem workflows, sound, networking, and CPU performance.
