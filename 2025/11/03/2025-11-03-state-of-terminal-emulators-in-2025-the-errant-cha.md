# State of Terminal Emulators in 2025: The Errant Champions

- Score: 238 | [HN](https://news.ycombinator.com/item?id=45799478) | Link: https://www.jeffquast.com/post/state-of-terminal-emulation-2025/

- TL;DR
  - Jeff Quast updates ucs-detect to probe Unicode width, DEC modes, sixel, window size and versions, then ranks terminals by correctness and speed. Ghostty (Zig) and Kitty top the charts, the only ones handling Variation Selector 15; many VTE-based terminals lag and some (iTerm2, Extraterm) are very slow. DEC mode reporting is inconsistent across apps; Mode 2027 is a weak proxy. He argues for variable-sized text (Kitty’s text sizing protocol) to improve legibility. HN discusses real VT emulation, VT100 double‑wide support, Ghostty adoption, and font-coverage queries.

- Comment pulse
  - Use MAME for authentic VT102/VT220 emulation via TCP+agetty; fun alternative to modern emulators with ideas like mouse/paste support.
  - Ghostty praised as faster, nicer Alacritty; missing scrollback search and Windows port. Alacritty’s long-standing ligature gap pushes users over — counterpoint: theme pickers are commonplace.
  - Developers want a way to query font coverage per terminal to fallback when characters (e.g., legacy symbols, private-use icons) aren’t rendered.

- LLM perspective
  - View: Converge on shared width engines (wcwidth spec, libghostty) plus runtime probes; stop relying on vague DEC modes.
  - Impact: TUI toolkits can use richer Unicode confidently; lagging VTE-based terminals face user churn and distro defaults scrutiny.
  - Watch next: libghostty release, Kitty text sizing experiments, a lightweight font-coverage query, and measurable VTE emoji-sequence support in stable builds.
