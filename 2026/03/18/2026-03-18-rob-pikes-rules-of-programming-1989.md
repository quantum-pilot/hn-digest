# Rob Pike’s Rules of Programming (1989)

- Score: 820 | [HN](https://news.ycombinator.com/item?id=47423647) | Link: https://www.cs.unc.edu/~stotts/COMP590-059-f24/robsrules.html

### TL;DR
Rob Pike’s 1989 rules say: don’t guess about performance; measure first and only optimize true hotspots. Prefer simple algorithms and data structures, because “fancy” ones are slower for typical small inputs, harder to implement, and buggier. Good data modeling makes the right algorithms obvious. Hacker News largely agrees, extending this to optimizing for developer time, warning that premature abstraction is often worse than premature optimization, and debating when asymptotic complexity really matters in modern, large‑n domains.

---

### Comment pulse
- Optimize for productivity → ship with simple arrays/linear scans, then profile and selectively improve; this works especially well in game loops and many business apps.  
- Premature abstraction is worse than premature optimization → speculative layers add complexity, cognitive load, and refactor cost—counterpoint: some devs see simplicity/maintainability as the primary rule, not performance.  
- Rule 3 is domain-dependent → for small n, simple O(n²) code is fine; for large or customer-scale n, better big‑O and standard “fancy” algorithms are essential.

---

### LLM perspective
- View: These rules map well to using profilers and production metrics, then asking LLMs to optimize only proven hotspots.  
- Impact: Coding standards can explicitly discourage speculative abstractions and algorithm cleverness without data, improving team velocity and reliability.  
- Watch next: Better tooling that surfaces real performance distributions so assistants can prioritize structural/data-model changes over micro-optimizations.
