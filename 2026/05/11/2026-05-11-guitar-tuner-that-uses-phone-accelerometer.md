# Guitar tuner that uses phone accelerometer

- Score: 152 | [HN](https://news.ycombinator.com/item?id=48058260) | Link: https://tautme.github.io/phone-sensors/accel-tuner.html

### TL;DR

Accel Tuner uses a phone’s motion sensor rather than its microphone. Press the handset against a guitar body, pluck a string, and the browser plots three acceleration axes plus combined magnitude, estimates pitch from the strongest axis, then corrects sampling aliases against expected string frequencies. It requires motion permission and works best with Android’s higher-rate IMUs. Commenters reproduced low-frequency readings on other vibrating objects and compared it with clip-on contact tuners. They noted 50–200 Hz sampling cannot directly capture every guitar string, but known targets make alias correction practical.

### Comment pulse

- Users detected a foosball-handle resonance and even a heartbeat, illustrating surprising sensitivity to direct mechanical coupling.
- Security concerns focused on covert sensing — counterpoint: phone mass, low sensitivity, and limited sampling make intelligible airborne speech unlikely.
- Orchestra players value contact tuners because vibrations isolate one instrument from surrounding sound, especially amid many nearby strings.

### LLM perspective

- View: Constraining the signal to six expected notes turns undersampling from a blocker into a solvable ambiguity.
- Impact: A microphone-free tuner can work in noisy rooms while demonstrating why motion access remains privacy-sensitive.
- Watch next: Device compatibility, false-octave rates, latency, calibration, permission behavior, and comparisons against clip-on and microphone tuners.
