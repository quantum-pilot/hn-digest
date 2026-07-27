# An ESP32 based plane radar for my desk

- Score: 260 | [HN](https://news.ycombinator.com/item?id=49054107) | Link: https://blog.ktz.me/esp32-plane-radar/

- TL;DR  
  An ESP32-C3 and a 1.28″ round display are turned into a desktop “plane radar” that visualizes nearby ADS‑B aircraft by distance and bearing. The author finds flashing trivial via a browser-based ESPHome tool, but discovers the popular 3D-printed case has tolerances too tight for their boards and swaps to a more forgiving model. They then fork the firmware to add richer flight context, weather and time widgets, web‑configurable settings, larger text, and authenticated OTA updates, with plans for a bigger display and custom enclosure.

- LLM perspective  
  - View: Nicely illustrates how commodity microcontrollers plus public ADS‑B data enable polished, purpose-built “ambient” displays.  
  - Impact: Lowers the bar for hobbyists to build rich, networked dashboards that feel like finished consumer gadgets.  
  - Watch next: More generalized ESP32 frameworks for pluggable widgets, displays, and OTA workflows, beyond single-purpose projects like this.
