# Flipper Zero Geiger Counter

- Score: 240 | [HN](https://news.ycombinator.com/item?id=45289453) | Link: https://kasiin.top/blog/2025-08-04-flipper_zero_geiger_counter_module/

- TL;DR
    - A Flipper Zero add‑on turns it into a Geiger counter with graphing, CPS/CPM readouts, CSV logging, and a Geiger‑tick‑based “atomic dice” RNG. It uses a J305 tube (β/γ only) and includes crude Sv/Rad conversions; the author notes dose isn’t precise. HN praises the build but debates value: cheap Geiger kits for curiosity vs. $250–$600 gamma spectrometers for spectra. Commenters highlight tube limits (no energy compensation, saturation, radon needs dedicated monitors), plus safety/enclosure concerns and home‑automation ideas.

- Comment pulse
    - Price/performance: $40–$99 Geiger modules satisfy curiosity; $250–$600 Radiacode/Raysid add spectra/BLE. — counterpoint: some Geigers have higher max dose-rate range for emergencies.
    - Capability caveats: β/γ tubes lack energy compensation; dose readouts can mislead; low-cost tubes saturate in hazardous fields; radon requires dedicated monitors or filter-and-measure setups.
    - Practicalities: exposed high-voltage leads worry users; print an enclosure; low-current HV can be safe, but charged capacitors can bite; desire for Home Assistant/Zigbee logging.

- LLM perspective
    - View: Flipper-as-sensor-hub demo; great for learning, logging, and RNG, not for calibrated dosimetry or emergency response.
    - Impact: Hobbyists, educators, and makers get an approachable radiation toolkit; pros will still prefer energy-compensated, high-range instruments.
    - Watch next: Publish tube calibration factors and saturation tests; add HA/MQTT firmware; compare against Radiacode/Better Geiger in side-by-side datasets.
