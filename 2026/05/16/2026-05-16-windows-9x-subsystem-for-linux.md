# Windows 9x Subsystem for Linux

- Score: 212 | [HN](https://news.ycombinator.com/item?id=48120162) | Link: https://codeberg.org/hails/wsl9x

### TL;DR
WSL9x is a hobby project that embeds a modern Linux 6.19 kernel directly inside the Windows 9x kernel, so both OSes run cooperatively on the same machine without rebooting or full virtualization. It uses a custom VxD driver to load and manage Linux in ring 0, a heavily modified user‑mode Linux tree that talks to Win9x kernel APIs, and a tiny 16‑bit DOS client to turn standard DOS prompts into Linux terminals. GPL‑3 licensed and very low‑level.

---

### LLM perspective
- View: This is a deep, educational example of low-level OS interop, not a general-purpose compatibility layer.
- Impact: Retrocomputing, OS-dev learners, and emulator authors gain a concrete reference for Win9x internals and cooperative kernels.
- Watch next: Performance benchmarks, device/FS support expansion, and documentation of Win9x API quirks uncovered by the port.
