# AliExpress runs silent WebAudio fingerprinting that breaks Bluetooth multipoint

- Score: 848 | [HN](https://news.ycombinator.com/item?id=49372583) | Link: https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html

### TL;DR

An investigator traced broken Bluetooth multipoint switching to two obfuscated AliExpress scripts creating silent WebAudio graphs. Their oscillators and analyzers feed zero-gain output into the audio destination, keeping the PC path active despite mute controls. The bundles also collect canvas, WebGL, hardware, timing, interaction, and automation signals, then transmit encrypted results. Blocking both script families stopped the contexts locally, though it could hinder anti-fraud checks. Comments reported similar effects on hearing aids and cars and urged browser visibility.

### Comment pulse

- Browser-control demands dominated → hidden audio processing should trigger tab indicators or permission notices like other hardware-sensitive APIs.
- Corroborating anecdotes spanned hearing aids, car audio, and Bluetooth peripherals → silent activity can create accessibility and usability failures.
- Tracking intent remained uncertain → the code resembles broad fingerprinting, while fraud and bot detection offer a plausible operational purpose.

### LLM perspective

- View: Client code establishes fingerprint-like collection and transmission, not server-side retention, identity linkage, or final purpose.
- Impact: Zero-volume processing can disrupt assistive devices and multipoint audio while evading controls users reasonably expect to work.
- Watch next: Browser indicators, background-execution rules, independent reproduction, AliExpress disclosure, and whether narrow blocking disrupts authentication or checkout.
