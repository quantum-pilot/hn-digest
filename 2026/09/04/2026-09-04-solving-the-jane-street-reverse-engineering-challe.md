# Solving the Jane Street reverse engineering challenge

- Score: 419 | [HN](https://news.ycombinator.com/item?id=49562657) | Link: https://jestoph.com/2026/09/04/jane-street-challenge.html

### TL;DR

The author recounts a month-long solution to Jane Street’s ASIC reverse-engineering puzzle: parsing GDS geometry, identifying SKY130 cells, constructing connectivity graphs and Verilog simulations, then translating circuit behavior into Z3 constraints. After finding and reporting a confirmed but nonessential design bug, he reduced the 120-bit search and obtained the accepted output “TWO STARS.” Commenters praised the learning journey and solver insight while observing that existing open-silicon extraction and formal-verification tools could have made the route substantially shorter.

### Comment pulse

- Constraint modeling feels transformative → defined state spaces and redundant constraints can turn opaque puzzles into solver-ready systems.
- Reinventing tools deepened learning → commenters admired persistence but pointed to LibreLane, Magic, Degate, and formal methods.
- The input was unusually rich → supplied GDS layers and standard-cell names avoided harder transistor and logic extraction.

### LLM perspective

- View: The solve demonstrates how simulation, validation, and constraints convert visual complexity into tractable semantics.
- Impact: Learners may trade efficiency for understanding; practitioners should begin with established extraction toolchains.
- Watch next: Reproduce the accepted result and compare custom, formal-verification, and standard open-silicon workflows.
