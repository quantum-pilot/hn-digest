# Show HN: Term.everything – Run any GUI app in the terminal

- Score: 727 | [HN](https://news.ycombinator.com/item?id=45181535) | Link: https://github.com/mmulet/term.everything

TL;DR (70–90 words)
term.everything is a scratch-built Wayland compositor that renders GUI windows to your terminal, including over SSH. It downsamples to terminal rows/cols or uses terminals’ image protocols (kitty/iTerm2) for full-res, trading performance for fidelity. Written in TypeScript/Bun with some C++, it’s beta and many apps may not launch. HN readers love the delightful “useless” hack, cite remote build-machine/VDI niches where VNC is awkward, and recall Carbonyl; they’re curious about latency, bandwidth, and breadth of Wayland app support.

Comment pulse
- Joyful hack/art → boundary-pushing and fun; value is the smile more than utility.
- Remote ops niche → interact with GUIs on SSH-only build machines; avoids VNC exposure — counterpoint: latency/bandwidth and terminal protocol trust still bite.
- Comparisons/precedents → evokes Carbonyl; shows Wayland-as-library potential alongside projects like greenfield.

LLM perspective
- View: Terminal-targeted compositing unifies TUI/GUI; image-capable terminals make remote GUIs practical without full desktop remoting.
- Impact: Ops, CI, and educators gain quick ad‑hoc GUI access in constrained networks; fewer brittle ncurses clones.
- Watch next: Benchmark FPS/latency vs VNC/Waypipe; publish compatibility list; expand kitty/iTerm2 protocols; clarify security sandboxing over SSH.
