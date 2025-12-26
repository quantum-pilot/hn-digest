# Quantum Error Correction Goes FOOM

- Score: 61 | [HN](https://news.ycombinator.com/item?id=46383233) | Link: https://algassert.com/post/2503

### TL;DR
Craig Gidney argues that quantum error-corrected qubit lifetimes can improve superexponentially once systems cross quality thresholds and qubit counts keep scaling. Google’s repetition-code experiments progressed from ~100 µs (2014) to ~2 hours (2024) by adding qubits and removing “QEC hurdles” like leakage and cosmic-ray hits, matching a model where lifetime scales roughly as λ^q with q growing exponentially. He predicts a similar “FOOM” for fully quantum (surface-code) logical qubits within ~5 years, though quantity and speed remain unsolved bottlenecks.

---

### Comment pulse
- 59-qubit repetition result is classical-style storage → bit-flip-only correction equals a classical bit; still strong evidence these are genuine, reorientable qubits.  
- “Can huge arrays do problems in one shot?” → no; depth lower bounds (e.g., Grover) and reaction constraints make speed a real resource.  
- Hype and FOOM framing raise eyebrows → some see grant-chasing and overpromising — counterpoint: author explicitly limits claim to error-corrected quality, not full-scale QC.

---

### LLM perspective
- View: The data show a clear pattern: once engineering crosses thresholds, error correction rapidly outruns individual qubit quality.  
- Impact: Hardware roadmaps may shift toward aggressively finding and removing QEC hurdles (leakage, cosmic rays, power events) over incremental fidelity tweaks.  
- Watch next: Multi-logical-qubit surface-code demos, cross-platform lifetime scaling, and standardized “logical uptime” benchmarks including correlated and catastrophic error sources.
