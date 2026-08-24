# Carrier Landing in Top Gun for the NES

- Score: 349 | [HN](https://news.ycombinator.com/item?id=46274822) | Link: https://relaxing.run/blag/posts/top-gun-landing/

### TL;DR

Reverse-engineering Top Gun’s NES landing routine reveals the exact success check: altitude 100–299, speed 238–337, and heading 0–7, all inclusive, when the sequence ends. Speed and altitude are stored as binary-coded decimals, apparently simplifying screen rendering; the routine writes a result code that selects the landing or crash trajectory. The game itself recommends altitude 200 and speed 288, but not the tolerances. Commenters said the harder part is coordinating pitch and throttle under its coupled flight physics.

### Comment pulse

- Manuals and the display gave target values, but readers found the newly documented tolerances—especially altitude’s wider margin—useful.
- Experienced players emphasized that nose angle changes speed, so braking while diving fails despite apparently correct control inputs.
- Carrier landing inspired frustration, yet several readers remembered midair refueling as even harder.

### LLM perspective

- View: A tiny disassembly converts a famously opaque challenge into explicit state constraints without removing the piloting skill.
- Impact: Players can prioritize heading and speed while exploiting the much broader altitude window.
- Watch next: Emulator-assisted validation at boundary values and similar analysis of the refueling sequence.
