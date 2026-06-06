# Guitar tuner that uses phone accelerometer

- Score: 152 | [HN](https://news.ycombinator.com/item?id=48058260) | Link: https://tautme.github.io/phone-sensors/accel-tuner.html

### TL;DR
- A web-based “Accel Tuner” uses a phone’s accelerometer instead of the microphone: you press the phone against the guitar, it graphs XYZ vibrations, picks the strongest axis, and estimates pitch using alias-aware analysis. It works best on devices with high‑rate IMUs. HN users report that low sampling rates on many phones limit accuracy, but experiments show surprising sensitivity, prompting discussion of physical clip‑on tuners and potential privacy risks from accelerometer side‑channel data.

---

### Comment pulse
- Sample-rate limits → Some phones report only 50–200 Hz, below guitar fundamentals; tuner relies on aliasing tricks yet still reveals subtle vibrations like heartbeat.  
- Accelerometer as microphone → Some fear side‑channel eavesdropping and keystroke capture; skeptics note low forces and sample rates — counterpoint: intelligence agencies exploit unconventional sensors.  
- Vibration tuners precedent → Clip‑on guitar/violin tuners already sense wood vibrations; some players even tune by feeling interference beats through the instrument body.

---

### LLM perspective
- View → Clever demo of browser IMU access and alias-aware DSP, but accuracy depends on device-specific sampling rates and noise.  
- Impact → Raises awareness that web pages can read motion sensors, nudging browsers toward stricter permissions and finer-grained rate/precision controls.  
- Watch next → Proof‑of‑concept attacks using accelerometers in realistic conditions, and standardized APIs for querying IMU sampling rate and resolution.
