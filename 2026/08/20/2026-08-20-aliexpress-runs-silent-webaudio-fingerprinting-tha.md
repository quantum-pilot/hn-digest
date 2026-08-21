# AliExpress runs silent WebAudio fingerprinting that breaks Bluetooth multipoint

- Score: 848 | [HN](https://news.ycombinator.com/item?id=49372583) | Link: https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html

- TL;DR  
  AliExpress’s homepage silently spins up WebAudio graphs that emit inaudible sawtooth signals into the audio output, as part of a larger device-fingerprinting and anti-fraud system. Because the audio pipeline stays “live”, it can hijack Bluetooth audio priority, breaking multipoint headphones while evading normal tab mute controls. The author shows how to block the specific scripts with uBlock Origin, warning it may trigger more CAPTCHAs. HN readers debate browser-level safeguards, share similar Bluetooth glitches, and note partial fingerprinting mitigations.

- Comment pulse  
  - Browsers should surface any live audio graph with icons or permission prompts → silent WebAudio currently hides from users yet affects devices.  
  - Multiple users report hearing aids, car stereos, and mice misbehaving when sites start “silent” streams → Bluetooth treats them as real audio sessions.  
  - Some note Firefox already randomizes WebAudio fingerprints → mitigates tracking, not side effects—counterpoint: relying on individual browsers, not standards, leaves gaps.

- LLM perspective  
  - View: Covert hardware engagement as a tracking vector shows how “benign” APIs become de facto surveillance and capability probes.  
  - Impact: Browser vendors face pressure to gate high-entropy APIs behind permissions or indicators, especially when they alter peripheral behavior.  
  - Watch next: Standardized WebAudio throttling, fingerprinting-resistance test suites, and independent audits of large sites’ anti-fraud scripts and data retention.
