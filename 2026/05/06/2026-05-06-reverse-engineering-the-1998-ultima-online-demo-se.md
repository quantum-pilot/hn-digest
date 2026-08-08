# Reverse-engineering the 1998 Ultima Online demo server

- Score: 224 | [HN](https://news.ycombinator.com/item?id=48032976) | Link: https://draxinar.github.io/articles/2026-05-01-uodemo-reverse-engineering.html

### TL;DR

After a decade of intermittent work, Draxinar released a portable C99 reconstruction of the 1998 Ultima Online demo server: roughly 5,000 MSVC x86 functions translated by hand and checked instruction-by-instruction against the binary. The demo contained much of the live production server, enabling restoration of disabled spawning, decay, and predator-prey systems, plus reconstructed world data, 64-bit support, accounts, and clients through 2007. LLMs helped finish the project, though the methodology remained manual and binary-grounded. HN readers celebrated both game preservation and UO’s enduring role in launching programming careers.

### Comment pulse

- Matching recompiled functions against original instructions constrains decompilation → intentional bug fixes and platform adaptations remain explicitly tagged.
- Missing historical save, region, and resource files limit fidelity → the author requests archives and can strip player data before release.
- UO’s private-server ecosystem taught scripting and networking → several commenters traced professional careers to childhood shard projects.

### LLM perspective

- **View:** This is executable archaeology: preserve behavior, document deviations, and recover design intent from artifacts.
- **Impact:** Researchers and players gain inspectable server internals instead of depending on aging binaries or approximate emulators.
- **Watch next:** Archival file recovery, netcode validation, reproducible builds, expanded process documentation, and community testing.
