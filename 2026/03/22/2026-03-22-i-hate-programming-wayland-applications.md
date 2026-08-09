# I hate: Programming Wayland applications

- Score: 159 | [HN](https://news.ycombinator.com/item?id=47478298) | Link: https://www.p4m.dev/posts/29/index.html

### TL;DR

A developer who enjoys Wayland as a user describes direct client programming as excessively fragmented and callback-heavy. Creating even a software-rendered window requires registry discovery, generated protocol bindings, multiple surface objects, shared-memory buffers, configure callbacks, frame callbacks, and careful dispatch ordering; input repetition, clipboard, hotplugging, screen capture, cursors, and monitor data add more extensions or compositor-specific behavior. HN agreed documentation and cross-compositor gaps hurt, but split on the diagnosis: critics called the low-level API hostile, while defenders said applications should use mature toolkits or wrappers.

### Comment pulse

- Direct API critics want a standard middle layer for windows, input, and clipboard — counterpoint: defenders say low-level asynchrony preserves toolkit flexibility.
- Cross-compositor gaps compound complexity → desktop-state access, portals, hotplugging, monitor geometry, and automation lack consistent behavior.
- Even experienced users found dispatch semantics poorly documented → one reply explained queues, flushes, round trips, EGL interaction, and timeout handling.

### LLM perspective

- **View:** The strongest complaint is not verbosity alone, but the missing portable layer between raw protocol and full GUI toolkit.
- **Impact:** Small native applications either absorb large integration costs, add dependencies, or inherit inconsistent compositor behavior.
- **Watch next:** Protocol standardization, documentation improvements, lightweight client libraries, and adoption of faster-moving extensions.
