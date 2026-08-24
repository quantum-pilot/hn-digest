# Show HN: Glasses to detect smart-glasses that have cameras

- Score: 468 | [HN](https://news.ycombinator.com/item?id=46075882) | Link: https://github.com/NullPxl/banrays

### TL;DR

A prototype wearable seeks to warn people when nearby smart glasses contain cameras without using a camera itself. Infrared LEDs and a photodiode look for lens retro-reflections, but tests against Meta Ray-Bans were weak and inconsistent even inches away. BLE fingerprints using Meta manufacturer and service identifiers work during pairing or power-on, not reliably during ordinary use because connection following needs better radio hardware. Commenters saw privacy, venue-security, and anti-surveillance uses while questioning wearability and modern cameras’ resistance to infrared dazzling.

### Comment pulse

- Optical detection remains noisy → glossy surfaces resemble lenses, signal strength varies, and useful scans currently require close, deliberate sweeps.
- BLE identification is event-limited → randomized addresses matter less than Meta identifiers, but advertisements rarely appear during ongoing use.
- A clip-on form may win adoption → users want protection without replacing preferred eyewear or trusting a vendor vulnerable to acquisition.

### LLM perspective

- View: Combining independent optical and radio evidence could reduce false alarms better than either immature channel alone.
- Impact: Reliable detection would restore notice and consent in spaces where discreet recording is otherwise invisible.
- Watch next: nRF packet following, Ray-Ban daylight tests, multi-wavelength optics, collimation, false-positive rates, and clip-on prototypes.
