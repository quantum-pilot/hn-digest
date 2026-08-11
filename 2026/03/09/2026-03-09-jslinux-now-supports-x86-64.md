# JSLinux Now Supports x86_64

- Score: 219 | [HN](https://news.ycombinator.com/item?id=47311484) | Link: https://bellard.org/jslinux/

### TL;DR

JSLinux now offers an x86-64 Alpine Linux 3.23.2 console that runs entirely in a browser with 256 MB of emulated memory, VFsync access, and advertised AVX-512 and APX support. It joins existing x86, RISC-V, Windows 2000, FreeDOS, and graphical Linux demos. HN readers admire Fabrice Bellard’s compact technical showcase and quickly imagine browser-contained coding agents, but reported WebAssembly virtualization performance remains a concern. Others note that the new 64-bit emulation layer and build configuration are not published, pointing to v86 and container2wasm as more open alternatives.

### Comment pulse

- Browser VMs could sandbox coding agents → shell-compatible automation becomes isolated and portable, though current performance can frustrate full development loops.
- Openness is the main reservation → the x86-64 layer lacks published source and build configuration, unlike v86 or container2wasm.
- Windows 2000 drew disproportionate affection → its restrained interface remains more memorable to commenters than many modern redesigns.

### LLM perspective

- **View:** The architectural milestone is compelling, but reproducibility determines whether it becomes infrastructure or remains a demonstration.
- **Impact:** Educators, emulator enthusiasts, and agent builders gain a zero-install 64-bit Linux target inside ordinary browsers.
- **Watch next:** Source availability, execution speed, persistence semantics, networking, and reliable interfaces for programmatically driving the console.
