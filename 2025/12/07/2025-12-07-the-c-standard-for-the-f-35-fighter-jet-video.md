# The C++ standard for the F-35 Fighter Jet [video]

- Score: 160 | [HN](https://news.ycombinator.com/item?id=46183657) | Link: https://www.youtube.com/watch?v=Gv4sDL9Ljww

## TL;DR
The F-35 uses a heavily restricted C++ subset defined by a 142‑page “JSF C++” coding standard: no STL, no dynamic allocation after initialization, strong bans on unsafe constructs, and detailed style/logic rules (e.g., every `if/else if` must end with `else` or a justification). HN discussion centers on why C++ beat Ada (talent pool, tools), how similar rules appear in satellite and hard real-time systems, and whether such constraints still work for modern, AI-heavy workloads.

*Content unavailable; summarizing from title/comments.*

---

## Comment pulse
- C++ over Ada → Easier hiring and richer toolchains; Ada perceived as career-limiting then, though interest is returning via SPARK and safety-critical work.  
- Fixed addresses, no STL/heap → Simplifies mission assurance and in-orbit patching when memory cells die—counterpoint: hardware could blacklist bad addresses dynamically instead.  
- JSF standard as model → Many rules suit embedded/real-time C++; people wonder about exceptions, static-analysis enforcement, and how this scales to adaptive, AI-guided systems.

---

## LLM perspective
- View: Safety-critical C++ here is essentially a domain-specific language defined by coding rules plus analysis tools.  
- Impact: Practices influence avionics, satellites, automotive safety, and even hobbyist embedded C++ cultures.  
- Watch next: How such static allocation and determinism adapt to onboard ML, larger models, and dynamic mission profiles.
