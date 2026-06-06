# The text mode lie: why modern TUIs are a nightmare for accessibility

- Score: 284 | [HN](https://news.ycombinator.com/item?id=48002938) | Link: https://xogium.me/the-text-mode-lie-why-modern-tuis-are-a-nightmare-for-accessibility

### TL;DR
Modern “text” apps in terminals are often less accessible than GUIs. Traditional CLIs stream text linearly, which kernel-level screen readers handle well. React-style TUI frameworks instead treat the terminal as a 2D canvas, constantly diffing and redrawing. This makes cursors jump, floods screen readers with noisy updates, and can introduce multi‑second input lag or even crashes when histories grow. Older tools work because they let users hide the cursor, constrain focus, or use terminal scrolling regions. Ignored accessibility bugs—and “stale bot” closures—compound the harm.

---

### Comment pulse
- Modern TUIs mimic DOS/WordPerfect‑era faux‑window systems, layering escape codes; accessibility and usability end up no better than ancient text GUIs.  
- TUI popularity: devs already live in terminals, ssh works everywhere, cross‑platform packaging is easy, and TUIs dodge Electron’s bloat stigma — counterpoint: many still prefer plain CLIs or web UIs.  
- Maintainers argue “Closed” can mean “not working on this now,” but critics see auto‑closing accessibility bugs in corporate projects as effectively burying them.  

---

### LLM perspective
- View: Treat “terminal = accessible” as false; design explicitly for screen readers, or default to simple streaming CLIs.  
- Impact: TUI framework authors and dev‑tool vendors need cursor‑less/headless modes and stricter guidance on redraw, focus, and dynamic content.  
- Watch next: Benchmarks comparing screen‑reader behavior across TUIs, emergence of accessibility‑first TUI primitives, and policy pressure on large vendors’ terminal tooling.
