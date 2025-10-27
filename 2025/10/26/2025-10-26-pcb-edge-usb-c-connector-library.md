# PCB Edge USB C Connector Library

- Score: 154 | [HN](https://news.ycombinator.com/item?id=45708686) | Link: https://github.com/AnasMalas/pcb-edge-usb-c

- TL;DR
An open library for using a PCB’s edge as a USB‑C “connector” drew interest for prototyping and low‑profile builds: no socket to buy or solder, fewer parts. Commenters warned about durability and production: abrasive wear on contacts, thin tongues snapping, and test/assembly tooling that doesn’t scale. Cost and geometry came up too, with ~0.6 mm tongue thickness suggested and some hesitance about finish costs. Consensus: clever and quick for bench or hobby gear, rarely ideal for mass production or high‑cycle ports.
  
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - Prototyping and space-saving → no connector to buy or solder; fewer failure points; faster assembly for DIY keyboards and dev boards.
  - Not production-friendly → edge fingers and Tag‑Connect/pogo wear; clips don’t fit lines; bed‑of‑nails at 50‑mil pitch is fussy and costly — counterpoint: fine for bench use.
  - Manufacturing specifics → ENIG preferred for wear/corrosion; HASL used successfully; 0.6 mm PCB tongue recommended; expect limited replug cycles.

- LLM perspective
  - View: Treat as a bench-only connector or internal debug port, not a customer-facing USB-C.
  - Impact: Cuts BOM and soldering steps for low-volume builds; simplifies DIY keyboards, dev boards, and cramped enclosures.
  - Watch next: Publish durability tests and stackups; compare ENIG vs HASL wear; validate 0.6 mm fab tolerances at multiple board houses.
