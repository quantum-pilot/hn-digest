# VitruvianOS – Desktop Linux Inspired by the BeOS

- Score: 324 | [HN](https://news.ycombinator.com/item?id=47512816) | Link: https://v-os.dev

### TL;DR

VitruvianOS combines Linux hardware support with a tightly integrated desktop inspired by BeOS and Haiku. Its custom Nexus kernel subsystem supplies BeOS-style node monitoring, device tracking, and messaging so Haiku applications can run with few or no API changes. The distribution ships real-time kernel patches, supports XFS and SquashFS extended attributes, and promises sensible defaults, privacy, and low latency; indexing, live queries, and graphical multiuser login remain planned. HN saw a potentially tractable compatibility-layer strategy, though some preferred running Haiku directly.

### Comment pulse

- BeOS veterans remembered exceptional speed and polish, alongside a recurring pattern of beloved Amiga, WebOS, BB10, and Windows Phone platforms dying.
- Haiku supporters favored the native successor — counterpoint: Vitruvian aims to pair the same stack with Linux’s broader hardware ecosystem.
- Technically minded readers asked why syscall translation lives in a kernel module instead of Linux’s user-space Syscall User Dispatch mechanism.

### LLM perspective

- **View:** Linux underneath and BeOS semantics above is a focused compromise between compatibility and driver coverage.
- **Impact:** Dedicated users could gain Haiku applications without surrendering modern device support.
- **Watch next:** Application compatibility rates, indexing delivery, latency benchmarks, hardware coverage, and maintenance burden of Nexus.
