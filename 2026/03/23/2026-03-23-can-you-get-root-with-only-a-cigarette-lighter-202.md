# Can you get root with only a cigarette lighter? (2024)

- Score: 173 | [HN](https://news.ycombinator.com/item?id=47453462) | Link: https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html

### TL;DR

A 2011 laptop gained a root shell after a piezoelectric lighter induced repeatable DDR bus bit flips through a wire soldered to one data pin. The exploit filled half of RAM with level-zero page tables, forced uncached translations, corrupted a page-table entry, then gained physical-memory read/write access and replaced the cached first page of the setuid su binary. Reliability was roughly 50% over SSH with the screen off and 20% in a graphical session, with frequent crashes. Later tests reportedly extended the technique to LPDDR4/5 and ARM.

### Comment pulse

- The lighter supplies only the electromagnetic fault → careful antenna placement, memory spraying, cache eviction, and exploit logic create privilege escalation.
- Random interference is unreliable — counterpoint: targeting a data line made one bit predictable enough for repeated exploitation.
- Follow-up work reached Switch 1 and WebKit primitives → Switch 2 memory encryption makes one flip corrupt an entire cache line.

### LLM perspective

- **View:** This is a physical fault-injection demonstration, not a remotely exploitable software vulnerability.
- **Impact:** Attackers with device access can challenge memory-isolation assumptions; consumer hardware may lack defenses against deliberate glitches.
- **Watch next:** ECC behavior, DDR4/5 variants, electronic triggering, hypervisor escape, memory encryption, and reproducibility across platforms.
