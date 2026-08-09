# Conway's Game of Life, in real life

- Score: 313 | [HN](https://news.ycombinator.com/item?id=47434732) | Link: https://lcamtuf.substack.com/p/conways-game-of-life-in-real-life

### TL;DR

An interactive 17×17 grid of 289 illuminated mechanical switches turns the cellular automaton into a tactile tabletop object. An AVR128DA64 multiplexes LED rows and columns at a 1/17 duty cycle, scans the same matrix for presses, reads a knob for 0–10 Hz speed, and pauses two seconds after edits. Because each LED receives 150 mA pulses, game-state updates occur during blackout windows, while a 15-millisecond watchdog reboots stalled firmware. HN loved the physicality and humor, while suggesting four MIDI Launchpads as a cheaper, imperfect 16×16 alternative.

### Comment pulse

- Single-purpose physical objects feel unusually engaging → tactile controls and visible mechanisms give a familiar simulation presence beyond a screen.
- Hobby budgeting became the favorite joke → 289 switches at roughly $3 each made deliberate extravagance part of the charm.
- Launchpads could cut cost substantially → four provide a 16×16 surface, but introduce gaps, clipped buttons, and different proportions.

### LLM perspective

- **View:** The project’s value comes from physical interaction and craftsmanship, so a cheaper touchscreen would miss its central design goal.
- **Impact:** Hardware hobbyists gain a complete reference for multiplexing high-current LEDs while safely sharing lines with switch scanning.
- **Watch next:** Long-term switch reliability, thermal behavior, repairability, alternative key hardware, and electromechanical or flip-dot variants.
