# Tested: How Many Times Can a DVD±RW Be Rewritten? Methodology and Results

- Score: 237 | [HN](https://news.ycombinator.com/item?id=47296568) | Link: https://goughlui.com/2026/03/07/tested-how-many-times-can-a-dvd%C2%B1rw-be-rewritten-part-2-methodology-results/

### TL;DR

A hardware archivist spent over six months empirically testing how many rewrite cycles various DVD±RW discs survive on a Lite-On iHAS120 drive, fully automating burn–verify–read–quality-scan loops via Opti Drive Control and pyautogui. Failure was defined as the first verify error; DVD-RWs effectively did double cycles because each rewrite triggered a full erase. Results varied widely by brand and speed: a Memorex 8x DVD+RW died at 106 cycles, Sony 6x DVD-RWs at ~200, a Japanese Victor JVC 6x DVD-RW reached 639 verified cycles (effectively >1000 erases), and a TDK 4x DVD+RW hit 413. Across 5,248 burns and ~4,020 drive-hours, both drives kept working, highlighting how much media quality and write speed matter for longevity.

---

### Comment pulse

- People underestimated DVD±RW endurance → Many assumed “a few rewrites at best,” are surprised by hundreds of successful cycles; compare it to modern SSD wear anxiety.  
- Tech nostalgia and media quirks → Stories of DVD-RW/DVD-RAM and magneto‑optical (MiniDisc) underline how capable, yet poorly marketed, rewritable optical media were.  
- Practitioner validation → Former optical-driver engineer confirms: media brand is critical, slower burns age better, and real-world drives often violate standards—counterpoint: consumers rarely saw this nuance.

---

### LLM perspective

- View: This is a rare, methodical, long‑run endurance test that exposes huge variability hidden behind identical “RW” logos.  
- Impact: Archivists, retro‑computing fans, and anyone using optical backup can choose media and speeds more rationally.  
- Watch next: Similar automated stress‑tests for BD‑RE, SD cards, and consumer SSDs, with cross‑drive comparisons instead of single‑drive results.
