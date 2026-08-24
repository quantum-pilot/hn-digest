# Defeating a 40-year-old copy protection dongle

- Score: 144 | [HN](https://news.ycombinator.com/item?id=46849567) | Link: https://dmitrybrant.com/2026/02/01/defeating-a-40-year-old-copy-protection-dongle

### TL;DR

While migrating an accounting firm from four-decade-old RPG software still running under DOS on Windows 98, the author found its compiler and generated programs depended on a parallel-port dongle. Disassembly revealed a 0x90-byte routine that always returned a constant in BX. After narrowing the high byte to 0x76 and brute-forcing 256 low-byte possibilities, he found 0x7606 and replaced the check with four bytes. The patched compiler also propagated the bypass into new executables. Commenters debated whether such minimal protection was entirely adequate for its era and customers.

### Comment pulse

- Reverse engineers recognized the pattern → locating the check was harder than changing a conditional jump or fixed return value.
- Simplicity may have been rational → business customers needed deterrence, not resistance to specialists armed with modern emulators and disassemblers.
- Licensing trade-offs persist → perpetual-license dongles preserve offline control but become liabilities when hardware fails and replacements disappear.

### LLM perspective

- View: Preservation sometimes requires bypassing abandoned enforcement mechanisms before data and executable behavior can be recovered.
- Impact: The bypass enables data-migration work, while historians may gain a rare RPG II compiler after PII cleanup.
- Watch next: Verify every generated module, remove personal data, document provenance, and preserve original disk images.
