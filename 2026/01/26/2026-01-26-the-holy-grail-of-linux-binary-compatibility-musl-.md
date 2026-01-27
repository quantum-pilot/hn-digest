# The Holy Grail of Linux Binary Compatibility: Musl and Dlopen

- Score: 205 | [HN](https://news.ycombinator.com/item?id=46762882) | Link: https://github.com/quaadgras/graphics.gd/discussions/242

### TL;DR
This post explains how the graphics.gd maintainer reached almost “ship one Linux binary anywhere” for hardware-accelerated Go+Godot games. They patch Go to target a custom GOOS=musl, statically link Godot and the game, then reintroduce dynamic loading by hijacking the host’s dynamic linker: a tiny C helper is run, its dlopen is “stolen” back, and assembly trampolines juggle TLS so musl code can safely call glibc GPU drivers. HN discussion zooms out to libc virtualization, packaging tools, and non-libc ABI surfaces.

---

### Comment pulse
- libc virtualization via musl, Cosmopolitan, LLVM libc → goal: portable static POSIX runtime hiding syscall/ABI differences—counterpoint: may just shift complexity, not remove it.  
- People want a tool that hoovers .so dependencies → suggestions span AppImage, Nix/Guix bundles, Flatpak/Snap, Docker images, Exodus, and Cosmopolitan/APE-style fat binaries or shell-based shappimage.  
- Others note ABI isn’t just libc → IPC stacks (dbus, Wayland, varlink) and desktop runtimes also break compatibility; Valve’s Steam Runtime is a heavyweight workaround.  

---

### LLM perspective
- View: Ingenious reuse of the host dynamic linker; but the TLS-trampoline machinery is fragile and difficult to generalize.  
- Impact: Makes Go+Godot games and tools shippable as one binary across glibc/musl distros without container runtimes.  
- Watch next: broader testing on old/new kernels, GPUs, distros; extracting this hack into a reusable library or compiler backend.
