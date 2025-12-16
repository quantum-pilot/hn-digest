# Carrier Landing in Top Gun for the NES

- Score: 349 | [HN](https://news.ycombinator.com/item?id=46274822) | Link: https://relaxing.run/blag/posts/top-gun-landing/

## TL;DR
Through 6502 disassembly, the author reverse-engineers Top Gun (NES)’s infamous carrier landing and shows it’s a simple numeric gate: your altitude, speed, and lateral heading only need to fall within specific inclusive ranges at a single end-of-sequence check. Speed and altitude are stored as BCD, heading as a signed byte, and one routine writes a “success/fail reason” to a state byte. HN commenters note that the manual gave target numbers but not tolerances, and that semi-realistic flight physics made matching them genuinely hard.

---

## Comment pulse
- Difficulty was more about semi-realistic energy management than hidden rules → players had to juggle throttle and pitch like real carrier landings.  
- Some insist “RTFM” solved it; others rented cartridges without manuals and remember near-random-feeling landings — counterpoint: on-screen hints still omitted tolerances.  
- Many found midair refueling even harder than landing → strong nostalgia for repeated failure, music, and sleepover NES marathons.

---

## LLM perspective
- View: Reverse-engineering reveals many “unfair” NES moments were deterministic, just opaque, turning mythic difficulty into knowable logic.  
- Impact: Speedrunners, ROM hackers, and retro fans gain precise constraints for training, tooling, and accessibility tweaks.  
- Watch next: Similar analyses of refueling, enemy AI, and other notorious 8-bit sequences, ideally with interactive visualizers over emulator memory.
