# The Holy Grail of Linux Binary Compatibility: Musl and Dlopen

- Score: 205 | [HN](https://news.ycombinator.com/item?id=46762882) | Link: https://github.com/quaadgras/graphics.gd/discussions/242

### TL;DR

A graphics.gd maintainer is prototyping one static Linux binary that still loads each host’s accelerated graphics libraries. After patching Go for a musl target and linking Go directly into Godot, the remaining obstacle was musl’s refusal to support dynamic loading in static executables because host libc thread-local storage is incompatible. The workaround runs a small target-side C helper, borrows the system dynamic linker, and uses assembly trampolines to switch TLS around calls. A beta sample exists, but currently requires GCC and broad compatibility is unproven.

### Comment pulse

- The technique solves a narrow libc bridge → graphics APIs can load without shipping separate glibc and musl application builds.
- Universal compatibility remains broader → D-Bus, Wayland, varlink, and other userspace protocols can break despite a portable executable.
- Bundling is the conservative alternative → AppImage, Flatpak, Snap, Nix, and containers trade single-binary purity for established dependency packaging.

### LLM perspective

- View: This is an inventive dynamic-linking experiment, not yet a universal compatibility solution.
- Impact: Godot and Go developers may simplify Linux distribution if TLS switching proves safe across drivers and distributions.
- Watch next: Embedded helpers, GCC removal, architecture coverage, driver testing, IPC compatibility, crash isolation, and reproducible benchmarks.
