# Unusual circuits in the Intel 386's standard cell logic

- Score: 208 | [HN](https://news.ycombinator.com/item?id=46020543) | Link: https://www.righto.com/2025/11/unusual-386-standard-cell-circuits.html

### TL;DR

Die-level reverse engineering shows how Intel used standard cells and automated placement and routing to rescue the schedule of its 285,000-transistor 386. Register selection required unusually large multiplexers built from CMOS transmission switches. One PMOS transistor sits outside the regular cell columns, plausibly a hand-added bug fix that avoided rerunning expensive mainframe layout. Other cells resembling inverters actually separate their NMOS and PMOS gates, adding selectable high, low, or disconnected cases. These physical exceptions reveal how early automation coexisted with manual optimization and interpretation.

### Comment pulse

- Transmission-gate terminology refined the analysis → commenters noted these CMOS switches avoid hazards and often use buffers to restore drive.
- Tooling history fascinated readers → Unix, Timberwolf, proprietary routing, and an IBM mainframe let engineers automate work despite management constraints.
- Ahead-of-schedule claims drew skepticism → early steppings had bugs. — counterpoint: cited records measured architecture-to-production and unusually fast tapeout.

### LLM perspective

- View: The anomalous transistor is a bug-fix hypothesis, while the fake inverters are directly evidenced by layout.
- Impact: Standard-cell automation accelerated a foundational processor while preserving enough flexibility for local manual repairs and unconventional cell reuse.
- Watch next: Completion of the register-control reconstruction, evidence for the patch theory, and comparisons with later synthesized x86 designs.
