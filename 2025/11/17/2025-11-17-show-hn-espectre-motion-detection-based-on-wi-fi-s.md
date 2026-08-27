# Show HN: ESPectre – Motion detection based on Wi-Fi spectre analysis

- Score: 106 | [HN](https://news.ycombinator.com/item?id=45953977) | Link: https://github.com/francescopace/espectre

### TL;DR

ESPectre is an experimental GPLv3 motion sensor using a roughly €10 ESP32-S3, ordinary 2.4 GHz router traffic, and MQTT or Home Assistant. It analyzes Wi-Fi Channel State Information: raw subcarrier turbulence feeds a two-state moving-variance detector, while optional filters produce ten statistical, spatial, and temporal features. No trained model or labeled dataset is required. Detection is environment-dependent, needs calibration, works best three to eight meters away, and cannot distinguish people, pets, or objects. Commenters highlight both creative uses and surveillance risk.

### Comment pulse

- The author is mapping continuous turbulence measurements to pitch for a Wi-Fi theremin running entirely on the ESP32.
- Signal-processing discussion compared controlled ICMP traffic with passive ACK sniffing and dedicated transmitter-receiver pairs.

### LLM perspective

- View: Cheap device-free sensing is useful precisely because its low barrier also makes covert deployment easy.
- Impact: Home automation gains camera-free occupancy signals, but privacy assumptions no longer follow from absent microphones or lenses.
- Watch next: False-positive measurements, cross-room leakage, adversarial testing, 802.11bf hardware, and explicit consent controls.
