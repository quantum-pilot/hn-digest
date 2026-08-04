# An ESP32 based plane radar for my desk

- Score: 260 | [HN](https://news.ycombinator.com/item?id=49054107) | Link: https://blog.ktz.me/esp32-plane-radar/

### TL;DR

An ESP32-C3 and 1.28-inch round screen become a desk display that fetches nearby ADS-B aircraft, plotting bearing, distance, and flight details. Assembly took about 15 minutes plus light soldering, and browser flashing took under 30 seconds; tight enclosure tolerances forced a different print. The author’s fork adds route and aircraft context, weather, configurable coordinates and display settings, larger text, and authenticated wireless updates. HN liked the gadget but stressed it visualizes reported aircraft positions rather than performing radio detection and ranging.

### Comment pulse

- Radar terminology matters → the device neither transmits probing waves nor derives positions from reflections; it presents externally supplied ADS-B data on a PPI-like display.
- Aircraft tracking has practical value → one reader used a Raspberry Pi receiver to follow firefighting tankers and infer agency attention before alerts.
- Setup could become more automatic → commenters suggested Wi-Fi or IP geolocation to avoid manually entering latitude and longitude.

### LLM perspective

- **View:** The project’s appeal comes from compressing public aviation data into an ambient, glanceable physical object.
- **Impact:** Aviation hobbyists get an approachable display, while serious monitoring still benefits from dedicated receivers and richer aggregation services.
- **Watch next:** Add automatic location, measure feed latency and coverage, publish enclosure tolerances, and clarify local versus internet sources.
