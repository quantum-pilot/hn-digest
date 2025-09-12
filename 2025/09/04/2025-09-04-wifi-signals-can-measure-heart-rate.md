# WiFi signals can measure heart rate

- Score: 466 | [HN](https://news.ycombinator.com/item?id=45127983) | Link: https://news.ucsc.edu/2025/09/pulse-fi-wifi-heart-rate/

- TL;DR
  - UC Santa Cruz’s Pulse-Fi measures heart rate from WiFi reflections using low-cost ESP32/Raspberry Pi and ML filtering. In tests with 118 people, five seconds yielded ~0.5 BPM error, working while seated, walking, and up to ~3 m away; longer windows improved accuracy. It’s a proof‑of‑concept with its own dataset; breathing/apnea detection is next. HN debates deployment: current setup is dedicated and single‑target, but commodity accuracy is notable; non‑invasive sensing is maturing; privacy/biometric risks weigh against eldercare benefits.

- Comment pulse
  - Real-world readiness questioned → dedicated emitter/receiver; unclear multi-person handling or simultaneous data traffic — counterpoint: single-antenna ESP32 accuracy is a meaningful proof-of-concept.
  - Biometric risk → heart and WiFi CSI can re-identify people at a distance; raises surveillance/privacy concerns beyond health monitoring.
  - Non-invasive sensing is booming → echoes NDT practices and prior RSSI/CSI gesture systems; cheap ubiquitous radios enable useful proxy measurements.

- LLM perspective
  - View: Low-cost WiFi plus ML makes passive vitals plausible, but multi-person separation and interference handling determine practical value.
  - Impact: Home health, eldercare, and sleep monitoring could gain insights without wearables; router and IoT vendors may compete on sensing.
  - Watch next: Release code/datasets, 802.11bf progress, clinical validation, multi-target benchmarks, and privacy standards for in-home RF biometrics.
