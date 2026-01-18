# Drone Hacking Part 1: Dumping Firmware and Bruteforcing ECC

- Score: 129 | [HN](https://news.ycombinator.com/item?id=46654749) | Link: https://neodyme.io/en/blog/drone_hacking_part_1/

### TL;DR
Longform walkthrough of hacking a Potensic Atom 2 drone by physically dumping its NAND flash, dealing with noisy SPI reads, and reverse‑engineering a custom BCH ECC layout to reconstruct a clean 512 MiB firmware image. The authors desolder the chip, script their own ESP32-based reader, use entropy analysis to infer data/ECC interleaving, then brute‑force BCH parameters and bit/byte transforms to correct on‑device errors and mount UBIFS filesystems. HN readers appreciate the educational depth, hardware inspiration, and debate broader implications for DRM and misuse.

---

### Comment pulse
- Experimentation over manuals → readers relate to “just try it” debugging, noting a small parity-notation typo and how datasheets only become clear in hindsight.  
- ECC clarification → some expected elliptic‑curve crypto; instead, they praise the clear BCH/ECC treatment, saying it demystifies hands‑on hardware hacking and sparks project ideas, plus performance curiosity.  
- Apply approach to BOSCH e‑bike DRM → desired for repair/customization — counterpoint: may also facilitate theft and illegal tuning, inviting stricter regulation.  

---

### LLM perspective
- View: Methodically reversing undocumented ECC shows how far persistence and general math tools go, even without vendor cooperation.  
- Impact: Enables serious analysis of “closed” IoT devices; similar workflows can unlock routers, cameras, and automotive or drone ecosystems.  
- Watch next: Expect reusable ECC‑reverse‑engineering tooling, more firmware dumps of consumer drones, and manufacturer moves toward authenticated, encrypted storage.
