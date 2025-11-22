# It's hard to build an oscillator

- Score: 216 | [HN](https://news.ycombinator.com/item?id=46002161) | Link: https://lcamtuf.substack.com/p/its-hard-to-build-an-oscillator

### TL;DR
The piece walks through why robust analog oscillators are surprisingly tricky: any circuit with gain wants to settle into a stable point rather than free‑run. The author builds up from a failing single‑MOSFET “switch” to a discrete Schmitt trigger relaxation oscillator, then a simpler op‑amp version, and finally a phase‑shift oscillator using RC filters and feedback phase. Along the way, they derive approximate frequency formulas and show scope traces, arguing that microcontrollers are usually easier now but analog designs teach core intuition.

---

### Comment pulse
- Amps become oscillators → Practical war stories: audio amps, radios, and mixers accidentally oscillate; “VIUPS” and feedback loops show how easy it is.  
- LC oscillators are easy → One commenter auto‑discovers LC topologies with SPICE; others note most “novel” designs are century‑old Colpitts variants — counterpoint: the search approach is still inspiring.  
- Real difficulty is stability → Clean sinewaves need controlled gain (e.g., lightbulb AGC), and precise clocks care about temperature, noise, Allan variance over decades.

---

### LLM perspective
- View: This is an excellent worked example of turning qualitative feedback stories into quantitative, testable oscillator designs.  
- Impact: Hobbyists and junior engineers gain intuition for hysteresis, phase shift, and why datasheet curves matter more than idealized “switches.”  
- Watch next: Tools that co‑design MCU firmware plus minimal analog front‑ends could make mixed‑signal oscillators both robust and approachable.
