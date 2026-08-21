# Show HN: I trained a 125M model to autocomplete piano on-device

- Score: 478 | [HN](https://news.ycombinator.com/item?id=49373456) | Link: https://simedw.com/2026/08/20/midi-autocomplete/

### TL;DR

Simon Edwardsson built RollTab, a 125M-parameter INT8 Core ML transformer that completes live MIDI piano entirely on iPhone or iPad, reaching about 108 notes per second on an iPhone 15. Its compound note representation predicts pitch, onset gap, duration, and velocity with one backbone pass; preprocessing folds sustain into duration. Training used several hundred thousand cleaned MIDI files containing roughly 300 million notes, where selection beat five-times-larger noisy data. Gemini-ranked DPO yielded 69.05% preference over the base. Short prompts, loops, and evaluator inconsistency remain; commenters connected it to classical improvisation.

### Comment pulse

- Readers noted that historical composers trained through comparable pattern-completion and improvisation exercises.
- A pianist argued cheap generation elevates taste: exploring candidates helps eliminate dead ends and occasionally finds gems.
- Others praised the learning journey and suggested packaging the model as a VST or Max for Live device.

### LLM perspective

- View: Representation, data curation, and preference tuning mattered more than brute-force scale or validation loss.
- Impact: Musicians gain a responsive, private improvisation partner running entirely on mobile hardware.
- Watch next: Human listening studies, stronger short prompts, loop rates, medium-model optimization, longer sessions, and plugin support.
