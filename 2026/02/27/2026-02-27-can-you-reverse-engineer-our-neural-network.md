# Can you reverse engineer our neural network?

- Score: 252 | [HN](https://news.ycombinator.com/item?id=47146487) | Link: https://blog.janestreet.com/can-you-reverse-engineer-our-neural-network/

### TL;DR
Jane Street released a puzzle: a PyTorch model whose behavior you must infer from weights alone. A student, Alex, inspects the final layers and realizes they implement an equality check against a fixed 16‑byte value. After heavy graph simplification, ILP and SAT attempts stall. He then notices strong periodic structure and, with LLM help, identifies the core as an MD5 hash implemented via logic-gate-style ReLU circuits, including an accidental length‑handling bug. Once the embedded hash is read from the biases, the “solution” is simply brute‑forcing a two‑word English phrase.

---

### Comment pulse
- Hash extraction → Some readers quickly pulled the target MD5 from the model and used hashcat plus a wordlist to crack the phrase almost instantly.  
- Hiring pipeline → Similar puzzles from Anthropic and others serve as high-signal recruitment tools, giving candidates hands-on ML, crypto, and interpretability experience.  
- Interpretability’s role → Many see mechanistic interpretability as future debugging; skeptics argue most software value lies in human decisions, not fully decoding opaque models — counterpoint: safety-critical AI demands such tools.

---

### LLM perspective
- View: This puzzle neatly bridges CTF-style cryptography with mechanistic interpretability, showing “neural nets as weird programs” in a tangible way.  
- Impact: Encourages practitioners to think in terms of circuits, invariants, and reductions, not just gradients and training curves.  
- Watch next: Expect more puzzles that hide standard algorithms in networks, plus better tooling for automated circuit discovery and bug localization.
