# Microsoft BASIC for 6502 Microprocessor – Version 1.1

- Score: 289 | [HN](https://news.ycombinator.com/item?id=45118392) | Link: https://github.com/microsoft/BASIC-M6502

- TL;DR
  - Microsoft published the complete 1976–78 source for Microsoft BASIC 1.1 for the 6502, the 8 KB, floating‑point interpreter that powered Apple II, PET, KIM‑1, and more. The code shows early multi‑platform conditional assembly and the business model that launched Microsoft. HN spots the hidden WAIT 6502,X “MICROSOFT!” easter egg, debates historically accurate Git metadata versus anachronisms, and discusses working on a single 162 kB PDP‑10‑edited source file. Retro builders cite Ben Eater’s projects as a modern way to modify and run it.

- Comment pulse
  - Hidden WAIT 6502,X easter egg → address check prints “MICROSOFT!”; a Python one‑liner reconstructs it — counterpoint: this doesn’t prove CP/M contained a similar egg.
  - Backdated Git history praised → “48 years ago” commits delight; others want accurate author, license dates, and fewer anachronisms like .md and .gitignore entries.
  - Single 162 kB source surprises → PDP‑10 TECO could handle it; timesharing, core limits, and TTY I/O affected usability and assembly times.

- LLM perspective
  - View: Beyond nostalgia, this is a masterclass in portable interpreters and conditional assembly under extreme memory constraints.
  - Impact: Enables education, exact ROM verification across Apple II/PET/KIM‑1, and grounded research on 1970s software practices and lore.
  - Watch next: Reproducible builds, byte‑for‑byte comparisons, authoritative authorship metadata, and annotated source with tests and timing benchmarks per platform.
