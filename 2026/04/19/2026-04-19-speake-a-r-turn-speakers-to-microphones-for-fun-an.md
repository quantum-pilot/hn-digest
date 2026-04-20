# SPEAKE(a)R: Turn Speakers to Microphones for Fun and Profit [pdf] (2017)

- Score: 154 | [HN](https://news.ycombinator.com/item?id=47822805) | Link: https://www.usenix.org/system/files/conference/woot17/woot17-paper-guri.pdf

### TL;DR
SPEAKE(a)R is a 2017 research prototype malware that abuses “jack retasking” on common PC audio codecs (e.g., Realtek HD Audio) to flip an output jack into an input jack, turning plugged-in headphones/earbuds into covert microphones. Experiments show intelligible speech capture at up to 9 meters and usable ultrasonic bandwidth for data exfiltration, even on machines with no official mic. The paper details hardware/driver mechanics, quality measurements, and countermeasures such as one‑way speakers, jack‑retasking policies, and audio jamming.

---

### Comment pulse
- Speaker-as-mic is old news → People recall recording albums or childhood tapes by rapping into busted headphones or plugging speakers into mic jacks.  
- Transducers are reversible → A coil and magnet can both emit and sense sound; dynamic mics/speakers are interchangeable—counterpoint: PC mics are mostly non-reversible condensers/electrets.  
- This duality is exploited elsewhere → Used for subkick drum mics, headphone-based voice notes on hacked iPods, and for absolute sound-pressure calibration at standards labs.

---

### LLM perspective
- View: The novelty isn’t physics; it’s the realistic, software-only exploitation path via ubiquitous HD Audio jack retasking.  
- Impact: Hardens “no-mic” security assumptions in air-gapped or high-security environments; policy must now cover headphones/earbuds, not just microphones.  
- Watch next: OS-level controls exposing and logging jack-role changes, vendor defaults that disable out→in retasking, and tools to simulate/jam such covert channels.
