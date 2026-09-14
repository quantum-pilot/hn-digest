# Reverse engineering my e-scooter and rewriting the firmware in Rust

- Score: 414 | [HN](https://news.ycombinator.com/item?id=49638071) | Link: https://bensimms.moe/reverse-engineering-scooter/

### TL;DR

The author reverse-engineered an Egret GT scooter after finding a firmware-update path that bypassed its PIN. App inspection exposed Bluetooth update targets and telemetry allegedly sent to the manufacturer; probing the display’s USB-C pins revealed a CAN bus. The author logged and decoded messages for throttle, modes, lights, speed, and battery state, extracted controller firmware through SWD, and analyzed it in Ghidra. They then built replacement display firmware in Rust with asynchronous tasks, explicit locked/unlocked states, persistent configuration, and a low-memory interface.

### Comment pulse

- Ownership enables deep inspection → accessible pads, replacement modules, standard tooling, and observable buses let the author reconstruct undocumented behavior.
- The original design exposed security and privacy concerns → a PIN bypass and undisclosed telemetry motivated scrutiny beyond customization.
- Rust supported structured embedded development → typed state, asynchronous tasks, and allocation-free UI components organized safety-critical interactions.

### LLM perspective

- View: The project demonstrates how physical access converts opaque consumer hardware into documented protocols and replaceable software boundaries.
- Impact: Owners gain repair and customization leverage, while manufacturers face questions about telemetry disclosure and avoidable bypasses.
- Watch next: Audit fail-safe behavior, braking interactions, update authentication, electrical compliance, fault injection, and long-duration road testing.
