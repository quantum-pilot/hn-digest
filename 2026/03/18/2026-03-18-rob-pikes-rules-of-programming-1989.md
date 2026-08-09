# Rob Pike’s Rules of Programming (1989)

- Score: 820 | [HN](https://news.ycombinator.com/item?id=47423647) | Link: https://www.cs.unc.edu/~stotts/COMP590-059-f24/robsrules.html

### TL;DR

Rob Pike’s five rules reduce performance engineering to a disciplined sequence: do not guess bottlenecks; measure before tuning; prefer simple algorithms while inputs stay small; remember sophistication raises constants and bug risk; and design data structures so control flow becomes obvious. HN readers extended the lesson from premature optimization to premature abstraction, arguing that developer time and maintainability often dominate runtime. The main dissent concerned Rule 3: simple quadratic code can explode for large customers, especially when a better standard-library option adds no complexity.

### Comment pulse

- Game developers favored flat arrays because predictable linear access fits frame budgets and helps teams ship quickly.
- One industrial quadratic search added six seconds to a four-hour process, illustrating why measurement can overturn theoretical alarm.
- Rule 5 drew broad support: strong schemas simplify algorithms, while commenters said current LLMs often miss those modeling opportunities.

### LLM perspective

- **View:** Pike’s rules allocate engineering attention through evidence rather than intuition or aesthetic sophistication.
- **Impact:** Teams gain simpler code, faster delivery, and fewer optimizations aimed at imaginary workloads.
- **Watch next:** Profile production distributions and revisit algorithms when input sizes or customer tiers change.
