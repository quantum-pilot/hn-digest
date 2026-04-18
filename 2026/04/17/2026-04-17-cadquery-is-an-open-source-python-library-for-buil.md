# CadQuery is an open-source Python library for building 3D CAD models

- Score: 216 | [HN](https://news.ycombinator.com/item?id=47772725) | Link: https://cadquery.github.io/

### TL;DR
CadQuery is an open-source Python library for creating fully parametric 3D CAD models as code instead of via a traditional GUI. Users highlight strengths like version control, reusability, and the ability to express complex design intent using Python functions and queries on geometry, making it ideal for 3D-printing workflows and intricate parts. However, it can feel harder than GUI CAD for simple tasks, and keeping geometric selections in mind is mentally taxing, prompting interest in hybrid GUI-that-writes-code tools.

---

### Comment pulse
- Code-first CAD shines on complex, iterated designs (bracelets, helmets, winches) → parameters, scripts, and lists make experimentation and reconfiguration trivial versus manual GUI edits.  
- GUI still wins for simple parts → direct sketching is faster; CadQuery’s relational geometry selections demand cognitive load — counterpoint: tooling like viewers reduces “what did I just select?” confusion.  
- AI helps but cannot yet own the workflow → autocomplete and LLM hints generate snippets and gcode, but spatial reasoning and full-part correctness still require human expertise.

---

### LLM perspective
- View: CadQuery shows “CAD as software” is practical: design intent, refactoring, testing, and reuse become normal programming activities.  
- Impact: Lowers entry barrier for programmers doing hardware, and tightens iteration loops for 3D-printing, cosplay, and hobby engineering projects.  
- Watch next: Mature bidirectional GUI/code editors, geometry-aware LLMs, and shared libraries of parametric components and design patterns.
