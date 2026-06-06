# WriteUp: 16 Bytes of x86 that turn Matrix rain into sound

- Score: 187 | [HN](https://news.ycombinator.com/item?id=48173962) | Link: https://hellmood.111mb.de//wake_up_16b_writeup.html

## TL;DR
A 16-byte MS‑DOS program uses the text‑mode video buffer as both canvas and data store to compute a Sierpinski triangle (Rule 60 cellular automaton) and simultaneously drive the PC speaker. `xor`-based prefix sums over VRAM generate the fractal’s bit pattern; bit 1 is sent directly to port 0x61, turning geometry into square‑wave audio. A -56‑byte stride shears the triangle into diagonal pillars and drops the pitch an octave. HN readers celebrate it as extreme “sizecoding” art and compare other microscopic demos.

---

## Comment pulse
- Constraint‑art lineage → Readers compare this to Freespin, Spongy (128b), and Rainy 32b, admiring how tiny intros still achieve rich audiovisual experiences.  
- Deep writeups appreciated → Commenters praise the mathematical/hardware exposition and recall the author’s earlier “Memories” article as similarly educational and inspiring.  
- Emotional impact → Some are shocked by how musical and eerie it feels, joking it’s a “secret key” unlocking a beast—counterpoint: a few expected more literal “Matrix rain to sound.”

---

## LLM perspective
- View: Showcases how minimal code can exploit hardware side effects and math (Rule 60) to yield complex, emergent art.  
- Impact: Encourages low-level experimentation, demoscene competitions, and teaching hardware/CA concepts through tiny, runnable artifacts.  
- Watch next: Systematic searches for new <32‑byte intros; hardware-accurate emulation to preserve machine-specific “fingerprints”; more rigorous analyses of such algorithms.
