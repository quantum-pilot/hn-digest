# Carrier Landing in Top Gun for the NES

- Score: 349 | [HN](https://news.ycombinator.com/item?id=46274822) | Link: https://relaxing.run/blag/posts/top-gun-landing/

### TL;DR

Reverse engineering reveals the NES game’s carrier-landing check: altitude must finish between 100 and 299, speed between 238 and 337, and heading between 0 and 7. The game stores speed and altitude as binary-coded decimal, evaluates them in a routine at address B6EA, and records the outcome at 9E; Game Genie code AEPETA forces success. Commenters note the manual and screen already supplied target values, but the newly exposed tolerances explain why apparently similar approaches could produce different outcomes.

### Comment pulse

- Players say coupled pitch and throttle physics, not hidden target values, made landing difficult.
- The altitude tolerance is much wider than speed and heading → prioritizing lateral alignment and speed improves consistency.
- Several remember midair refueling as even harder than carrier landing.

### LLM perspective

- View: The disassembly converts childhood trial-and-error into a precise three-variable boundary test.
- Impact: Players can allocate attention to narrow tolerances instead of chasing the displayed center perfectly.
- Watch next: Instrument the approach physics to map how pitch, throttle, and air brakes move those variables.
