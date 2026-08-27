# Show HN: Glasses to detect smart-glasses that have cameras

- Score: 468 | [HN](https://news.ycombinator.com/item?id=46075882) | Link: https://github.com/NullPxl/banrays

### TL;DR

Ban-Rays is an experimental wearable intended to detect camera-equipped smart glasses without using its own camera. Infrared sweeps look for lens retro-reflection, but Meta Ray-Ban tests produced weak, inconsistent signals even four inches away. Bluetooth fingerprinting can identify Meta manufacturer data and service UUIDs during pairing or power-on, yet not reliably during normal directed traffic. Commenters saw privacy and venue-security uses, proposed stationary detectors or IR countermeasures, and noted modern camera filters make sensor flooding unreliable, especially in daylight.

### Comment pulse

- Wearability serves people worried about covert public recording → fixed installations may better protect venues or sensitive rooms.
- BLE identification is currently event-limited → advertisements appear during startup or pairing, not consistently while recording.
- IR could detect or disrupt lenses → counterpoint: reflections are noisy and modern filters reduce blinding effectiveness.

### LLM perspective

- View: The prototype demonstrates identifiable signals, not yet a dependable test that nearby glasses contain an active camera.
- Impact: False positives or missed devices would limit trust in personal and security deployments.
- Watch next: Measure range, angles, lighting, device coverage, active BLE probing, and classification error rates on blinded trials.
