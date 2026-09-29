# Flip Fluid on Flip Dots

- Score: 398 | [HN](https://news.ycombinator.com/item?id=49854219) | Link: https://mitxela.com/projects/flipflip

### TL;DR

Mitxela built an interactive FLIP fluid simulation from eight reclaimed 13-by-28 electromechanical flip-dot panels for EMF2026. To eliminate slow matrix scanning and visible wipe artifacts, custom boards drive every dot independently using cheap motor-driver chips, series capacitors, shift registers, distributed microcontrollers, and RS485. A joystick controls gravity while the dots supply their own sound. The installation cost under £500 excluding donor parts and labor, ran for four festival days, and exposed the hidden commercial cost: hundreds of hours of delicate soldering and repairs.

### Comment pulse

- Independent dot drive enables fluid-like motion → capacitor pulses avoid matrix artifacts while limiting damage from firmware holding a coil on.
- Reclaimed hardware shifts cost into labor → donor panels kept materials cheap, but preparation, soldering, and pixel repair consumed hundreds of hours.
- Flip-dot sound is part of the medium → even a protective acrylic cover was rejected because it muffled the mechanical effect.

### LLM perspective

- View: The project’s key achievement is practical electromechanical control, with the simulation serving as an expressive stress test.
- Impact: Published driver boards give similar Hanover panels a path to fast, tileable, safer operation.
- Watch next: Adaptations for other panel sizes, volunteer assembly methods, state sensing, and arcade-style applications.
