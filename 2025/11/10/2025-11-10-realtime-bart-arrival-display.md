# Realtime BART Arrival Display

- Score: 233 | [HN](https://news.ycombinator.com/item?id=45873113) | Link: https://filbot.com/real-time-bart-display/

### TL;DR

A hobbyist built a polished, vintage-style BART arrivals display using a red 20×4 character OLED, an ESP32-C6 board, a logic-level converter, and a carefully finished 3D-printed enclosure. The device shows live arrivals, a clock, and safety messages above the author’s desk. Rather than parse BART’s GTFS Realtime feed on the microcontroller, it requests simplified data from personal middleware. The author shared both the code and enclosure files for others to reproduce or adapt.

### Comment pulse

- Readers praised the physical finish, while debating whether ambient arrival data reduces waiting or merely makes delays more visible.
- Some thought the ESP32 could parse the feed directly, eliminating the middleware dependency.

### LLM perspective

- View: Purpose-built ambient displays can make public data more useful than another phone notification.
- Impact: The polished enclosure turns a small data project into durable, glanceable household infrastructure.
- Watch next: Direct feed parsing could simplify deployment by removing the author-operated middleware.
