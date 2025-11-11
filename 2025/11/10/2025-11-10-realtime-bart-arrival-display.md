# Realtime BART Arrival Display

- Score: 233 | [HN](https://news.ycombinator.com/item?id=45873113) | Link: https://filbot.com/real-time-bart-display/

- TL;DR
  - A maker built a desk-friendly, vintage-style BART arrival sign: ESP32‑C6 + red 20×4 SPI OLED, 3D‑printed housing, showing live arrivals, clock, and platform safety messages. Instead of parsing GTFS‑Realtime on-device, a small middleware service fetches BART data and exposes a simplified API for the ESP. HN debates the real benefit of checking arrivals given headways and the waiting‑time paradox, notes strong utility in harsh weather, cites similar DIY/products, and suggests running the API directly on the ESP with LLM‑assisted code translation.

- Comment pulse
  - Skip planning → reduces anxiety; expected wait ~half headway — counterpoint: 30‑min services and waiting‑time paradox justify checking.
  - Home display → avoids standing in −20°C; the difference between 1 and 7 minutes outside matters.
  - Ditch middleware → ESP32 can parse GTFS with help from LLM code translation; others turned similar builds into products using open transit data.

- LLM perspective
  - View: Pattern: edge device + proxy API simplifies complex feeds; 20x4 character OLED nails legibility and vibe.
  - Impact: Helps commuters glanceable info; gives makers a replicable GTFS-to-IoT template; nudges agencies to keep stable open data.
  - Watch next: Measure ESP32‑C6 parsing GTFS vs proxy: latency, power, memory; add caching, MQTT updates, and local voice alerts.
