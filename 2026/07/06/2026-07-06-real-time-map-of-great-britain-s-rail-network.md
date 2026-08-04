# Real-time map of Great Britain's rail network

- Score: 379 | [HN](https://news.ycombinator.com/item?id=48802535) | Link: https://www.map.signalbox.io

### TL;DR

Signalbox provides an interactive browser map of trains moving across Great Britain, rendered with Mapbox and OpenStreetMap and fed by its production map API, with Trainline credited. The page does not document update frequency, positional accuracy, or whether every marker represents measured rather than inferred location. A quoted Signalbox description says its technology can match a snapshot of smartphone data to train trajectories without continuous background location or dedicated hardware. Commenters found it useful but imperfect for anticipating passing trains; discussion contrasted measured positions with schedule-and-delay interpolation used elsewhere.

### Comment pulse

- Practical value survived imperfections → one family regularly uses it to predict passing trains, reporting good but non-perfect results.
- Real-time semantics drew scrutiny → comparable Swiss and French maps interpolate schedules and delays — counterpoint: Signalbox claims smartphone-to-trajectory matching.
- Privacy mechanism remained opaque → matching smartphone snapshots without background tracking sounds efficient, but readers asked which app supplies the data.

### LLM perspective

- **View:** The visualization is compelling, but provenance and uncertainty matter more than marker animation when labeling transit positions real-time.
- **Impact:** Reliable live positions can aid passengers, enthusiasts, and operations; inferred movement can mislead during disruptions.
- **Watch next:** API documentation, source coverage, latency, confidence indicators, smartphone consent, data retention, and behavior when trains stop unexpectedly.
