# A friendly tour of process memory on Linux

- Score: 187 | [HN](https://news.ycombinator.com/item?id=45805539) | Link: https://www.0xkato.xyz/linux-process-memory/

- TL;DR
    - Clear, hands-on tour of Linux x86‑64 process memory: VMAs define regions; pages materialize on first touch; file vs anonymous mappings; CoW for fork/MAP_PRIVATE; mprotect enforces W^X and triggers TLB invalidations; THP/mTHP boost TLB efficiency with latency tradeoffs; /proc tools expose per‑page reality; PTI mitigates Meltdown by switching page tables. HN praised the “tiny explainers,” some disliked the LLM‑ish tone, and a side thread debated hardware simplicity vs modern complexity; a few hit false .xyz domain blocks.

- Comment pulse
    - Tiny explainers improve comprehension → readers appreciate confirmations and pacing — counterpoint: LLM‑like phrasing (“without the fog”) feels inauthentic.
    - Prefer simpler, non‑VM designs → reduce complexity/security fallout — counterpoint: VM predates 6502; complexity bought isolation, performance, and multiprogramming.
    - Site blocked as unsafe → corporate filters often distrust .xyz TLDs; likely a false positive.

- LLM perspective
    - View: Design for demand paging: batch touches, avoid accidental CoW, minimize permission flips.
    - Impact: JITs/DBs/hypervisors: tune THP/mTHP, RW→RX transitions, and dirty‑tracking with userfaultfd+PAGEMAP_SCAN.
    - Watch next: mTHP defaults, PTI/PCID tuning, benchmark TLB shootdowns and huge‑page compaction latency.
