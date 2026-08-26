# Drone Hacking Part 1: Dumping Firmware and Bruteforcing ECC

- Score: 129 | [HN](https://news.ycombinator.com/item?id=46654749) | Link: https://neodyme.io/en/blog/drone_hacking_part_1/

### TL;DR

Researchers extracted firmware from a Potensic Atom 2 by desoldering its 4Gb SPI NAND and reading 131,072 pages with an ESP32. Noisy wiring caused random flips, so three dumps were majority-voted; entropy analysis and the SoC datasheet then revealed interleaved user, control, bad-block, and parity regions. They inferred a 16-bit-per-1KB BCH scheme, brute-forced polynomial 17475 plus bit-reversal and inversion transforms in 22 seconds, corrected 247,134 bits, and recovered usable UBIFS files. HN applauded the reproducible hardware work, documentation lessons, and approachable error-correction explanation.

### Comment pulse

- Documentation becomes legible after experiments → the SoC’s “16-bit” clue only mattered once observed flash layout supplied context.
- ECC means error-correction codes here → readers found the electronics approachable, despite expecting elliptic-curve cryptography.
- Linux raised compliance questions → some demand stronger enforcement — counterpoint: unmodified kernels only require source availability upon request.

### LLM perspective

- View: The decisive skill was converting messy physical evidence into testable storage-format hypotheses.
- Impact: A corrected firmware image enables deeper analysis of update encryption, backdoors, and remote-control vulnerabilities.
- Watch next: Review Part 2 for exploitability, disclosure outcomes, firmware-decryption details, and vendor remediation.
