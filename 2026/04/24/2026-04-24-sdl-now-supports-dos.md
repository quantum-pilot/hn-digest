# SDL Now Supports DOS

- Score: 213 | [HN](https://news.ycombinator.com/item?id=47892291) | Link: https://github.com/libsdl-org/SDL/pull/15377

### TL;DR

SDL 3 merged a 53-commit DJGPP port that brings its cross-platform API to DOS. The backend covers VGA/VESA 1.2+ video with indexed color and page flipping, Sound Blaster playback, keyboard, mouse, joystick, cooperative threading, PIT timing, filesystem fallbacks, CMake cross-compilation, and CI. Audio recording and shared-library loading remain absent; automation still has formatting failures, and hardware coverage is limited despite successful DOSBox, DevilutionX, Quake, and one DOS 6.22/Vortex86 test. Hacker News celebrated the recursive spectacle of SDL software testing SDL-in-DOSBox and wondered about FreeBASIC, direct-boot games, UEFI, and long-term maintainership.

### Comment pulse

- DOSBox itself uses SDL, making the port’s primary test environment an amusingly recursive compatibility stack.
- UEFI could enable pre-OS games — counterpoint: missing sound drivers and absent vsync information make it worse than DOS-era hardware interfaces.
- Merging a niche backend depends on limited invasiveness and contributors remaining available to maintain it across SDL changes.

### LLM perspective

- **View:** A modern compatibility layer converts retro-platform support from a bespoke engine problem into a reusable backend problem.
- **Impact:** Existing SDL games and language bindings gain a plausible route to 386-class DOS targets with fewer platform-specific rewrites.
- **Watch next:** Real-hardware matrices, Nvidia page-flip controls, remaining test failures, audio recording, FreeBASIC integration, and maintainer continuity.
