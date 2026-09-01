# Run macOS Software on Linux

- Score: 230 | [HN](https://news.ycombinator.com/item?id=49515830) | Link: https://www.darlinghq.org/

### TL;DR

Darling is a GPLv3 translation layer aiming to run macOS software directly on Linux, analogous to Wine rather than hardware emulation. It builds a Darwin environment from Apple’s open-source code plus Cocotron, Apportable, and GNUstep components, with experimental support for simple graphical applications and longer-term interest in ARM iOS apps. Commenters admire the project but stress its present limits: it targets x86-64, development appears slow, and proprietary macOS frameworks, audio systems, DRM, and complex GUI applications remain major compatibility barriers.

### Comment pulse

- Open Darwin is insufficient → many desired applications depend on proprietary frameworks that still need compatible reimplementations.
- Architecture limits matter → commenters want Apple Silicon applications on ARM Linux, while current support remains focused on x86-64.
- Professional software is distant → Logic and similar tools also require audio, MIDI, instruments, effects, and licensing infrastructure.

### LLM perspective

- View: Darling proves the translation architecture, but framework breadth determines usefulness more than basic Darwin process compatibility.
- Impact: Developers may gain access to command-line or simpler macOS tools before mainstream creative applications become practical.
- Watch next: AppKit commit velocity, ARM64 support, compatibility tests, and demonstrable GUI applications are the clearest progress signals.
