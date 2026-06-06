# Show HN: Edsger – A handwritten Clojure REPL for the reMarkable 2

- Score: 233 | [HN](https://news.ycombinator.com/item?id=48374552) | Link: https://handwritten.danieljanus.pl/2026-06-01-edsger.html

### TL;DR
A hobby project called Edsger turns a reMarkable 2 e‑ink tablet into a handwritten Clojure REPL: you write Clojure code with the pen, it’s captured from the tablet, transcribed via an LLM (Claude), evaluated on a Clojure interpreter, and the results are rendered back into the notebook. The author documents it in a fully handwritten blog, including clickable links. HN readers love the hackability and aesthetics but note significant interaction latency and brainstorm ways to reduce it.

---

### Comment pulse
- Latency analysis → ~14 seconds from pen-up to result; most delay from reMarkable’s slow file writes, plus transcription and REPL startup.  
- Optimization ideas → Direct framebuffer access, custom Qt apps, and offloading via streaming to a server are suggested to cut delay—counterpoint: complexity might outweigh benefit for a hobby tool.  
- Meta inspiration → People discover they can SSH into reMarkable, praise the handwritten SVG blog with embedded links, and see the device as a fertile hacking platform.

---

### LLM perspective
- View → Clever pipeline: e‑ink capture → file event → LLM transcription → Clojure eval → rendered output, all tied to handwritten UX.  
- Impact → Encourages treating e‑ink devices as programmable canvases for code, notebooks, and LLM-backed “magic paper” tools.  
- Watch next → Faster on-device triggers, incremental streaming of output, and more robust notebook-style UIs integrating handwriting, code, and results.
