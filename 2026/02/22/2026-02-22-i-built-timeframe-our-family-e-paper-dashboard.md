# I built Timeframe, our family e-paper dashboard

- Score: 465 | [HN](https://news.ycombinator.com/item?id=47113728) | Link: https://hawksley.org/2026/02/17/timeframe.html

### TL;DR

Timeframe evolved over a decade from an unreadable LCD mirror and fragile jailbroken Kindles into several e-paper household displays combining calendars, weather, music, and Home Assistant sensor status. A 25.3-inch Boox Mira Pro enables real-time updates, while smaller battery-powered Visionect panels refresh periodically. Moving integrations into Home Assistant removed over half the Rails code, Redis, and the database. HN admired the calm, glanceable “information radiator” but saw the roughly $2,000 large display and supporting hardware as the central barrier to mainstream adoption.

### Comment pulse

- Ambient e-paper shares information without glow or doomscrolling → a blank status area means the house needs no attention.
- Cost scales badly with size → sub-$100 ESP32 builds work for smaller panels — counterpoint: polished large displays remain niche and expensive.
- Simpler alternatives have value → recycled tablets, reflective LCDs, or even a kitchen whiteboard can serve overlapping family needs.

### LLM perspective

- **View:** Separating status display from device control is the project’s most reusable design principle.
- **Impact:** Home Assistant users gain a calmer interface, but installation and maintenance still demand enthusiasts.
- **Watch next:** Sole-source Home Assistant integration, embedded reliability, lower-cost hardware, and a viable product price.
