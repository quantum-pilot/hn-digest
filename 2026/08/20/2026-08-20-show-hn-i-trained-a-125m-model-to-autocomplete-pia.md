# Show HN: I trained a 125M model to autocomplete piano on-device

- Score: 478 | [HN](https://news.ycombinator.com/item?id=49373456) | Link: https://simedw.com/2026/08/20/midi-autocomplete/

### TL;DR
A 125M-parameter decoder-only transformer was trained to autocomplete live piano on-device, running at ~108 notes/sec on an iPhone. The key insights were a compact, note-level MIDI representation (pitch, onset delta, duration, velocity in one step), aggressive data cleaning over sheer scale (~300M notes), and post-training Direct Preference Optimization using Gemini pairwise judgments to favor continuations that follow the prompt musically. HN discussion connects this to historical improvisation, taste as the scarce resource, and potential plugin/VST applications.

---

### Comment pulse
- Classical training analogy → historical composers practiced pattern-based improvisation and “autocomplete” games; this model automates a tradition of stylistic completion.  
- Generation is cheap, taste is scarce → tools like this and AI UI generators shift value to curating, rejecting, and refining ideas, not producing raw material.  
- Product direction → people want this as a VST/Max for Live, fitting naturally into modern DAW workflows and live performance rigs.

---

### LLM perspective
- View: Clever note-level tokenization shows domain-specific structures can massively improve speed and coherence over generic event streams.  
- Impact: Demonstrates that sub-GPT2-sized models can feel “magical” when tightly scoped and engineered for real-time, on-device use.  
- Watch next: Benchmarks comparing DPO vs. plain CE for symbolic music, plus open, reproducible MIDI datasets and DAW/plugin integrations.
