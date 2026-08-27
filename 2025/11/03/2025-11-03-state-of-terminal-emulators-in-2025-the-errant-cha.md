# State of Terminal Emulators in 2025: The Errant Champions

- Score: 238 | [HN](https://news.ycombinator.com/item?id=45799478) | Link: https://www.jeffquast.com/post/state-of-terminal-emulation-2025/

### TL;DR

Updated `ucs-detect` tests compare terminal emulators on Unicode cell widths, grapheme behavior, DEC private modes, sixel support, pixel sizing, and automated-response speed. Ghostty scored highest, while Kitty performed comparably and publishes a text-splitting algorithm aligned with the tested `wcwidth` behavior. Several terminals were slow, inconsistent, or unable to report modes reliably. The author argues that binary Mode 2027 support reveals too little, so applications must test specific capabilities and Unicode versions. Variable-sized text could eventually improve complex-script legibility beyond fixed cells.

### Comment pulse

- Readers supplied older terminal tests and examples of hardware emulation, double-width text, and missing legacy behavior.
- Users praised Ghostty but noted gaps such as scrollback search and Windows support.

### LLM perspective

- View: Terminal compatibility is a matrix of behaviors, not a reliable product-name or mode-number lookup.
- Impact: Incorrect width assumptions corrupt both display and cursor input for multilingual command-line applications.
- Watch next: Adoption of capability queries, text-sizing protocols, and better complex-script rendering.
