# Show HN: WhatCable, a tiny menu bar app for inspecting USB-C cables

- Score: 388 | [HN](https://news.ycombinator.com/item?id=47972511) | Link: https://github.com/darrylmorley/whatcable

### TL;DR

WhatCable is an MIT-licensed macOS 14 utility translating Apple Silicon IOKit data into USB-C capabilities and charging diagnoses: e-marker speed, current, and vendor; charger profiles; negotiated wattage; devices; and transports. It offers menu-bar, Dock-window, CLI, JSON, watch, and raw modes without private APIs or helper daemons. Caveats include unmarked sub-60W cables, trusting potentially false e-markers, no Intel support, and App Store sandbox incompatibility. Hacker News praised rapid feedback-driven releases, explored Linux and KDE ports, debated menu-bar clutter, and highlighted its value for blind users unable to read hardware testers.

### Comment pulse

- Hacker News feedback produced 16 releases in seven hours, adding Dock and CLI options; the author credited Claude as a pair programmer.
- One commenter recreated the UI as a KDE widget in ten minutes, showing fast adaptation once platform data access exists.
- Software inspection helps blind users who cannot read hardware testers, but readers urged explicit VoiceOver testing.

### LLM perspective

- **View:** The strongest feature is explaining the charging bottleneck rather than dumping USB-PD fields.
- **Impact:** Clear diagnostics reduce needless cable and charger replacement while making invisible capabilities understandable.
- **Watch next:** Accessibility results, broader hardware coverage, PD 3.2 decoding, and a maintainable Linux data source.
