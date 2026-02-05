# Building a 24-bit arcade CRT display adapter from scratch

- Score: 106 | [HN](https://news.ycombinator.com/item?id=46888795) | Link: https://www.scd31.com/posts/building-an-arcade-display-adapter

### TL;DR
A Recurse Center member built a custom USB-to-VGA adapter so laptops can drive an old arcade CRT at odd resolutions with true 24‑bit color. Early attempts used an RP2040’s PIO and a Rust GUD gadget implementation, but USB full‑speed bandwidth and improvised resistor DACs limited color depth and framerate. A second‑generation STM32H7 board with external HS PHY, SDRAM, hand‑designed VGA DAC, and 3D‑printed enclosure finally delivered 60 Hz, banding‑free output. HN discussion centers on PCB best practices, newer MCUs, and CRT timing details.

---

### Comment pulse
- Serious adapter design → add TVS/ESD parts on all external pins, buffer or IC DACs, and wider traces/vias to improve robustness and manufacturability.  
- RP2350’s improved PIO and new HSTX block → could generate high‑res, high‑depth VGA directly, avoiding STM32 complexity — counterpoint: still lacks USB HS.  
- CRT engineers → blanking actually surrounds the active picture and carries metadata like CC/VITC; the article’s reference timing diagram is oversimplified.

---

### LLM perspective
- View: This is an excellent end‑to‑end example of turning a “hacky” proof‑of‑concept into a real, product‑like embedded system.  
- Impact: Arcade and CRT hobbyists gain a template for weird‑mode, high‑color USB display adapters using GUD plus commodity MCUs.  
- Watch next: Benchmark similar designs on RP2350 vs STM32H7; add audio/input; upstream GUD improvements like optional deltas and real documentation.
